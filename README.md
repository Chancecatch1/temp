# Beyond Jupyter - Deep Learning Project Template

> A template for transitioning from Jupyter Notebooks to production-ready Python code

## Overview

A project template for those who want to move beyond Jupyter Notebooks to structured Python projects. Uses CIFAR-10 image classification as an example to demonstrate production-level code organization.

## Key Features

- **Modular Structure**: Separated datasets, models, training modules
- **CIFAR-10 Example**: Ready-to-run image classification
- **CLI-based Execution**: Simple command-line training
- **Extensible**: Easy to swap datasets and models

## Quick Start

```bash
git clone https://github.com/Chancecatch1/temp.git
cd temp
python datasets.py   # Download dataset
python main.py       # Start training
```

## Project Structure

```
temp/
├── main.py         # Main execution script
├── models.py       # Model architecture definitions
├── datasets.py     # Dataset loading and preprocessing
└── training.py     # Training loop and utilities
```

## Tech Stack

- Python 3.8+
- PyTorch
- torchvision (CIFAR-10)

## Why This Template?

| Jupyter Notebook | This Template |
|-----------------|---------------|
| Cell-by-cell execution | Module-based execution |
| Global state issues | Clear function/class structure |
| Reproducibility issues | Consistent CLI execution |
| Version control challenges | Git-friendly structure |
