"use client";

import Link from "next/link";
import { Menu as MenuIcon, X } from "lucide-react";
import Image from "next/image";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

export function NavBar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const menuItems = [
    { href: "/deals", label: "Deals" },
    { href: "/menu", label: "Menu" },
    { href: "/track", label: "Track Order" },
  ];

  const menuVariants = {
    closed: {
      opacity: 0,
    },
    open: {
      opacity: 1,
      transition: {
        duration: 0.8,
        staggerChildren: 0.3,
      },
    },
    exit: {
      opacity: 0,
      transition: {
        duration: 0.5,
      },
    },
  };

  const itemVariants = {
    closed: {
      opacity: 0,
      y: 50,
    },
    open: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.8,
        ease: [0.6, 0.05, -0.01, 0.9],
      },
    },
    exit: {
      opacity: 0,
      y: 30,
      transition: {
        duration: 0.5,
      },
    },
  };

  return (
    <nav className="sticky top-0 z-50 bg-primary">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-20">
          {/* Left - Menu Button */}
          <div className="w-[100px]">
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="bg-primary h-20 px-6 -ml-4 sm:-ml-6 lg:-ml-8 text-secondary hover:text-black flex items-center"
            >
              {isMenuOpen ? (
                <X className="h-8 w-8" />
              ) : (
                <MenuIcon className="h-8 w-8" />
              )}
            </button>
          </div>

          {/* Center - Logo */}
          <div className="flex-shrink-0">
            <Link href="/">
              <Image
                src="/logo.png"
                alt="DoughDoughs Pizza"
                width={150}
                height={50}
                className="h-28 w-auto"
              />
            </Link>
          </div>

          {/* Right - Order Button */}
          <div className="w-[100px] flex justify-end">
            <Link
              href="/order"
              className="text-secondary border-2 border-secondary px-6 py-2 hover:bg-secondary hover:text-primary transition-colors"
            >
              ORDER
            </Link>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isMenuOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="absolute top-20 left-0 w-full bg-black/95 shadow-lg"
          >
            <div className="px-4 py-2 flex flex-col items-center">
              {menuItems.map((item, index) => (
                <motion.div
                  key={item.href}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: 20 }}
                  className="block py-4 text-white hover:text-secondary text-lg"
                  onClick={() => setIsMenuOpen(false)}
                >
                  {item.label}
                </motion.div>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
}