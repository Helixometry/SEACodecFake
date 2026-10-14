# SEACodecFake: Neural Audio Codec-Synthesized Speech Deepfakes in South-East Asian Languages

<div align="center">

[![Paper](https://img.shields.io/badge/Paper-IJCAI%202026-blue)](https://www.ijcai.org/proceedings/2026/791)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-ee4c2c)](https://pytorch.org/)

Neural audio codec deepfake detection benchmark for South-East Asian languages

</div>

## Overview

**SEACodecFake (SEA-CF)** is the first large-scale benchmark for detecting neural audio codec-synthesized speech deepfakes in South-East Asian languages. We introduce **GARUDA**, a lightweight audio language model specifically designed for codecfake detection that achieves state-of-the-art performance.

### Key Problem

Current codecfake detectors:
- Trained primarily on English data
- Fail dramatically on SEA languages
- Don't account for phonetic structure, tonal variation, and prosody of SEA languages
- Existing benchmarks lack SEA language coverage

### Key Solution

**GARUDA**: A lightweight audio language model that:
1. **Bridges SEA Gap** - Trained on SEA-CF benchmark
2. **Lightweight Design** - Suitable for low-resource and latency-constrained environments
3. **Strong Performance** - Outperforms large audio language models
4. **Language-Specific** - Captures SEA phonetics and prosody

Achieves **state-of-the-art results** on SEA-CF benchmark.

## Paper

**Bridging the SEA Gap: An Initial Benchmark for Neural Audio Codec-Synthesized Speech Deepfakes in South-East Asian Languages**

- **Authors**: Orchid Chetia Phukan, Girish, Mohd Mujtaba Akhtar, Arun Balaji Buduru
- **Conference**: IJCAI 2026, Paper 791
- **Paper Link**: [IJCAI Proceedings](https://www.ijcai.org/proceedings/2026/791)

## SEA-CF Dataset

### Coverage

- **Languages**: Multiple South-East Asian languages
  - Thai
  - Vietnamese
  - Indonesian
  - Filipino
  - And more...

- **Data**: Real speech corpora from public sources
- **Codecs**: Multiple neural audio codec architectures
- **Task**: Binary classification (Real/Synthetic)

### Dataset Scale

- Multiple SEA languages
- Diverse speaker demographics
- 14+ codec architectures
- Real and codec-synthesized paired samples

## GARUDA Framework

### Architecture

```
Input SEA Speech Audio
    ↓
┌─────────────────────────────┐
│   Audio Feature Extraction  │
│   (Phonetic/Tonal)         │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│   Language-Specific         │
│   Audio Language Model      │
│   (Lightweight)             │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│   Codec Artifact Detection  │
│   Module                    │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│   Classification Head       │
│   (Real/Synthetic)          │
└─────────────────────────────┘
```

### Key Design Principles

1. **Lightweight** - Smaller than full audio language models
2. **Language-Aware** - Captures SEA linguistic features
3. **Efficient** - Low latency and memory footprint
4. **Effective** - State-of-the-art performance

## Quick Start

### Installation

```bash
git clone https://github.com/Helixometry/SEACodecFake.git
cd SEACodecFake

pip install -r requirements.txt
```

### Training

```bash
python scripts/train.py --config configs/config_garuda.yaml
```

### Evaluation

```bash
python scripts/evaluate.py --checkpoint models/garuda_best.pt --test-data data/sea_cf_test
```

### Inference

```bash
python scripts/inference.py --audio sea_speech.wav --checkpoint models/garuda_best.pt
```

## Results

### Performance on SEA-CF

| Model | English (Transfer) | SEA Languages | Improvement |
|-------|------------------|---------------|------------|
| English Detector | 85.2% | 42.1% | - |
| Audio LM (Zero-shot) | 78.5% | 68.3% | +26.2% |
| Audio LM (Fine-tuned) | 89.1% | 82.5% | +40.4% |
| **GARUDA** | **88.7%** | **84.9%** | **+42.8%** |

### Key Findings

- Fine-tuning helps but large models are impractical
- GARUDA achieves comparable performance with minimal parameters
- Language-specific training crucial for SEA languages
- Codec-specific patterns differ from vocoder-based deepfakes

## Repository Structure

```
SEACodecFake/
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
│
├── seacf/                       # Main package
│   ├── __init__.py
│   ├── garuda.py                # GARUDA model
│   ├── audio_encoder.py         # Audio feature extraction
│   ├── codec_detector.py        # Codec artifact detection
│   ├── utils.py
│   └── metrics.py
│
├── data/                        # Data handling
│   ├── __init__.py
│   ├── loaders.py               # SEA-CF dataset loaders
│   ├── preprocessor.py          # Audio preprocessing
│   └── augmentation.py          # Data augmentation
│
├── scripts/                     # Training/evaluation
│   ├── train.py
│   ├── evaluate.py
│   ├── inference.py
│   └── __init__.py
│
├── configs/                     # Configuration files
│   ├── config_garuda.yaml
│   └── config_baseline.yaml
│
├── tests/                       # Unit tests
│   ├── test_model.py
│   ├── test_codec_detection.py
│   └── __init__.py
│
└── docs/                        # Documentation
    ├── ARCHITECTURE.md
    ├── TRAINING.md
    └── SEA_LANGUAGES.md
```

## Key Features

🌏 **SEA Language Focus** - First benchmark for SEA codecfake detection  
🎤 **Lightweight Model** - GARUDA designed for resource-constrained environments  
📊 **Comprehensive Evaluation** - Zero-shot and fine-tuned results  
🔍 **Codec Analysis** - Understanding codecfake-specific artifacts  
🌐 **Multilingual** - Support for multiple SEA languages  
⚡ **Low Latency** - Efficient inference model  

## Citation

```bibtex
@inproceedings{phukan2026sea,
  title={Bridging the SEA Gap: An Initial Benchmark for Neural Audio Codec-Synthesized Speech Deepfakes in South-East Asian Languages},
  author={Phukan, Orchid Chetia and Girish and Akhtar, Mohd Mujtaba and Buduru, Arun Balaji},
  booktitle={Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},
  pages={791},
  year={2026}
}
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Authors

- **Orchid Chetia Phukan**
- **Girish** - girish281003@gmail.com
- **Mohd Mujtaba Akhtar**
- **Arun Balaji Buduru**

## Acknowledgments

- IJCAI 2026 organizers
- SEA language resource providers
- Codecfake research community
- Audio codec researchers

---

<div align="center">

**Advancing deepfake detection across South-East Asian languages**

</div>
