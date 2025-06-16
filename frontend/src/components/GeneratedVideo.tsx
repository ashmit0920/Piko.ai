"use client";

import { useEffect, useState } from "react";

type Props = {
    topic: string;
    resolution?: string;
};

export default function GeneratedVideo({ topic, resolution = "1080p60" }: Props) {
    const [videoFile, setVideoFile] = useState<string | null>(null);

    useEffect(() => {
        fetch(`http://localhost:8000/videos/${encodeURIComponent(topic)}/${resolution}/file`)
            .then((res) => res.json())
            .then((data) => setVideoFile(data.filename))
            .catch(() => setVideoFile(null));
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
