import numpy as np
import os, json
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load model
print("🧠 Loading ResNet50 model...")
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Paths
data_dir = "V:/D/WebDevelopment/Unthinkable/Visual Product matcher/Backend/static/product_images"  # folder with product images
json_path = "database/products.json"
output_path = "processed_images.npy"

# Load product metadata
with open(json_path) as f:
    products = json.load(f)

features = []

print("⚙️ Extracting features...")
for prod in products:
    img_path = os.path.join(data_dir, prod["image"])
    try:
        img = Image.open(img_path).convert("RGB").resize((224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        feat = model.predict(x)
        features.append(feat.flatten())
    except Exception as e:
        print(f"❌ Error processing {img_path}: {e}")

# Save all features
features = np.array(features)
np.save(output_path, features)
print(f"✅ Saved {len(features)} features to {output_path}")
