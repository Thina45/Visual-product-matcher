import React from "react";

const Loader = () => {
  return (
    <div className="flex flex-col items-center justify-center mt-10">
      <div className="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
      <p className="mt-4 text-gray-600 font-medium">
        Finding similar products...
      </p>
    </div>
  );
};

export default Loader;
