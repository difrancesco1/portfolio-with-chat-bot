"use client";

import ChatPrompt from "./chat-prompt";

interface BiographyItem {
  id: number;
  bulletPoint: string;
  order: number;
}

interface AboutBodyProps {
  biography: BiographyItem[];
}

export default function AboutBody({ biography }: AboutBodyProps) {
  return (
    <div className="flex flex-col gap-2 h-full">
      {biography.map((item) => (
        <span key={item.id}>{item.bulletPoint}</span>
      ))}

      <div className="font-semibold">What I do:</div>
      <ul className="list-disc list-inside">
        <li>full stack engineer</li>
        <li>founder of sapling ai</li>
        <li>solves business needs</li>
      </ul>
      <div className="font-semibold">Services:</div>
      <div className="grid w-full grid-cols-2 gap-4 text-sm">
        <div className="flex flex-col gap-1 py-2 bg-muted p-2 rounded-md">
          <span>👨‍💻 hire my team</span>
          <span>
            with experience building production ready apps, my team and i can
            build your next project.
          </span>
        </div>
        <div className="flex flex-col gap-1 py-2 bg-muted p-2 rounded-md">
          <span>👨‍💻 hire me</span>
          <span>
            with experience building production ready apps, my team and i can
            build your next project.
          </span>
        </div>
      </div>
      <ChatPrompt />
    </div>
  );
}
