import React from 'react';
import { useLocation, useNavigate, useParams } from 'react-router-dom';
import { mockNewsData } from '../mockdata/news';

const NewsDetail = () => {
  const { newsTitle } = useParams();
  const location = useLocation();
  const navigate = useNavigate();
  
  const news = location.state?.news || Object.values(mockNewsData)
    .flat()
    .find(news => {
      const urlTitle = news.title
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-+|-+$/g, '');
      return urlTitle === newsTitle;
    });

  const otherNews = news ? mockNewsData[news.date]?.filter(item => item.id !== news.id) : [];

  if (!news) {
    return (
      <div className="fixed inset-0 flex items-center justify-center bg-gray-50">
        <div className="text-center px-4">
          <div className="w-[200px] mx-auto mb-6">
            <svg
              viewBox="0 0 500 500"
              className="w-full h-full"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g clipPath="url(#clip0_0_1)">
                <circle cx="250" cy="250" r="200" fill="#f3f4f6" />
                
                <g transform="translate(250, 220)">
                  <rect x="-50" y="-30" width="100" height="70" fill="#4b5563" rx="5"/>
                  <rect x="-40" y="-20" width="60" height="8" fill="#f3f4f6" rx="2"/>
                  <rect x="-40" y="-5" width="80" height="6" fill="#f3f4f6" rx="2"/>
                  <rect x="-40" y="8" width="70" height="6" fill="#f3f4f6" rx="2"/>
                  <rect x="-40" y="21" width="75" height="6" fill="#f3f4f6" rx="2"/>
                </g>
                
                <circle cx="200" cy="300" r="8" fill="#4b5563" />
                <circle cx="300" cy="300" r="8" fill="#4b5563" />
                <path
                  d="M175 360 C215 340 285 340 325 360"
                  stroke="#4b5563"
                  strokeWidth="10"
                  strokeLinecap="round"
                  fill="none"
                />
              </g>
            </svg>
          </div>
  
          <h1 className="text-4xl font-bold text-gray-900 mb-2">Oops!</h1>
          <h2 className="text-2xl font-semibold text-gray-700 mb-3">
            News article not found
          </h2>
          <p className="text-gray-500 text-base max-w-md mx-auto mb-6">
            The news article you are looking for might have been removed or is temporarily unavailable.
          </p>
  
          <button
            onClick={() => navigate('/news')}
            className="px-6 py-3 bg-blue-600 text-white rounded-lg font-medium 
                     hover:bg-blue-700 transition-colors duration-200
                     focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          >
            Back to News
          </button>
        </div>
      </div>
    );
  }

 const RelatedNews = () => (
   <div className="bg-white border border-gray-200 rounded-lg shadow-sm p-4">
     <h2 className="text-xl font-bold text-gray-900 mb-4">More News From Today</h2>
     <div className="divide-y divide-gray-100">
       {otherNews.map((item, index) => (
         <div 
           key={item.id} 
           className={`py-3 ${index === 0 ? 'pt-0' : ''} ${index === otherNews.length - 1 ? 'pb-0' : ''}`}
         >
           <h3 className="font-medium text-gray-900 text-sm mb-1 line-clamp-1">
             {item.title}
           </h3>
           <p className="text-xs text-gray-600 mb-1 line-clamp-1">
             {item.summary}
           </p>
           <button 
             onClick={() => {
               const urlTitle = item.title
                 .toLowerCase()
                 .replace(/[^a-z0-9]+/g, '-')
                 .replace(/^-+|-+$/g, '');
               navigate(`/news/${urlTitle}`, { state: { news: item } });
             }}
             className="text-xs text-blue-600 hover:text-blue-800 font-medium transition-colors duration-200"
           >
             Read More →
           </button>
         </div>
       ))}
     </div>
   </div>
 );

 return (
   <div className="max-w-7xl mx-auto px-4 py-8">
     <button
       onClick={() => navigate('/news')}
       className="text-blue-600 hover:text-blue-800 mb-6"
     >
       ← Go back
     </button>

     <div className="flex flex-col lg:flex-row gap-10">
       <div className="lg:w-2/3 pb-8">
         <div className="aspect-video w-full mb-6 rounded-lg overflow-hidden relative group">
           <div className="absolute inset-0 bg-black/40"></div>
           <img 
             src={news.image} 
             alt={news.title}
             className="w-full h-full object-cover"
           />
           
           <div className="absolute bottom-4 right-4 max-w-[90%] text-right">
             <h1 className="text-3xl font-bold text-white">{news.title}</h1>
             <div className="text-sm text-gray-200">
               {new Date(news.createdAt).toLocaleString()}
             </div>
           </div>
         </div>
         
         <div className="prose max-w-none">
           <p className="text-gray-600 text-lg mb-4 font-semibold">{news.summary}</p>
           <div className="text-gray-800 leading-relaxed">
             {news.content}
           </div>
         </div>

         <div className="block lg:hidden mt-8">
           <RelatedNews />
         </div>
       </div>

       <div className="hidden lg:block lg:w-1/3">
         <div className="fixed w-[calc(100%/3-3rem)] max-w-sm top-16">
           <div className="my-4">
             <RelatedNews />
           </div>
         </div>
       </div>
     </div>
   </div>
 );
};

export default NewsDetail;