"use client";

import React from 'react';
import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { motion } from 'framer-motion';
import { Textarea } from '@/components/ui/textarea';
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
  const [topic, setTopic] = useState("");
  const [loading, setLoading] = useState(false);

  const handleCreate = async () => {
    if (!topic.trim()) return;

    setLoading(true);

    try {
      const response = await fetch(`http://localhost:8000/code/${encodeURIComponent(topic)}`);
      const data = await response.json(); // adjust if your backend returns plain text
      console.log("Generated Code:", data);
      // Handle display, saving, or scrolling here
    } catch (error) {
      console.error("API call failed:", error);
    } finally {
      setLoading(false);
    }
  };

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
          <Card className="bg-slate-900 text-white border-slate-700 shadow-lg w-xs mx-2">
            <CardHeader>
              <CardTitle>One Click is all you need</CardTitle>
              <CardDescription>~ Dua Lipa (probably)</CardDescription>
            </CardHeader>
            <CardContent>
              <p>Just enter the topic you want to learn and hit "Create".</p>
            </CardContent>
          </Card>

          <Card className="bg-slate-900 text-white border-slate-700 shadow-lg w-xs mx-2">
            <CardHeader>
              <CardTitle>Give Piko a few minutes</CardTitle>
              <CardDescription>Let it do its magic</CardDescription>
            </CardHeader>
            <CardContent>
              <p>Piko will write code to generate and compile an animation just for you.</p>
            </CardContent>
          </Card>

          <Card className="bg-slate-900 text-white border-slate-700 shadow-lg w-xs mx-2">
            <CardHeader>
              <CardTitle>Voila! All done</CardTitle>
              <CardDescription>Ready Study Go</CardDescription>
            </CardHeader>
            <CardContent>
              <p>Within 2-3 minutes, you would have an explanatory video ready!</p>
            </CardContent>
          </Card>
        </div>
        </motion.div>

        <Textarea 
          placeholder='Enter any topic...' 
          className='border-slate-700 mt-15 text-white' 
          value={topic} 
          onChange={(e) => setTopic(e.target.value)}
        />
        <Button size="lg" className='bg-slate-900 mt-5' onClick={handleCreate} disabled={loading}>
            {loading ? "Creating..." : "Create"}
        </Button>

      </section>
    </main>
  );
}

export default Steps;