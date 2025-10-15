import React, { useState } from "react";

const UploadBox = ({ onUpload }) => {
  const [image, setImage] = useState(null);

  const handleChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
      onUpload(file);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center border-2 border-dashed border-gray-400 rounded-2xl p-6 bg-gray-50 hover:bg-gray-100 transition">
      <label className="cursor-pointer text-center">
        <input
          type="file"
          accept="image/*"
          className="hidden"
          onChange={handleChange}
        />
        <span className="text-lg font-semibold text-gray-600">
          Click or drag image to upload
        </span>
      </label>
      {image && (
        <img
          src={image}
          alt="preview"
          className="mt-4 rounded-xl w-48 h-48 object-cover shadow"
        />
      )}
    </div>
  );
};

export default UploadBox;
