import lpips, torch, os
from PIL import Image
from torchvision import transforms
from tqdm import tqdm

print("[INFO] Computing LPIPS for first half...")

lpips_fn = lpips.LPIPS(net='alex').cuda()
transform = transforms.Compose([
    transforms.Resize((256, 192)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

real_path = "dataset/test/image"
fake_path = "results_half1/pair"
scores = []
matched = 0

for fname in tqdm(os.listdir(fake_path)):
    real_img = os.path.join(real_path, fname.split('_')[0] + ".jpg")
    fake_img = os.path.join(fake_path, fname)
    if not os.path.exists(real_img):
        continue
    try:
        i1 = transform(Image.open(real_img).convert("RGB")).unsqueeze(0).cuda()
        i2 = transform(Image.open(fake_img).convert("RGB")).unsqueeze(0).cuda()
        score = lpips_fn(i1, i2).item()
        scores.append(score)
        matched += 1
    except:
        continue

avg_lpips = sum(scores) / matched if matched > 0 else float('nan')

with open("results/results_half1_metrics.csv", "a") as f:
    f.write(f"Avg LPIPS,{avg_lpips:.4f}\n")
    f.write(f"Num Images,{matched}\n")

print("✅ LPIPS computed and appended to metrics CSV")