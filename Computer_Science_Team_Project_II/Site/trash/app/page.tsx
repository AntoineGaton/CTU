import { NavBar } from '@/components/NavBar'
import { HeroSection } from '@/components/HeroSection'
import Image from 'next/image'

export default function Home() {
  return (
    <main className="min-h-screen bg-neutral-900">
      <NavBar />
      <HeroSection />
      {/* Other sections will go here */}
    </main>
  );
}