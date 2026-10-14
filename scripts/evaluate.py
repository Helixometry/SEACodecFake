"""Evaluation script for GARUDA"""

import argparse
from seacf.garuda import GARUDA
from seacf.utils import get_device

def main():
    parser = argparse.ArgumentParser(description="Evaluate GARUDA")
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--test-data", type=str, required=True)

    args = parser.parse_args()
    device = get_device()
    model = GARUDA.from_pretrained(args.checkpoint).to(device)
    print(f"Evaluating on {args.test_data}")

if __name__ == "__main__":
    main()
