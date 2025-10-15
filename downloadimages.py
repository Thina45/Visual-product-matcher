import json
import requests
from pathlib import Path

# ✅ Always use raw string for Windows paths
with open(r"V:\D\WebDevelopment\Unthinkable\Visual Product matcher\Backend\database\products.json", "r") as f:
    data = json.load(f)

# ✅ Make sure all parent folders exist
output_dir = Path(r"V:\D\WebDevelopment\Unthinkable\Visual Product matcher\Backend\static\product_images")
output_dir.mkdir(parents=True, exist_ok=True)

# ✅ Add browser headers to avoid 403/HTML issues
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for item in data:
    img_path = output_dir / item["image"]
    if not img_path.exists():
        print(f"Downloading {item['name']}...")
        try:
            r = requests.get(item["url"] + "?auto=format&fit=crop&w=600&q=80", headers=headers, timeout=15)
            if r.status_code == 200 and r.headers.get("Content-Type", "").startswith("image"):
                with open(img_path, "wb") as f:
                    f.write(r.content)
            else:
                print(f"⚠️ Failed {item['name']} — {r.status_code}, {r.headers.get('Content-Type')}")
        except Exception as e:
            print(f"❌ Error downloading {item['name']}: {e}")

print("✅ All valid images downloaded!")
