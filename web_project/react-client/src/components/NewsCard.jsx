const NewsCard = ({ news }) => {
  return (
    <div className="bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300 h-full flex flex-col">
      <div className="aspect-[16/9] w-full overflow-hidden rounded-t-lg">
        <img 
          src={news.image} 
          alt={news.title}
          className="w-full h-full object-cover"
        />
      </div>
      
      <div className="flex flex-col flex-grow p-3 sm:p-4">
        <h3 className="font-bold text-base sm:text-lg text-gray-900 mb-2 line-clamp-2">
          {news.title}
        </h3>
        
        <p className="text-sm text-gray-600 line-clamp-3">
          {news.summary}
        </p>
        
        <div className="mt-auto pt-3 flex justify-end">
          <button className="text-blue-600 hover:text-blue-800 text-sm font-medium transition-colors duration-200">
            Read More →
          </button>
        </div>
      </div>
    </div>
  );
};

export default NewsCard;