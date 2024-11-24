"use client";

import Image from "next/image";
import Link from "next/link";
import { ArrowRight } from "lucide-react";

const pizzas = [
  {
    id: 1,
    name: "Supreme",
    description: "Pepperoni, Italian sausage, mushrooms, onions, green peppers",
    image: "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=800&auto=format&fit=crop&q=60",
    price: "18.99"
  },
  {
    id: 2,
    name: "Margherita",
    description: "Fresh mozzarella, tomatoes, basil on our signature sauce",
    image: "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=800&auto=format&fit=crop&q=60",
    price: "16.99"
  },
  {
    id: 3,
    name: "BBQ Chicken",
    description: "Grilled chicken, bacon, onions with sweet BBQ sauce",
    image: "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800&auto=format&fit=crop&q=60",
    price: "17.99"
  },
  {
    id: 4,
    name: "Meat Lovers",
    description: "Pepperoni, sausage, ham, bacon, seasoned pork, beef",
    image: "https://images.unsplash.com/photo-1571407970349-bc81e7e96d47?w=800&auto=format&fit=crop&q=60",
    price: "19.99"
  }
];

export function PopularPizzas() {
  return (
    <section className="py-12">
      <div className="border-t-2 border-b-2 border-red-600 py-8 my-8">
        <div className="flex justify-between items-center mb-8">
          <h2 className="text-4xl font-bold text-gray-900">Popular Pizzas</h2>
          <Link 
            href="/menu" 
            className="text-red-600 hover:text-red-700 font-semibold flex items-center"
          >
            PIZZA MENU <ArrowRight className="ml-1 h-4 w-4" />
          </Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {pizzas.map((pizza) => (
            <Link
              key={pizza.id}
              href={`/menu/pizzas/${pizza.id}`}
              className="group bg-white rounded-lg shadow-md overflow-hidden hover-scale"
            >
              <div className="relative h-48 w-full">
                <Image
                  src={pizza.image}
                  alt={pizza.name}
                  fill
                  className="object-cover"
                />
                <div className="absolute top-4 right-4 bg-white text-red-600 px-3 py-1 rounded-full font-bold">
                  ${pizza.price}
                </div>
              </div>
              <div className="p-4">
                <h3 className="text-xl font-bold text-gray-900 mb-2">{pizza.name}</h3>
                <p className="text-gray-600 text-sm">{pizza.description}</p>
                <div className="mt-4 flex items-center text-red-600 font-semibold">
                  Order Now <ArrowRight className="ml-2 h-4 w-4 group-hover:translate-x-1 transition-transform" />
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}