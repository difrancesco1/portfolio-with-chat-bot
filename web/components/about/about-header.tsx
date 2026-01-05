"use client";

import Image from "next/image";
import pfp from "@/public/profile.png";
interface AboutHeaderProps {
  title: string;
}

export default function AboutHeader({ title }: AboutHeaderProps) {
  return (
    <>
      <div className="flex gap-4">
        {" "}
        <Image
          src={pfp}
          width={65}
          height={65}
          className="rounded-full"
          alt="Profile Picture"
        />
        <div className="flex flex-col gap-0.5">
          <h1 className="text-3xl">{title}</h1>
          <div className="flex gap-2 text-sm">
            <span className="bg-accent p-0.5 px-1 rounded-md font-semibold">
              open to work
            </span>
            <span className="bg-accent p-0.5 px-1 rounded-md font-semibold">
              fullstack
            </span>
          </div>
        </div>
      </div>
    </>
  );
}
