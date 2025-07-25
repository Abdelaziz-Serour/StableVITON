import subprocess

print("[INFO] Computing FID for first half...")

fid_output_path = "results/fid_half1.txt"
with open(fid_output_path, "w") as out_file:
    subprocess.run([
        "python", "-m", "cleanfid",
        "--mode", "clean",
        "--kid", "False",
        "--dataset-path-fake", "results_half1/pair",
        "--dataset-path-real", "dataset/test/image"
    ], stdout=out_file, stderr=subprocess.STDOUT)

print(f"✅ FID computed and saved to: {fid_output_path}")
