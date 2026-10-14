"""Inference script for GARUDA"""

import argparse
from pathlib import Path
from seacf.garuda import GARUDA
from seacf.utils import get_device

def main():
    parser = argparse.ArgumentParser(description="GARUDA inference")
    parser.add_argument("--audio", type=str, required=True)
    parser.add_argument("--checkpoint", type=str, required=True)

    args = parser.parse_args()
    device = get_device()
    model = GARUDA.from_pretrained(args.checkpoint).to(device)
    print(f"\nSEACodecFake Detection Results")
    print("=" * 60)
    print(f"Audio: {Path(args.audio).name}")
    print(f"\n(Placeholder inference)")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
