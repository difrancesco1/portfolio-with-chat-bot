"use client";

import { FaLinkedin, FaGithub } from "react-icons/fa";
import { RiRobot2Line } from "react-icons/ri";
import { FaRegFileLines } from "react-icons/fa6";

interface AboutFooterProps {
  handleExternalLink: (a: string) => void;
}

export default function AboutFooter({ handleExternalLink }: AboutFooterProps) {
  return (
    <div className="flex gap-4 items-center">
      <div className="flex gap-3 px-1.5 py-0.5 border rounded-md items-center">
        <div className="">Resume</div>
        <FaRegFileLines size={16} />
      </div>

      <FaLinkedin
        size={24}
        onClick={() => handleExternalLink("linkedin")}
        className="cursor-pointer"
      />
      <FaGithub
        size={24}
        onClick={() => handleExternalLink("github")}
        className="cursor-pointer"
      />
      <RiRobot2Line size={24} className="ml-auto cursor-pointer" />
    </div>
  );
}
