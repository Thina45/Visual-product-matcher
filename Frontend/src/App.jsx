import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select an image!");
    setLoading(true);
    const formData = new FormData();
    formData.append("image", file);

    try {
      const res = await axios.post(
        "https://visual-product-matcher-ny0u.onrender.com/match",
        formData
      );
      setResults(res.data);
    } catch (err) {
      console.error(err);
      alert("Error fetching matches.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-3xl font-bold text-center mb-6">
        🖼️ Visual Product Matcher
      </h1>
      <div className="flex flex-col items-center space-y-4">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="border rounded p-2"
        />
        <button
          onClick={handleUpload}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          {loading ? "Processing..." : "Find Similar Products"}
        </button>
      </div>

      {loading && (
        <p className="text-center mt-4 text-gray-600">Analyzing image...</p>
      )}

      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-6">
        {results.map((r) => (
          <div
            key={r.id}
            className="bg-white shadow-md rounded-lg p-3 text-center"
          >
            <img
              src={`https://visual-product-matcher-ny0u.onrender.com/static/product_images/${r.image}`}
              alt={r.name}
              className="w-full h-48 object-cover rounded"
            />
            <h3 className="mt-2 font-semibold">{r.name}</h3>
            <p className="text-gray-500">{r.category}</p>
            <p className="text-green-600 font-medium mt-1">
              Similarity: {r.similarity}%
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
