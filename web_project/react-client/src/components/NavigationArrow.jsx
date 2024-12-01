import React from 'react';
import { ChevronUp, ChevronDown } from 'lucide-react';

const NavigationArrow = ({ direction, onClick, disabled }) => {
  const baseStyles = `
    w-10 h-10 flex items-center justify-center
    rounded-full transition-all duration-200
    focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500
  `;

  const activeStyles = `
    bg-white border border-gray-200 shadow-sm
    hover:bg-gray-50 hover:shadow-md
    text-gray-700 hover:text-gray-900
  `;

  const disabledStyles = `
    bg-gray-100 cursor-not-allowed
    text-gray-400 border border-gray-200
  `;

  const containerStyles = `
    absolute right-0 z-10
    ${direction === 'up' ? '-top-5' : '-bottom-5'}
  `;

  return (
    <div className={containerStyles}>
      <button
        onClick={onClick}
        disabled={disabled}
        className={`${baseStyles} ${disabled ? disabledStyles : activeStyles}`}
        aria-label={`Navigate to ${direction === 'up' ? 'next' : 'previous'} day's news`}
      >
        {direction === 'up' ? (
          <ChevronUp className="w-6 h-6" />
        ) : (
          <ChevronDown className="w-6 h-6" />
        )}
      </button>
    </div>
  );
};

export default NavigationArrow;