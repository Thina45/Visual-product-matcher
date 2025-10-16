import streamlit as st
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json, io
from PIL import Image

st.set_page_config(page_title="Visual Product Matcher", layout="wide")

@st.cache_resource
def load_model():
    return MobileNetV2(weights="imagenet", include_top=False, pooling="avg")

@st.cache_data
def load_data():
    with open("database/products.json", "r") as f:
        products = json.load(f)
    product_features = np.load("processed_images.npy", allow_pickle=True)
    if product_features.ndim > 2:
        product_features = product_features.reshape(product_features.shape[0], -1)
    return products, product_features

model = load_model()
products, product_features = load_data()

def extract_features(img_bytes):
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB").resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return model.predict(x, verbose=0).flatten()

st.title("🖼️ Visual Product Matcher")
uploaded = st.file_uploader("Upload a product image:", type=["jpg", "jpeg", "png"])

if uploaded:
    st.image(uploaded, caption="Uploaded Image", width=300)
    features = extract_features(uploaded.read()).reshape(1, -1)
    sims = cosine_similarity(features, product_features)[0]
    top_idx = sims.argsort()[-6:][::-1]

    st.subheader("🔍 Top Matching Products:")
    cols = st.columns(3)
    for i, idx in enumerate(top_idx):
        with cols[i % 3]:
            st.image(f"static/product_images/{products[idx]['image']}", width=200)
            st.write(products[idx]['name'])
            st.write(f"Category: {products[idx]['category']}")
            st.write(f"Similarity: {round(float(sims[idx]) * 100, 2)}%")
