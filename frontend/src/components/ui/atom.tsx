import Lottie from "lottie-react";
import atom from "@/assets/atom.json"

const AtomAnimation = () => {
  return (
    <div className="absolute top-0 left-0 w-full h-full z-0 opacity-20">
      <Lottie animationData={atom} loop={true} />
    </div>
  );
};

export default AtomAnimation;
