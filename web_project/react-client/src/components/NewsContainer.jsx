import React, { useEffect, useRef, useState } from 'react';
import NewsCard from './NewsCard';
import { ChevronLeft, ChevronRight, AlertCircle } from 'lucide-react';
import DatePicker from './DatePicker';
import { mockNewsData } from '../mockdata/news';

const NavigationButton = ({ direction, onClick, disabled }) => (
  <button
    onClick={onClick}
    disabled={disabled}
    className={`
      p-2 rounded-full hover:bg-gray-100 transition-all duration-200
      ${disabled ? 'text-gray-300 cursor-not-allowed' : 'text-gray-600 hover:text-gray-900'}
    `}
  >
    {direction === 'left' ? 
      <ChevronLeft className="w-5 h-5" /> : 
      <ChevronRight className="w-5 h-5" />
    }
  </button>
);

const NewsContainer = () => {
  const availableDates = Object.keys(mockNewsData).sort();
  const mostRecentDate = availableDates[availableDates.length - 1];
  const [currentDate, setCurrentDate] = React.useState(mostRecentDate);
  const [isHeaderSticky, setIsHeaderSticky] = useState(false);
  const headerRef = useRef(null);
  
  const currentDateIndex = availableDates.findIndex(date => date === currentDate);

  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [currentDate]);

  useEffect(() => {
    const handleScroll = () => {
      const headerHeight = headerRef.current?.offsetHeight || 0;
      setIsHeaderSticky(window.scrollY > headerHeight);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const Header = (
    <div
      ref={headerRef}
      className={`transition-all duration-300 ${
        isHeaderSticky 
          ? 'sticky top-16 bg-white border-b shadow-sm z-10' 
          : 'bg-transparent'
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 sm:py-6">
        <div className="flex items-center justify-between">
          <h2 className="text-lg sm:text-xl lg:text-2xl font-bold text-gray-900 truncate">
            {new Date(currentDate).toLocaleDateString('en-US', {
              month: 'long',
              day: 'numeric',
              year: 'numeric'
            })} News
          </h2>
          
          <div className="flex items-center gap-2 shrink-0">
            <NavigationButton
              direction="left"
              onClick={() => currentDateIndex > 0 && 
                setCurrentDate(availableDates[currentDateIndex - 1])} 
                disabled={false}
            />
            
            <DatePicker 
              selectedDate={currentDate}
              onSelectDate={setCurrentDate}
            />
            
            <NavigationButton
              direction="right"
              onClick={() => currentDateIndex < availableDates.length - 1 && 
                setCurrentDate(availableDates[currentDateIndex + 1])}
              disabled={currentDateIndex === availableDates.length - 1}
            />
          </div>
        </div>
      </div>
    </div>
  );

  if (!mockNewsData[currentDate]?.length) {
    return (
      <div className="min-h-screen bg-gray-50">
        {Header}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-center" style={{ height: 'calc(100vh - 200px)' }}>
          <div className="text-center">
            <AlertCircle className="w-12 h-12 text-gray-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-gray-600 mb-2">No News Available</h3>
            <p className="text-gray-500">There are no news articles for the selected date.</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {Header}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 sm:py-6">
        <div className="flex flex-col gap-4 sm:gap-6">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
            {mockNewsData[currentDate].slice(0, 4).map((news) => (
              <div key={news.id} className="h-full">
                <NewsCard news={news} />
              </div>
            ))}
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6 lg:px-[12.5%]">
            {mockNewsData[currentDate].slice(4, 7).map((news) => (
              <div key={news.id} className="h-full">
                <NewsCard news={news} />
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default NewsContainer;