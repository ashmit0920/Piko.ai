"use client";

import React from 'react';
import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { motion } from 'framer-motion';
import { Textarea } from '@/components/ui/textarea';

const Create = () => {
  const [topic, setTopic] = useState("");
  const [loading, setLoading] = useState(false);
  const [explanation, setExplanation] = useState("");

  const handleCreate = async () => {
    if (!topic.trim()) return;

    setLoading(true);

    try {
      const response = await fetch(`http://localhost:8000/code/${encodeURIComponent(topic)}`);
      const data = await response.json(); // adjust if your backend returns plain text
      console.log("Generated Code:", data);
      setExplanation(data.explanation)
    } catch (error) {
      console.error("API call failed:", error);
      setExplanation("Oops! An error occured while generating explanation.")
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="relative flex flex-col items-center justify-center min-h-screen overflow-hidden bg-gradient-to-br from-slate-950 via-gray-900 to-black px-6">
        <section id='create' className="relative z-10 flex flex-col items-center justify-center px-4">
        {/* Top Info Paragraph */}
        <motion.p
            className="text-lg text-gray-500 mb-8 text-center max-w-xl"
            initial={{ y: 0, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 1.2, ease: "easeOut" }}
        >
            Transform your topics into stunning, explanatory animations. Enter a topic, and instantly receive tailored explanatory video.
        </motion.p>

        {/* Input Box + Button */}
        <motion.div
            initial={{ y: 0, opacity: 0 }}
            animate={{
            y: 0,
            opacity: 1,
            scale: 1,
            }}
            transition={{ duration: 1.2, ease: "easeInOut" }}
            className="w-full max-w-xl text-center"
        >
            <Textarea
            placeholder='Enter any topic...'
            className='border-slate-700 text-white'
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            />
            <Button
            size="lg"
            className='bg-slate-900 mt-5'
            onClick={handleCreate}
            disabled={loading}
            >
            {loading ? "Creating..." : "Create"}
            </Button>
        </motion.div>

        {/* Generated Explanation */}
        {explanation && (
            <motion.div
            initial={{ opacity: 0, y: 50, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            transition={{ duration: 1, delay: 0.5 }}
            className="mt-10 max-w-2xl px-6"
            >
            <div className="p-6 rounded-md text-white border border-slate-700 bg-slate-900 shadow-lg">
                <h3 className="text-xl font-semibold mb-3 text-sky-300">Explanation:</h3>
                <p className="text-slate-300 whitespace-pre-line text-justify leading-relaxed">
                {explanation}
                </p>
            </div>
            </motion.div>
        )}
        </section>
    </main>
  );
}

export default Create;