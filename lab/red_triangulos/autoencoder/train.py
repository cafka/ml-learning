import torch
from torch import nn
from generadores import dataset as ds
import numpy as np
from . import modelo as mod

import time


def train_loop(model, loss_fn, optimizer, total_size, batch_size, x_img_size, y_img_size):
    #np.random.seed(42)
    iteraciones = total_size//batch_size

    # Set the model to training mode - important for batch normalization and dropout layers
    # Unnecessary in this situation but added for best practices
    model.train()

    for i in range(iteraciones):
        dataset = ds.crear_dataset(batch_size,x_img_size,y_img_size)
        batch_normalizado = ds.dataset_normalizado(dataset)
        # Compute prediction and loss
        pred = model(batch_normalizado)
        loss = loss_fn(pred, batch_normalizado)

        # Backpropagation
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        loss, current = loss.item(), batch_size*(i+1)
        print(f"loss: {loss:>7f}  [{current:>5d}/{total_size:>5d}]")



def main():
    total_size = 50000
    batch_size = 100
    x_img_size = 28
    y_img_size = 28

    model = mod.Autoencoder()
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    cant_epocas = 100
    np.random.seed(42)
    inicio_entrenamiento = time.perf_counter()
    for epoch in range(cant_epocas):
        inicio_epoca = time.perf_counter()
        train_loop(
            model=model,
            loss_fn=loss_fn,
            optimizer=optimizer,
            total_size=total_size,
            batch_size=batch_size,
            x_img_size=x_img_size,
            y_img_size=y_img_size
        )
        duracion_epoca = time.perf_counter() - inicio_epoca
        tiempo_total = time.perf_counter() - inicio_entrenamiento

        epocas_completadas = epoch + 1
        promedio = tiempo_total / epocas_completadas
        tiempo_restante = promedio * (cant_epocas - epocas_completadas)

        print(
            f"Época {epocas_completadas}/{cant_epocas} | "
            f"Duración: {duracion_epoca:.2f} s | "
            f"Transcurrido: {tiempo_total / 60:.2f} min | "
            f"Restante estimado: {tiempo_restante / 60:.2f} min"
        )

    torch.save(model.state_dict(), "autoencoder_latente_16_v9.pth")

if __name__ == "__main__":
    main()
    
'''
def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    # Set the model to training mode - important for batch normalization and dropout layers
    # Unnecessary in this situation but added for best practices
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        # Compute prediction and loss
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * batch_size + len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test_loop(dataloader, model, loss_fn):
    # Set the model to evaluation mode - important for batch normalization and dropout layers
    # Unnecessary in this situation but added for best practices
    model.eval()
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    # Evaluating the model with torch.no_grad() ensures that no gradients are computed during test mode
    # also serves to reduce unnecessary gradient computations and memory usage for tensors with requires_grad=True
    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
'''
