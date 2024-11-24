import { MapPin } from "lucide-react";

export function HeroSection() {
  return (
    <div className="relative w-full h-[800px] overflow-hidden">
      <video 
        autoPlay 
        loop 
        muted 
        playsInline
        className="absolute top-0 left-0 w-full h-full object-cover"
      >
        <source src="/hero-video.mp4" type="video/mp4" />
      </video>
      
      {/* Content container */}
      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col items-center justify-center h-full text-white">
        <h1 className="text-5xl md:text-7xl font-bold text-center mb-4 animate-fade-in-down drop-shadow-2xl">
          Authentic Thai Flavors
          <span className="block text-3xl md:text-4xl mt-2 text-yellow-400">
            Made Fresh Daily
          </span>
        </h1>
        
        <div className="flex flex-col sm:flex-row gap-4 mt-8 animate-fade-in-up">
          <button className="px-8 py-3 bg-red-600 hover:bg-red-700 rounded-full text-lg font-semibold transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl">
            Order Now
          </button>
          <button className="px-8 py-3 bg-transparent border-2 border-white hover:bg-white hover:text-red-600 rounded-full text-lg font-semibold transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl">
            View Menu
          </button>
        </div>
      </div>
    </div>
  );
}