"use client";

import React from 'react';
import { Button } from '@/components/ui/button';
import { motion } from 'framer-motion';
import AtomAnimation from './ui/atom';

const Hero = () => {
  return (
    <main className="relative flex flex-col items-center justify-center min-h-screen overflow-hidden bg-gradient-to-br from-slate-950 via-gray-900 to-black px-6">
      {/* Decorative animated blobs */}
      <AtomAnimation />
      
      <section className="relative z-10 text-center max-w-2xl py-16">
        <motion.h1
          className="text-6xl font-extrabold bg-gradient-to-r from-cyan-300 to-blue-800 bg-clip-text text-transparent mb-4"
          initial={{ y: -50, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 0.8, ease: 'easeOut' }}
        >
          Piko.ai
        </motion.h1>
        <motion.h2
          className="text-2xl font-semibold text-gray-300 mb-6"
          initial={{ y: -30, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.2 }}
        >
          Your Friendly Neighbourhood Learning Assistant
        </motion.h2>
        <motion.p
          className="text-lg text-gray-500 mb-8"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1, delay: 0.4 }}
        >
          Transform your topics into stunning, explanatory animations. Enter a topic, and instantly receive tailored explanatory video.
        </motion.p>
        <motion.div
          initial={{ scale: 0.8, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.6 }}
        >
          <Button size="lg"className='bg-slate-900' asChild>
            <a href="#steps">Get Started</a>
          </Button>
        </motion.div>
      </section>
    </main>
  );
}

export default Hero;