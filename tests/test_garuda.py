"""Unit tests for GARUDA"""

import unittest
import torch
from seacf.garuda import GARUDA

class TestGARUDA(unittest.TestCase):
    def setUp(self):
        self.model = GARUDA(audio_dim=64, hidden_dim=256)

    def test_forward(self):
        audio = torch.randn(4, 100, 64)
        output = self.model(audio)
        self.assertIn('codec_score', output)
        self.assertEqual(output['codec_score'].shape[0], 4)

if __name__ == '__main__':
    unittest.main()
