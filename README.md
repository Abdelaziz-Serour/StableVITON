# StableVITON Half Dataset Evaluation

This repo evaluates the StableVITON virtual try-on model on the first half of the test dataset.

## 📦 Components

- ✅ Inference pipeline using `StableVITON`
- 📊 Evaluation using FID and LPIPS metrics
- 🔀 Dataset splitting logic
- 📤 Script to upload results as Kaggle dataset

## 🧪 Reproduction Steps

```bash
# Clone repo
git clone https://github.com/YourUsername/StableVITON-Experiment.git
cd StableVITON-Experiment

# Install dependencies
pip install -r requirements.txt

# Run inference on first half
python scripts/run_inference_half1.py

# Compute metrics
python scripts/compute_fid.py
python scripts/compute_lpips.py
