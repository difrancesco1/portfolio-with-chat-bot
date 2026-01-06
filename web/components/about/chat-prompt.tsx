"use client";

import { Input } from "../ui/input";
import Typewriter from "typewriter-effect";
import { RiRobot2Line } from "react-icons/ri";

export default function ChatPrompt() {
  return (
    <div className="w-full h-full border border-secondary rounded-sm px-2 py-1 flex flex-col justify-center bg-background">
      <div className="flex items-center gap-2">
        <RiRobot2Line size={20} className="cursor-pointer flex-shrink-0" />
        <div className="text-sm text-muted-foreground text-left">
          <Typewriter
            options={{
              strings: ["Send a message to start the chat!"],
              autoStart: true,
              loop: false,
              cursor: "",
              delay: 50,
              deleteSpeed: Infinity,
            }}
          />
        </div>
      </div>

      <div className="flex flex-col gap-4 flex-1 justify-center items-center w-full"></div>

      <div className="mt-4 p-2 flex flex-col gap-1">
        <div className="flex text-xs gap-1">
          <div className="bg-background/50 hover:bg-background/80 transition-colors p-1 rounded-md cursor-pointer border border-border/50 px-2">
            What is Sapling AI?
          </div>
          <div className="bg-background/50 hover:bg-background/80 transition-colors p-1 rounded-md cursor-pointer border border-border/50 px-2">
            Is Josh really 6'5?
          </div>
        </div>
        <Input className="w-full" placeholder="Ask something..." />
      </div>
    </div>
  );
}
