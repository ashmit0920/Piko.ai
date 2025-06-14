import React from 'react';
import Hero from '@/components/Hero';
import Steps from '@/components/Steps';
import Create from '@/components/Create';

const Page = () => {
  return (
    <div className="min-h-screen bg-background">
      <Hero />
      <Steps />
      <Create />
    </div>
  );
};

export default Page;