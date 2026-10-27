import torch
from torch import nn

class Autoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.capa1 = nn.Linear(28*28, 64)
        self.capa2 = nn.ReLU()
        self.capa3 = nn.Linear(64,2)
        self.linear_relu_stack = nn.Sequential(
            self.capa1,
            self.capa2,
            self.capa3,
        )

    def forward(self, x):
        x_latente = self.linear_relu_stack(x)
        return x_latente