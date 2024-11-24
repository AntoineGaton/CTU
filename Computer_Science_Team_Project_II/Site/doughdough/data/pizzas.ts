import { getPizzaImage } from '@/utils/images';

let initializedPizzas: Pizza[] | null = null;

export async function initializePizzas() {
  if (initializedPizzas) return initializedPizzas;
  
  const pizzaData = [...pizzas];
  await Promise.all(
    pizzaData.map(async (pizza) => {
      pizza.image = await getPizzaImage(pizza.name.toLowerCase());
    })
  );
  
  initializedPizzas = pizzaData;
  return pizzaData;
}

export type Pizza = {
  id: number;
  name: string;
  description: string;
  image: string | Promise<string>;
  price: string;
  ingredients: string[];
  isCustom?: boolean;
  isPopular?: boolean;
};

export const pizzas: Pizza[] = [
   {
      id: 0,
      name: "Cheese Pizza",
      description: "A classic cheese pizza with a thin crust",
      image: getPizzaImage("cheese pizza"),
      price: "10.99",
      ingredients: [],
      isCustom: true,
      isPopular: true
   },
   {
    id: 1,
    name: "Supreme",
    description: "Pepperoni, Italian sausage, mushrooms, onions, green peppers",
    image: getPizzaImage("supreme pizza"),
    price: "18.99",
    ingredients: ['pepperoni', 'italian-sausage', 'mushrooms', 'onions', 'green-peppers'],
    isPopular: true
  },
  {
    id: 2,
    name: "Margherita",
    description: "Fresh mozzarella, tomatoes, basil on our signature sauce",
    image: getPizzaImage("margherita pizza"),
    price: "16.99",
    ingredients: ['mozzarella', 'tomatoes', 'basil', 'tomato-sauce'],
    isPopular: true
  },
  {
    id: 3,
    name: "BBQ Chicken",
    description: "Grilled chicken, bacon, onions with sweet BBQ sauce",
    image: getPizzaImage("bbq chicken pizza"),
    price: "17.99",
    ingredients: ['chicken', 'bacon', 'onions', 'bbq-sauce'],
    isPopular: false
  },
  {
    id: 4,
    name: "Meat Lovers",
    description: "Pepperoni, sausage, ham, bacon, seasoned pork, beef",
    image: getPizzaImage("meat lovers pizza"),
    price: "19.99",
    ingredients: ['pepperoni', 'italian-sausage', 'ham', 'bacon', 'pork', 'beef'],
    isPopular: true
  },
  {
    id: 5,
    name: "Hawaiian",
    description: "Ham, pineapple, extra mozzarella on our signature sauce",
    image: getPizzaImage("hawaiian pizza"),
    price: "17.99",
    ingredients: ['ham', 'pineapple', 'mozzarella', 'tomato-sauce'],
    isPopular: false
  },
  {
    id: 6,
    name: "Veggie Delight",
    description: "Mushrooms, onions, peppers, olives, tomatoes, spinach",
    image: getPizzaImage("veggie delight pizza"),
    price: "16.99",
    ingredients: ['mushrooms', 'onions', 'green-peppers', 'olives', 'tomatoes', 'spinach'],
    isPopular: false
  },
  {
    id: 7,
    name: "Buffalo Chicken",
    description: "Spicy buffalo chicken, ranch, mozzarella, red onions",
    image: getPizzaImage("buffalo chicken pizza"),
    price: "18.99",
    ingredients: ['buffalo-chicken', 'ranch-sauce', 'mozzarella', 'red-onions'],
    isPopular: false
  },
  {
    id: 8,
    name: "Pepperoni Perfection",
    description: "Double pepperoni, extra cheese, Italian seasoning",
    image: getPizzaImage("pepperoni perfection pizza"),
    price: "17.99",
    ingredients: ['pepperoni', 'pepperoni', 'mozzarella', 'italian-seasoning'],
    isPopular: true
  },
  {
    id: 9,
    name: "Mediterranean",
    description: "Feta, olives, sun-dried tomatoes, spinach, garlic",
    image: getPizzaImage("mediterranean pizza"),
    price: "18.99",
    ingredients: ['feta', 'olives', 'sun-dried-tomatoes', 'spinach', 'garlic'],
    isPopular: false
  },
  {
    id: 10,
    name: "Create Your Own",
    description: "Choose your toppings and create your perfect pizza. Starting at $10.99",
    image: getPizzaImage("create your own pizza"),
    price: "10.99",
    ingredients: ['thick-crust'],
    isCustom: true,
    isPopular: true
  }
]; 