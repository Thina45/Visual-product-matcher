from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
from PIL import Image
import io

app = Flask(__name__)

# ✅ Fixed CORS setup
CORS(app, resources={r"/*": {"origins": [
    "https://visualmatcher1.vercel.app",
    "http://localhost:3000"
]}}, supports_credentials=True)

print("🧠 Loading MobileNetV2 model (lightweight)...")
model = MobileNetV2(weights="imagenet", include_top=False, pooling="avg")

with open('database/products.json', 'r') as f:
    products = json.load(f)

product_features = np.load('processed_images.npy', allow_pickle=True)
if product_features.ndim > 2:
    product_features = product_features.reshape(product_features.shape[0], -1)

def extract_features(img_bytes):
    try:
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB").resize((224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        features = model.predict(x, verbose=0)
        return features.flatten()
    except Exception as e:
        print("❌ Feature extraction failed:", e)
        return np.zeros((1280,))

@app.route('/')
def home():
    return jsonify({"message": "✅ Visual Product Matcher API running with MobileNetV2!"})

@app.route('/match', methods=['POST'])
def match():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    img_bytes = request.files['image'].read()
    query_features = extract_features(img_bytes).reshape(1, -1)
    similarities = cosine_similarity(query_features, product_features)[0]
    top_indices = similarities.argsort()[-6:][::-1]

    results = [
        {**products[i], 'similarity': round(float(similarities[i]) * 100, 2)}
        for i in top_indices
    ]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
