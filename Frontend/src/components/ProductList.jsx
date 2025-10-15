import React, { useState } from "react";
import UploadBox from "./uploadBox";
import Loader from "./Loader";

const ProductSearch = () => {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [uploadedImage, setUploadedImage] = useState(null);

  const handleUpload = async (file) => {
    setLoading(true);
    setResults([]);
    setUploadedImage(URL.createObjectURL(file));

    const formData = new FormData();
    formData.append("image", file);

    try {
      const res = await fetch("http://127.0.0.1:5000/match", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResults(data);
    } catch (err) {
      console.error("❌ Error fetching results:", err);
    }

    setLoading(false);
  };

  return (
    <div className="max-w-5xl mx-auto mt-10 p-4">
      <h1 className="text-3xl font-bold text-center mb-8 text-blue-600">
        🖼️ Visual Product Matcher
      </h1>

      <UploadBox onUpload={handleUpload} />

      {loading && <Loader />}

      {uploadedImage && !loading && (
        <div className="mt-10">
          <h2 className="text-xl font-semibold mb-4">Uploaded Image:</h2>
          <img
            src={uploadedImage}
            alt="Uploaded"
            className="w-64 h-64 object-cover rounded-xl shadow-lg"
          />
        </div>
      )}

      {results.length > 0 && (
        <div className="mt-10">
          <h2 className="text-xl font-semibold mb-4">Similar Products:</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            {results.map((p) => (
              <div
                key={p.id}
                className="border rounded-2xl p-3 shadow hover:shadow-lg transition"
              >
                <img
                  src={`http://127.0.0.1:5000/static/product_images/${p.image}`}
                  alt={p.name}
                  className="w-full h-48 object-cover rounded-lg"
                />
                <h3 className="mt-2 text-md font-semibold">{p.name}</h3>
                <p className="text-gray-600 text-sm">{p.category}</p>
                <p className="text-blue-600 font-semibold">
                  {p.similarity}% match
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ProductSearch;
