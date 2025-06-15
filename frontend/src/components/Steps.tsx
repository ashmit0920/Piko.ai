"use client";

import React from 'react';
import { Button } from '@/components/ui/button';
import { motion } from 'framer-motion';
import SpotlightCard from './ui/SpotlightCard/SpotlightCard';
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

const Steps = () => {
  return (
    <main className="relative flex flex-col items-center justify-center min-h-screen overflow-hidden bg-gradient-to-br from-slate-950 via-gray-900 to-black px-6">
      <section id='steps' className="relative z-10 text-center max-w-2xl py-16">
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
        <div className="flex justify-center items-center min-h-xl min-w-xl">
          <SpotlightCard className='text-white bg-slate-900 border-slate-700 shadow-lg w-lg h-lg mx-2' spotlightColor="rgba(255, 255, 255, 0.25)">
            <p className='font-bold'>One click is all you need</p>
            <p className='text-neutral-500 text-sm mb-5'>~ Dua Lipa (probably)</p>
            <p>Just enter the topic you want to learn and hit "Create".</p>
          </SpotlightCard>
          
          <SpotlightCard className='text-white bg-slate-900 border-slate-700 shadow-lg w-lg h-lg mx-2' spotlightColor="rgba(255, 255, 255, 0.25)">
            <p className='font-bold'>Give Piko a few minutes</p>
            <p className='text-neutral-500 text-sm mb-5'>To do its magic</p>
            <p>Piko will write code to generate an animation just for you.</p>
          </SpotlightCard>
          
          <SpotlightCard className='text-white bg-slate-900 border-slate-700 shadow-lg w-lg h-lg mx-2' spotlightColor="rgba(255, 255, 255, 0.25)">
            <p className='font-bold'>Voila! All done</p>
            <p className='text-neutral-500 text-sm mb-5'>Ready Study Go</p>
            <p>Within 2-3 minutes, you would have an explanatory video ready!</p>
          </SpotlightCard>
        </div>
        </motion.div>

        <motion.div
          initial={{ scale: 0.8, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.6 }}
        >
          <Button size="lg" className='bg-slate-900 mt-8' asChild>
              <a href="#create">Ask Piko</a>
          </Button>
        </motion.div>
      </section>
    </main>
  );
}

export default Steps;