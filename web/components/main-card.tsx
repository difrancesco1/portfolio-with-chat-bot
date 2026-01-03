"use client";
import { useState } from "react";
import Topbar from "./topbar";
import Tabs from "./tabs";
import AboutSection from "./about/about-section";
import ExperienceSection from "./experience/experience-section";
import ProjectSection from "./projects/projects-section";
const tabs = ["about", "experience", "projects", "education", "contact"];

export default function MainCard() {
  const [open, setOpen] = useState(false);
  const [activeTab, setActiveTab] = useState(tabs[0]);

  const toggleOpen = () => {
    setOpen((prev) => {
      return !prev;
    });
  };

  const handleTabChange = (tab: string) => {
    setActiveTab(tab);
  };

  const handleExternalLink = (website: string) => {
    if (website === "github") {
      window.open("https://github.com/difrancesco1");
    } else {
      window.open("https://www.linkedin.com/in/joshua-difrancesco-a28265183/");
    }
  };

  return (
    <div
      className={`max-w-[34rem] overflow-y-auto ${
        open ? "main-card-open" : "main-card-collapsed"
      }`}
    >
      <div className="flex flex-col w-full gap-4">
        <Topbar toggleOpen={toggleOpen} open={open} />
        {open && (
          <>
            <Tabs
              tabs={tabs}
              activeTab={activeTab}
              handleTabChange={handleTabChange}
            />
            {activeTab === "about" && (
              <AboutSection handleExternalLink={handleExternalLink} />
            )}
            {activeTab === "experience" && <ExperienceSection />}
            {activeTab === "projects" && <ProjectSection />}
          </>
        )}
      </div>
    </div>
  );
}
