"""GARUDA: Lightweight Audio Language Model for Codecfake Detection"""

import torch
import torch.nn as nn
from typing import Dict, Optional


class GARUDA(nn.Module):
    """
    GARUDA: Lightweight Audio Language Model for SEA Codecfake Detection.

    Designed for South-East Asian speech with minimal parameters.

    Args:
        audio_dim (int): Audio feature dimension
        hidden_dim (int): Hidden dimension
        num_layers (int): Number of layers
        dropout (float): Dropout probability
    """

    def __init__(
        self,
        audio_dim: int = 64,
        hidden_dim: int = 256,
        num_layers: int = 2,
        dropout: float = 0.3,
    ):
        super().__init__()
        self.audio_dim = audio_dim
        self.hidden_dim = hidden_dim

        # Audio projection
        self.audio_proj = nn.Linear(audio_dim, hidden_dim)

        # Lightweight encoder
        self.encoder = nn.GRU(hidden_dim, hidden_dim, num_layers, batch_first=True, dropout=dropout)

        # Codec detection head
        self.codec_detector = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, 1),
            nn.Sigmoid(),
        )

    def forward(self, audio_features: torch.Tensor) -> Dict[str, torch.Tensor]:
        """Forward pass of GARUDA."""
        # Project audio features
        x = self.audio_proj(audio_features)

        # Encode
        out, _ = self.encoder(x)

        # Use last hidden state
        last_hidden = out[:, -1, :]

        # Detect codec artifacts
        codec_score = self.codec_detector(last_hidden)

        return {
            "codec_score": codec_score.squeeze(-1),
            "real_prob": 1 - codec_score.squeeze(-1),
            "features": last_hidden,
        }

    @classmethod
    def from_pretrained(cls, checkpoint_path: str) -> "GARUDA":
        """Load pretrained GARUDA model."""
        checkpoint = torch.load(checkpoint_path, map_location="cpu")
        config = checkpoint.get("config", {})
        model = cls(**config)
        model.load_state_dict(checkpoint["model_state_dict"])
        model.eval()
        return model

    def save(self, checkpoint_path: str, config: Optional[Dict] = None) -> None:
        """Save GARUDA model checkpoint."""
        checkpoint = {
            "model_state_dict": self.state_dict(),
            "config": config or {
                "audio_dim": self.audio_dim,
                "hidden_dim": self.hidden_dim,
            },
        }
        torch.save(checkpoint, checkpoint_path)
