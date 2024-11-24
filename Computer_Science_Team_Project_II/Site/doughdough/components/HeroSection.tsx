"use client";

import { MapPin, ChevronDown } from "lucide-react";
import { motion } from "framer-motion";

export function HeroSection() {
  const heroVideo = "/hero-video.mp4";

  const scrollToNext = () => {
    const nextSection = document.getElementById('featured-section');
    nextSection?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <div className="relative w-screen h-[calc(100vh-80px)]">
      <div className="absolute inset-0 bg-black/40" />
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute w-screen h-full object-cover"
      >
        <source src={heroVideo} type="video/mp4" />
      </video>

      {/* Bouncing Chevron */}
      <div 
        className="flex flex-col items-center absolute bottom-3 left-1/2 -translate-x-1/2 text-center cursor-pointer drop-shadow-lg"
        onClick={scrollToNext}
      >
        <motion.div
          animate={{
            y: [0, 10, 0],
            opacity: [0.5, 1, 0.5],
            color: ['#000000', '#fafaf5', '#c4321c']
          }}
          transition={{
            duration: 1.5,
            repeat: Infinity,
            ease: "easeInOut",
          }}
        >
          <ChevronDown className="h-10 w-10" />
        </motion.div>
      </div>
    </div>
  );
}