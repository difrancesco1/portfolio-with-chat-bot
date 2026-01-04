"use client";

import ExperienceJobCard from "./experience-job-card";
import ExperienceEducationCard from "./experience-education-card";

interface ExperienceSectionProps {
  activeTab: string;
}

export default function ExperienceSection({activeTab}:ExperienceSectionProps) {
  return (
    <div>
      {activeTab === "experience" && <ExperienceJobCard />}
      {activeTab === "education" && <ExperienceEducationCard />}
    </div>
  );
}
