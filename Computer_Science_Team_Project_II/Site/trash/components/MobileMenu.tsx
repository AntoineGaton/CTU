import { Menu } from "lucide-react";
import { useState } from "react";

export function MobileMenu() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="md:hidden">
      <button 
        onClick={() => setIsOpen(!isOpen)} 
        className="text-white p-2"
      >
        <Menu size={24} />
      </button>

      {isOpen && (
        <div className="absolute top-20 left-0 right-0 bg-black/95 backdrop-blur-sm p-4">
          <div className="flex flex-col space-y-4">
            <a href="#" className="text-white hover:text-yellow-400 transition-colors">Home</a>
            <a href="#" className="text-white hover:text-yellow-400 transition-colors">Menu</a>
            <a href="#" className="text-white hover:text-yellow-400 transition-colors">About</a>
            <a href="#" className="text-white hover:text-yellow-400 transition-colors">Contact</a>
            <button className="bg-red-600 text-white px-6 py-2 rounded-full hover:bg-red-700 transition-colors">
              Order Now
            </button>
          </div>
        </div>
      )}
    </div>
  );
} 