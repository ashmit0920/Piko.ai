"use client";

import React from 'react';
import { Button } from '@/components/ui/button';
import { motion } from 'framer-motion';
import dynamic from 'next/dynamic';
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

// Example dynamic import for a decorative background animation (e.g., Lottie)
// const BackgroundAnimation = dynamic(
//   () => import('@/components/animations/BlobAnimation'),
//   { ssr: false }
// );

const Steps = () => {
  return (
    <main className="relative flex flex-col items-center justify-center min-h-screen overflow-hidden bg-gradient-to-br from-slate-950 via-gray-900 to-black px-6">
      {/* Decorative animated blobs */}
      {/* <BackgroundAnimation /> */}

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
        
        <div className="flex justify-center items-center min-h-xl min-w-xl">
          <Card className="bg-slate-900 text-white border-slate-700 shadow-lg max-w-xs mx-2">
            <CardHeader>
              <CardTitle>One Click is all you need</CardTitle>
              <CardDescription>~ Dua Lipa (probably)</CardDescription>
            </CardHeader>
            <CardContent>
              <p>Just enter the topic you want to learn and hit "Create".</p>
            </CardContent>
          </Card>

          <Card className="bg-slate-900 text-white border-slate-700 shadow-lg max-w-xs mx-2">
            <CardHeader>
              <CardTitle>One Click is all you need</CardTitle>
              <CardDescription>~ Dua Lipa (probably)</CardDescription>
            </CardHeader>
            <CardContent>
              <p>Just enter the topic you want to learn and hit "Create".</p>
            </CardContent>
          </Card>

          <Card className="bg-slate-900 text-white border-slate-700 shadow-lg max-w-xs mx-2">
            <CardHeader>
              <CardTitle>One Click is all you need</CardTitle>
              <CardDescription>~ Dua Lipa (probably)</CardDescription>
            </CardHeader>
            <CardContent>
              <p>Just enter the topic you want to learn and hit "Create".</p>
            </CardContent>
          </Card>
        </div>

      </section>
    </main>
  );
}

export default Steps;