import os
import time
import subprocess

print("[INFO] Running inference on first half of dataset...")
start = time.time()

subprocess.run([
    "python", "inference.py",
    "--config_path", "configs/VITONHD.yaml",
    "--batch_size", "4",
    "--model_load_path", "ckpts/VITONHD.ckpt",
    "--save_dir", "results_half1"
])

end = time.time()
inference_time = end - start
print(f"✅ Inference completed in {inference_time:.2f} seconds")

with open("results/results_half1_metrics.csv", "a") as f:
    f.write(f"Inference Time (s),{inference_time:.2f}\n")