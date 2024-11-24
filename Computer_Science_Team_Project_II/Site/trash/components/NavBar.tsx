'use client';

import Link from 'next/link';
import { ShoppingCart, User } from "lucide-react";
import Image from 'next/image';

export function NavBar() {
  return (
    <nav className="fixed top-0 left-0 right-0 bg-white border-b z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Left side */}
          <div className="flex-1 flex items-center">
            <Link href="/" className="flex-shrink-0">
              <Image
                src="/logo.png"
                alt="DoughDoughs Pizza"
                width={120}
                height={40}
                priority
                className="h-8 w-auto"
              />
            </Link>
            <div className="hidden md:flex ml-10">
              <div className="flex space-x-8">
                <Link href="/deals" className="text-gray-900 hover:text-red-600">
                  Deals
                </Link>
                <Link href="/menu" className="text-gray-900 hover:text-red-600">
                  Menu
                </Link>
              </div>
            </div>
          </div>

          {/* Right side */}
          <div className="flex items-center space-x-6">
            <Link
              href="/account"
              className="flex items-center text-gray-900 hover:text-red-600"
            >
              <User className="h-5 w-5 mr-1" />
              <span className="hidden sm:inline">Sign In</span>
            </Link>
            <Link
              href="/cart"
              className="flex items-center text-gray-900 hover:text-red-600"
            >
              <ShoppingCart className="h-5 w-5 mr-1" />
              <span className="hidden sm:inline">$0.00</span>
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}