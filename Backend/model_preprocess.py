import os
import json
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "static\product_images")

# Load model
model = MobileNetV2(weights="imagenet", include_top=False, pooling="avg")

# Load products
with open(os.path.join(BASE_DIR, "database", "products.json"), "r") as f:
    products = json.load(f)

features = []

for p in products:
    img_path = os.path.join(IMG_DIR, p["image"])

    if not os.path.exists(img_path):
        print(f"⚠️ Missing image: {img_path}")
        features.append(np.zeros((1280,)))
        continue

    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    feat = model.predict(img_array)
    features.append(feat.flatten())

features = np.array(features)
np.save(os.path.join(BASE_DIR, "processed_images.npy"), features)

print("✅ Feature extraction complete and saved!")
