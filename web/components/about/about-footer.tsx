"use client";

import { FaLinkedin, FaGithub } from "react-icons/fa";
import { RiRobot2Line } from "react-icons/ri";
import { FaRegFileLines } from "react-icons/fa6";
import { IoLocationOutline } from "react-icons/io5";
import { MdOutlineMailOutline, MdLocalPhone } from "react-icons/md";

interface AboutFooterProps {
  handleExternalLink: (a: string) => void;
  activeTab: string;
}

export default function AboutFooter({
  handleExternalLink,
  activeTab,
}: AboutFooterProps) {
  return (
    <div className="flex gap-2 items-center">
      {activeTab === "about" && (
        <>
          <div className="flex gap-3 px-1.5 py-0.5 border rounded-md items-center">
            <div className="">Resume</div>
            <FaRegFileLines size={16} />
          </div>

          <FaLinkedin
            size={20}
            onClick={() => handleExternalLink("linkedin")}
            className="cursor-pointer"
          />
          <FaGithub
            size={20}
            onClick={() => handleExternalLink("github")}
            className="cursor-pointer"
          />
        </>
      )}
      {activeTab === "contact" && (
        <div className="flex text-sm items-center gap-3">
          <div className="flex gap-1 border border-secondary rounded-md p-1 px-1.5">
            <IoLocationOutline size={20} className="cursor-pointer" />
            <span>Seattle, WA</span>
          </div>
          <div className="flex gap-1 border border-secondary rounded-md p-1 px-1.5">
            <MdLocalPhone size={20} className="cursor-pointer" />
            <span>(727)-437-8706</span>
          </div>

          <div className="flex gap-1 border border-secondary rounded-md p-1 px-1.5">
            <MdOutlineMailOutline size={20} className="cursor-pointer" />
            <span>difrancesco.joshua1@gmail.com</span>
          </div>
        </div>
      )}
      <RiRobot2Line size={20} className="ml-auto cursor-pointer" />
    </div>
  );
}
