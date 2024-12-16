import React, { useState } from 'react';
import { Link, NavLink, Outlet } from 'react-router-dom';
import { urls } from './urls';

const Layout = () => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const getLinkClassName = ({ isActive }) => {
    return `px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200 
      ${isActive 
        ? 'text-blue-600 font-semibold bg-blue-50' 
        : 'text-gray-600 hover:text-gray-900'}`;
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow-md fixed w-full top-0 z-40">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex justify-between items-center h-16">
            <div className="flex-shrink-0">
              <Link to="/" className="text-xl font-bold text-gray-800">
                AI Research Labs
              </Link>
            </div>

            {/* Desktop Navigation */}
            <div className="hidden md:flex items-center space-x-8 ml-auto">
              {urls.map((link) => (
                <NavLink
                  key={link.path}
                  to={link.path}
                  className={getLinkClassName}
                >
                  {link.title}
                </NavLink>
              ))}
            </div>

            {/* Mobile menu button */}
            <div className="flex md:hidden">
              <button
                onClick={() => setIsSidebarOpen(true)}
                className="text-2xl"
              >
                ☰
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="pt-16">
        <Outlet />
      </main>

      <div 
        className={`fixed inset-0 z-50 md:hidden transition-opacity duration-300 ease-in-out
          ${isSidebarOpen ? 'opacity-100 visible' : 'opacity-0 invisible'}`}
      >
        <div 
          className={`absolute inset-0 bg-black/50 transition-opacity duration-300 ease-in-out
            ${isSidebarOpen ? 'opacity-100' : 'opacity-0'}`}
          onClick={() => setIsSidebarOpen(false)}
        />

        <div 
          className={`absolute top-0 left-0 w-64 h-full bg-white transform transition-transform duration-300 ease-in-out
            ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'}`}
        >
          <div className="flex items-center justify-between p-4 border-b">
            <h2 className="text-lg font-semibold">Menu</h2>
            <button
              onClick={() => setIsSidebarOpen(false)}
              className="text-2xl"
            >
              ×
            </button>
          </div>

          {/* Sidebar Links */}
          <div className="py-4">
            {urls.map((link) => (
              <NavLink
                key={link.path}
                to={link.path}
                onClick={() => setIsSidebarOpen(false)}
                className={({ isActive }) => `
                  block px-4 py-2.5 w-full text-left transition-colors duration-200
                  ${isActive 
                    ? 'text-blue-600 font-semibold bg-blue-50' 
                    : 'text-gray-600 hover:bg-gray-100'}
                `}
              >
                {link.title}
              </NavLink>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Layout