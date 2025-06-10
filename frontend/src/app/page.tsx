import React from 'react';
import Link from 'next/link';

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-slate-950 px-6">
      <section className="text-center max-w-3xl">
        <h1 className="text-5xl font-bold bg-gradient-to-r from-cyan-600 via-blue-400 to-green-600 inline-block text-transparent bg-clip-text mb-4">
          Piko.ai
        </h1>
        <h1 className="text-2xl font-bold text-gray-300 mb-8">
          Your friendly neighbourhood learning assistant
        </h1>
        <p className="text-xl text-gray-500 mb-8">
          Generate beautiful Manim animations using AI. Just enter a topic, and get ready-to-run Manim code instantly.
        </p>
        <Link href="/app">
          {/* <a className="inline-block px-6 py-3 text-white bg-blue-600 hover:bg-blue-700 rounded-xl text-lg shadow-md transition">
            Get Started
          </a> */}
        </Link>
      </section>
    </main>
  );
}
