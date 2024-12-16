import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import About from '../pages/About';
import Analysis from '../pages/Analysis';
import Layout from '../components/Layout';
import NotFound from '../pages/NotFound';
import NewsDetail from '../pages/NewsDetail';
import News from '../pages/News';


const AppRouter = () => {
  return (
    <Router>
        <Routes>
            <Route path="/" element={<Layout />}>
                <Route index element={<Home />} />
                <Route path="about" element={<About />} />
                <Route path="analysis" element={<Analysis />} />
                <Route path="news" element={<News />} />
                <Route path="news/:newsTitle" element={<NewsDetail />} />
            </Route>
            
            <Route path="*" element={<NotFound />} />
        </Routes>
    </Router>
  );
};

//? Gonna use this part after creating login and register
// const ProtectedRoute = ({ children }) => {
//   const isAuthenticated = false; 
  
//   if (!isAuthenticated) {
//     return <Navigate to="/login" replace state={{ from: location }} />;
//   }

//   return children;
// };

export default AppRouter;