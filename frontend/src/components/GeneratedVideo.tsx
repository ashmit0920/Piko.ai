"use client";

import { useEffect, useState } from "react";

type Props = {
    topic: string;
    resolution?: string;
};

export default function GeneratedVideo({ topic, resolution = "1080p60" }: Props) {
    const [videoFile, setVideoFile] = useState<string | null>(null);

    useEffect(() => {
        let intervalId: NodeJS.Timeout;

        const pollForVideo = async () => {
            try {
                const res = await fetch(`http://localhost:8000/videos/${encodeURIComponent(topic)}/${resolution}/file`);
                if (res.ok) {
                    const data = await res.json();
                    setVideoFile(data.filename);

                    // ✅ Stop polling once video is found
                    clearInterval(intervalId);
                }
            } catch (error) {
                // Do nothing (server still compiling)
            }
        };

        // Start polling every 5 seconds
        intervalId = setInterval(pollForVideo, 5000);
        pollForVideo(); // Also check immediately once

        // Cleanup interval on unmount or topic/resolution change
        return () => clearInterval(intervalId);
    }, [topic, resolution]);


    if (videoFile === null) return <p className="text-gray-400">Loading video…</p>;

    return (
        <video
            className="rounded-md w-full border border-slate-600"
            controls
            preload="metadata"
        >
            <source
                src={`http://localhost:8000/videos/${encodeURIComponent(topic)}/${resolution}/${videoFile}`}
                type="video/mp4"
            />
            Your browser does not support the video tag.
        </video>
    );
}
