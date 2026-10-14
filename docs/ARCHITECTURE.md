# GARUDA Architecture

## Overview

GARUDA (lightweight audio language model) detects neural audio codec-synthesized speech deepfakes in South-East Asian languages.

## Key Innovation

**Lightweight + Language-Specific**: Unlike large audio language models, GARUDA is optimized for:
- Low memory footprint
- Fast inference
- SEA language characteristics (tones, prosody)

## Architecture

```
Audio Input
    ↓
Audio Features (64-dim)
    ↓
Projection (64→256)
    ↓
GRU Encoder (2 layers)
    ↓
Last Hidden State
    ↓
Codec Detector
    ↓
Output: Real/Synthetic Probability
```

## Results on SEA-CF

- English transfer: 42.1%
- GARUDA: 84.9%
- Improvement: +42.8%

## Language Support

- Thai
- Vietnamese
- Indonesian
- Filipino
