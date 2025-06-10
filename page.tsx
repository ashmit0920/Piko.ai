import React from 'react';
import GradientText from '../components/ui/GradientText/GradientText';
import { Button } from '@/components/ui/button';
import shortid from "shortid";
import dynamic from 'next/dynamic';

// const GradientText = dynamic(() => import('../components/ui/GradientText/GradientText.js'), {
//   ssr: false, // This is crucial for client-side only components
// });

function getRandomKey() {
  return shortid.generate();
}

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-slate-950 px-6">
      <section className="text-center max-w-3xl">
        <h1 className="text-5xl font-bold bg-gradient-to-r from-cyan-600 via-blue-400 to-green-600 inline-block text-transparent bg-clip-text mb-4">
          Piko.ai
        </h1>
        <GradientText
          key={getRandomKey()}
          colors={["#40ffaa", "#4079ff", "#40ffaa", "#4079ff", "#40ffaa"]}
          animationSpeed={3}
          showBorder={false}
          className="text-5xl font-bold mb-4"
        >
          Add a splash of color!
        </GradientText>
        <h1 className="text-2xl font-bold text-gray-300 mb-8">
          Your friendly neighbourhood learning assistant
        </h1>
        <p className="text-xl text-gray-500 mb-8">
          Generate beautiful Manim animations using AI. Just enter a topic, and get ready-to-run Manim code instantly.
        </p>
        <Button variant="outline">
          Get Started
        </Button>
      </section>
    </main>
  );
}
