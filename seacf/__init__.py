"""SEACodecFake: Neural Audio Codec Deepfake Detection for SEA Languages"""

__version__ = "1.0.0"
__author__ = "Orchid Chetia Phukan, Girish, Mohd Mujtaba Akhtar, Arun Balaji Buduru"
__email__ = "girish281003@gmail.com"

from .garuda import GARUDA
from .codec_detector import CodecDetector

__all__ = ["GARUDA", "CodecDetector"]
