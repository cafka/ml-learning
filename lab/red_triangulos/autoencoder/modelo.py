import torch
from torch import nn

class Autoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.capa1 = nn.Linear(28*28, 64)
        self.capa2 = nn.ReLU()
        self.capa3 = nn.Linear(64,16)
        self.linear_relu_stack_enc = nn.Sequential(
            self.capa1,
            self.capa2,
            self.capa3,
        )
        self.capa4 = nn.Linear(16, 64)
        self.capa5 = nn.ReLU()
        self.capa6 = nn.Linear(64, 784)
        self.linear_relu_stack_dec = nn.Sequential(
            self.capa4,
            self.capa5,
            self.capa6,
        )

    def forward(self, x):
        x_latente_enc = self.linear_relu_stack_enc(x)
        x_out_dec = self.linear_relu_stack_dec(x_latente_enc)
        return x_out_dec