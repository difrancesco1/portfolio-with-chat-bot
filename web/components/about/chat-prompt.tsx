"use client";

import { Input } from "../ui/input";
import { MessageCircle } from "lucide-react";

export default function ChatPrompt() {
  return (
    <div className="w-full h-full relative flex-1 bg-muted min-h-0 rounded-lg px-2 py-1 flex flex-col text-center">
      <div className="flex items-center gap-2 justify-center">
        <MessageCircle className="w-5 h-5 text-primary" />
      </div>

      <div className="flex flex-col gap-1 flex-1">
        <div className="text-sm text-muted-foreground">
          Send a message to start the chat! You can ask the bot anything about
          me and it will give you the information.
        </div>

        <div className="flex flex-col gap-2">
          <div className="flex flex-col gap-2 text-sm">
            <div className="bg-background/50 hover:bg-background/80 transition-colors p-1 rounded-md cursor-pointer border border-border/50">
              💼 What is Sapling AI?
            </div>
            <div className="bg-background/50 hover:bg-background/80 transition-colors p-1 rounded-md cursor-pointer border border-border/50">
              🔗 Insert the link to a job to see if Josh is a good fit (and why)
            </div>
            <div className="bg-background/50 hover:bg-background/80 transition-colors p-1 rounded-md cursor-pointer border border-border/50">
              📏 Is Josh really 6'5?
            </div>
          </div>
        </div>
      </div>

      <div className="mt-4">
        <Input className="w-full" placeholder="Ask something..." />
      </div>
    </div>
  );
}
