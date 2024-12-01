import React, { useState } from 'react';
import { Calendar, X, ChevronLeft, ChevronRight } from 'lucide-react';
import { format, addMonths, subMonths, startOfMonth, endOfMonth, eachDayOfInterval, isSameMonth, isSameDay, startOfWeek, endOfWeek, isAfter, startOfDay } from 'date-fns';

const DatePicker = ({ onSelectDate, selectedDate }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [currentMonth, setCurrentMonth] = useState(new Date());

  const onDateSelect = (date) => {
    const formattedDate = format(date, 'yyyy-MM-dd');
    onSelectDate(formattedDate);
    setIsOpen(false);
  };

  const renderCalendar = () => {
    const monthStart = startOfMonth(currentMonth);
    const monthEnd = endOfMonth(currentMonth);
    const calendarStart = startOfWeek(monthStart);
    const calendarEnd = endOfWeek(monthEnd);
    
    const allDays = eachDayOfInterval({ 
      start: calendarStart, 
      end: calendarEnd 
    });

    const dayOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

    // Bugünün tarihini al
    const today = startOfDay(new Date());
    
    return (
      <>
        <div className="flex items-center justify-between mb-4 px-2">
          <button
            onClick={() => setCurrentMonth(prev => subMonths(prev, 1))}
            className="p-1 hover:bg-gray-100 rounded-full transition-colors"
            type="button"
          >
            <ChevronLeft className="w-5 h-5 text-gray-600" />
          </button>
          
          <h3 className="font-semibold text-gray-800">
            {format(currentMonth, 'MMMM yyyy')}
          </h3>
          
          <button
            onClick={() => setCurrentMonth(prev => addMonths(prev, 1))}
            className="p-1 hover:bg-gray-100 rounded-full transition-colors"
            type="button"
          >
            <ChevronRight className="w-5 h-5 text-gray-600" />
          </button>
        </div>

        <div className="grid grid-cols-7 mb-2">
          {dayOfWeek.map(day => (
            <div 
              key={day} 
              className="text-xs font-medium text-gray-500 text-center py-2"
            >
              {day}
            </div>
          ))}
        </div>

        <div className="grid grid-cols-7 gap-1">
          {allDays.map(day => {
            const isCurrentMonth = isSameMonth(day, currentMonth);
            const isToday = isSameDay(day, today);
            const isSelected = isSameDay(day, new Date(selectedDate));
            const isFutureDate = isAfter(day, today);

            return (
              <button
                key={day.toString()}
                onClick={() => !isFutureDate && onDateSelect(day)}
                type="button"
                disabled={isFutureDate}
                className={`
                  relative p-2 text-sm rounded-lg transition-all
                  ${!isCurrentMonth ? 'text-gray-400' : 'text-gray-700'}
                  ${isFutureDate ? 'opacity-50 cursor-not-allowed bg-gray-100' : 'hover:bg-blue-50 hover:text-blue-600'}
                  ${isToday ? 'after:absolute after:bottom-1 after:left-1/2 after:-translate-x-1/2 after:w-1 after:h-1 after:bg-blue-500 after:rounded-full' : ''}
                  ${isSelected ? 'bg-blue-100 text-blue-700 ring-2 ring-blue-400' : ''}
                  ${isCurrentMonth && !isFutureDate && 'hover:scale-110 transform duration-100'}
                `}
              >
                <span>{format(day, 'd')}</span>
              </button>
            );
          })}
        </div>
      </>
    );
  };

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="p-2 rounded-full hover:bg-gray-100 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
        aria-label="Select date"
        type="button"
      >
        <Calendar className="w-5 h-5 text-gray-600" />
      </button>

      {isOpen && (
        <>
          <div 
            className="fixed inset-0 z-40"
            onClick={() => setIsOpen(false)}
          />
          
          <div className="absolute top-full mt-2 right-0 z-50">
            <div className="bg-white rounded-lg shadow-xl border border-gray-200 w-80">
              <div className="flex items-center justify-between p-3 border-b">
                <h3 className="font-semibold text-gray-700">Select Date</h3>
                <button 
                  onClick={() => setIsOpen(false)}
                  className="p-1 hover:bg-gray-100 rounded-full"
                  type="button"
                >
                  <X className="w-4 h-4 text-gray-500" />
                </button>
              </div>

              <div className="p-3">
                {renderCalendar()}
              </div>

              <div className="p-3 bg-gray-50 rounded-b-lg border-t text-xs text-center text-gray-500">
                Future dates are disabled
              </div>
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default DatePicker;