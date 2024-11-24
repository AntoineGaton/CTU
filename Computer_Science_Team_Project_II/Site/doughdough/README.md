# DoughDoughs Pizza - Online Ordering Platform

A modern, responsive pizza ordering website built with Next.js 13, TypeScript, and Tailwind CSS.

## 🍕 Features

- Modern, responsive design
- Animated hero section with video background
- Featured deals showcase
- Popular pizzas gallery
- Mobile-friendly navigation
- Dark mode support
- Smooth scrolling animations

## 🛠️ Tech Stack

- **Framework**: Next.js 13
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui
- **Animations**: Framer Motion
- **Icons**: Lucide React

## 📦 Project Structure

```tree
doughdoughs-pizza/
├── app/
│   ├── layout.tsx       # Root layout
│   ├── page.tsx         # Home page
│   └── globals.css      # Global styles
├── components/
│   ├── HeroSection.tsx  # Hero video section
│   ├── NavBar.tsx       # Navigation bar
│   ├── FeaturedDeals.tsx# Deals section
│   ├── PopularPizzas.tsx# Popular pizzas section
│   └── ui/             # Reusable UI components
└── public/
    └── logo.png        # Site logo
```

## 🚀 Getting Started

```shell
git clone https://github.com/yourusername/doughdoughs-pizza.git
```

```shell
npm install
```

```shell
npm run dev
```

1. Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🎨 Design System

The project uses a custom design system with the following key colors:

```css
:root {
  --foreground-rgb: 0, 0, 0;
  --background-start-rgb: 214, 219, 220;
  --background-end-rgb: 255, 255, 255;
  --background: 60 33% 97%;  /* #fbfaf3 */
  --foreground: 0 0% 3.9%;
  --card: 60 33% 97%;
  --card-foreground: 0 0% 3.9%;
  --popover: 60 33% 97%;
  --popover-foreground: 0 0% 3.9%;
  --primary: 60 33% 97%;     /* #fbfaf3 */
  --primary-foreground: 0 0% 9%;
  --secondary: 8 75% 44%;    /* #c4391c */
  --secondary-foreground: 0 0% 98%;
  --muted: 60 33% 90%;
  --muted-foreground: 0 0% 45.1%;
  --accent: 8 75% 44%;
  --accent-foreground: 0 0% 98%;
  --destructive: 0 84.2% 60.2%;
  --destructive-foreground: 0 0% 98%;
  --border: 60 33% 85%;
  --input: 60 33% 85%;
  --ring: 8 75% 44%;
  --radius: 0.75rem;
}
```

## 📱 Responsive Design

The website is fully responsive with breakpoints for:

- Mobile: Default
- Tablet: `sm:` (640px)
- Desktop: `lg:` (1024px)

## 🔧 Configuration

Key configuration files:

- `next.config.js`: Next.js configuration
- `tailwind.config.ts`: Tailwind CSS configuration
- `tsconfig.json`: TypeScript configuration
- `components.json`: UI component configuration

## 📄 License

MIT License - feel free to use this project for your own purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🔮 Future Plans

- User authentication
- Shopping cart functionality
- Order tracking system
- Payment integration
- Admin dashboard
- Real-time order updates

---

**Note**: This is a work in progress. More features and documentation will be added as the project develops.
