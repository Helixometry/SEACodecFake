"""Codec artifact detection module"""

import torch
import torch.nn as nn


class CodecDetector(nn.Module):
    """Detect artifacts from neural audio codecs"""

    def __init__(self, hidden_dim: int = 256):
        super().__init__()
        self.detector = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, 1),
            nn.Sigmoid(),
        )

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        """Detect codec artifacts in features"""
        return self.detector(features)
