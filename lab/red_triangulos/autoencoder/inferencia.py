import torch
import matplotlib.pyplot as plt
from generadores import dataset as ds
from . import modelo as mod
import numpy as np

# Cargar el modelo entrenado
model = mod.Autoencoder()
model.load_state_dict(
    torch.load("autoencoder_latente_16_v9.pth", weights_only=True)
)
model.eval()
np.random.seed(42)
# Generar un triángulo nuevo
cant_imagenes = 5
dataset = ds.crear_dataset(cant_imagenes, 28, 28)
triangulo = ds.dataset_normalizado(dataset)

for i in range(cant_imagenes):
    # Ejecutar inferencia
    with torch.no_grad():
        reconstruccion_i = model(triangulo[i])

    # Preparar las imágenes
    original = triangulo[i].reshape(28, 28).cpu().numpy()
    resultado = reconstruccion_i.reshape(28, 28).cpu().numpy()

    # Visualizar
    fig, axes = plt.subplots(1, 2)

    axes[0].imshow(original, cmap="gray", vmin=0, vmax=1)
    axes[0].set_title("Original")

    axes[1].imshow(resultado, cmap="gray", vmin=0, vmax=1)
    axes[1].set_title(f"Reconstrucción {i}")

    plt.savefig(f"reconstruccion_latente_16_v9_{i}.png")

    plt.close()