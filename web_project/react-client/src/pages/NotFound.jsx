import React from 'react';
import { useNavigate } from 'react-router-dom';

const NotFound = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center bg-gray-50 px-4">
      <div className="text-center">
        <div className="max-w-[350px] mx-auto mb-8">
          <svg
            viewBox="0 0 500 500"
            className="w-full h-full"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g clipPath="url(#clip0_0_1)">
              <circle cx="250" cy="250" r="200" fill="#f3f4f6" />
              
              <text
                x="250"
                y="220"
                fontSize="100"
                fontWeight="bold"
                fill="#4b5563"
                textAnchor="middle"
              >
                404
              </text>
              
              {/* Sad face */}
              <circle cx="200" cy="280" r="8" fill="#4b5563" /> {/* Left eye */}
              <circle cx="300" cy="280" r="8" fill="#4b5563" /> {/* Right eye */}
              <path
                d="M175 340 C215 320 285 320 325 340"
                stroke="#4b5563"
                strokeWidth="10"
                strokeLinecap="round"
                fill="none"
              />
            </g>
          </svg>
        </div>

        <div className="mb-8">
          <h1 className="text-6xl font-bold text-gray-900 mb-3">Oops!</h1>
          <h2 className="text-3xl font-semibold text-gray-700 mb-4">
            Page not found
          </h2>
          <p className="text-gray-500 text-lg max-w-md mx-auto">
            The page you are looking for might have been removed, had its name changed, 
            or is temporarily unavailable.
          </p>
        </div>

        <div className="space-x-4">
          <button
            onClick={() => navigate('/')}
            className="px-6 py-3 bg-blue-600 text-white rounded-lg font-medium 
                     hover:bg-blue-700 transition-colors duration-200
                     focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          >
            Go Home
          </button>
        </div>
      </div>
    </div>
  );
};

export default NotFound;