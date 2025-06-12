import Lottie from "lottie-react";
import atom from "@/assets/atom.json"

const AtomAnimation = () => {
  return (
    <div className="absolute top-3 left-50% w-3xs h-3xs z-0 opacity-70">
      <Lottie animationData={atom} loop={true} />
    </div>
  );
};

export default AtomAnimation;
