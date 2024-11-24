import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "DoughDough Pizzaria",
  description: "Authentic Thai Cuisine in [Location]. Fresh, delicious Thai food made daily.",
  openGraph: {
    title: "DoughDough Pizzaria",
    description: "Authentic Thai Cuisine in [Location]",
    images: ['/og-image.jpg'],
  },
  icons: {
    icon: '/favicon.ico',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
