"use client";

import { FaGithub } from "react-icons/fa";
import { RiRobot2Line } from "react-icons/ri";
import { TabsList, TabsTrigger } from "@/components/ui/tabs";

export default function ContentTabs() {
  return (
    <TabsList className="w-fit">
      <TabsTrigger value="chatbot" className="gap-1.5">
        <RiRobot2Line size={16} />
        Chat Bot
      </TabsTrigger>
      <TabsTrigger value="github" className="gap-1.5">
        <FaGithub size={16} />
        GitHub
      </TabsTrigger>
    </TabsList>
  );
}
