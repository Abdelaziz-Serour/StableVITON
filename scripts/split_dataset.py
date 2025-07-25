with open("dataset/test_pairs_full.txt", "r") as f:
    lines = f.readlines()

half = len(lines) // 2

with open("dataset/test_pairs_half1.txt", "w") as f:
    f.writelines(lines[:half])

# overwrite the current test_pairs
with open("dataset/test_pairs.txt", "w") as f:
    f.writelines(lines[:half])

print("✅ Dataset split and test_pairs updated.")