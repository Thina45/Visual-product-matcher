# 🧠 Visual Product Matcher

An AI-powered **Visual Product Matching System** that identifies and matches products based on image similarity.  
Built using **Flask (Python)** for the backend and **React.js** for the frontend, it leverages a pre-trained **ResNet50** deep learning model to extract image features and perform cosine similarity matching between uploaded and existing product images.

---

## 🚀 Features

- 🧩 Upload a query image (e.g., clothing, shoes, accessories)
- 🤖 Extract image embeddings using ResNet50 (TensorFlow)
- 📊 Compare with stored product embeddings using cosine similarity
- 🔍 Return top visually similar products instantly
- 🌐 Deployed backend on **Render**
- ⚛️ Deployed frontend on **Vercel**

---

## 🏗️ Tech Stack

### Frontend
- React.js  
- Axios (for API calls)  
- TailwindCSS (for styling)  
- Deployed on **Vercel**

### Backend
- Python (Flask)  
- TensorFlow / Keras (ResNet50 model)  
- scikit-learn (Cosine Similarity)  
- Flask-CORS (for frontend-backend connection)  
- Deployed on **Render**

---

## ⚙️ Project Structure



Visual Product Matcher/
│
├── Backend/
│ ├── app.py # Flask API with image processing
│ ├── requirements.txt # Python dependencies
│ ├── render.yaml # Render deployment config
│ ├── database/
│ │ ├── products.json # Product data
│ │ └── processed_images.npy # Precomputed image features
│ └── static/uploads/ # Uploaded query images
│
├── Frontend/
│ ├── src/
│ │ ├── App.jsx # Main React component
│ │ ├── components/ # UI components
│ │ └── assets/ # Static assets
│ ├── package.json
│ └── vite.config.js
│
└── README.md


---

## 🧩 Setup Instructions (Local)

### 🖥️ Backend Setup

```bash
cd Backend
python -m venv venv
venv\Scripts\activate        # (Windows)
pip install -r requirements.txt
python app.py


Backend runs on:

http://127.0.0.1:5000

💻 Frontend Setup
cd Frontend
npm install
npm run dev


Frontend runs on:

http://localhost:5173

🌍 Deployment
🔹 Backend (Render)

Push your backend to GitHub.

Go to Render
 → Create a New Web Service.

Connect your GitHub repo and select the Backend folder.

Use the following start command:

gunicorn app:app


Add a render.yaml file in Backend/:

services:
  - type: web
    name: visual-product-matcher
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app

🔹 Frontend (Vercel)

Go to Vercel
 → Import your GitHub repo.

Set:

Build Command: npm run build

Output Directory: dist

Update your API URL in App.jsx:

const API_URL = "https://visual-product-matcher-1-8jsy.onrender.com";

🧪 Example Usage

Upload a query image (e.g., a shoe or t-shirt).

Backend extracts its ResNet50 feature vector.

Compares it with features of stored product images.

Returns top visually similar products based on cosine similarity.

🛠️ Troubleshooting
🔸 CORS Error

Add this in app.py:

from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": "*"}})

🔸 GPU Not Found Warning

Safe to ignore — TensorFlow automatically switches to CPU.

✨ Future Enhancements

Add product upload portal

Integrate MongoDB / PostgreSQL for product storage

Use CLIP or ViT for better semantic understanding

Add search filters and categories

👨‍💻 Author

P Thinakaran
📍 MCA Student at VIT Vellore
💼 GitHub
 | LinkedIn

⭐ If you found this project helpful, give it a star!

“Turning pixels into insights — one image at a time.”


---

Would you like me to add **badges** (e.g., “Made with Flask”, “Deployed on Render”, “Frontend: Vercel”, etc.) to
