"use client";
import Image, { StaticImageData } from "next/image";
import linqqImage from "@/public/linqq.png";
import { FaLinkedin, FaGithub } from "react-icons/fa";

const projects = [
  {
    id: 0,
    title: "linqq",
    subtitle: "customizable creater profiles",
    featuredImage: linqqImage,
    projectDescription:
      "Streampage is an all-in-one influencer platform featuring customizable widgets, community events, gaming profile integration, and interactive components. Expanding beyond traditional link-in-bio tools.",
    tags: [
      "TypeScript",
      "Python",
      "Nextjs",
      "Docker",
      "FastAPI",
      "PostgreSQL",
      "Supabase",
      "TailwindCSS",
    ],
    githubLink: "url",
    websiteLink: "url",
  },
];

export interface Project {
  id: number;
  title: string;
  subtitle: string;
  featuredImage: StaticImageData | string;
  projectDescription: string;
  tags: string[];
  githubLink?: string | null;
  websiteLink?: string | null;
}

interface ProjectsCardProps {
  project: Project;
}

export default function ProjectsCard() {
  return (
    <div className="flex flex-col">
      {projects.map((item) => (
        <div key={item.id} className="flex gap-0.5 flex-col text-sm">
          <div className="text-[16px] font-semibold">{item.title}</div>
          <div>{item.subtitle}</div>
          <div className="flex gap-1">
            <Image
              src={item.featuredImage}
              width={200}
              height={200}
              alt={item.title}
            />
            <div className="pr-10">{item.projectDescription}</div>
          </div>
          <div className="flex gap-1 text-xs">
            {item.tags.map((item, index) => (
              <div className="px-1 py-0.5 bg-black/10 rounded-lg" key={index}>
                {item}
              </div>
            ))}
          </div>
          <div className="flex gap-2">
            <FaLinkedin
              size={24}
              onClick={() => window.open(item.websiteLink || undefined)}
              className="cursor-pointer"
            />
            <FaGithub
              size={24}
              onClick={() => window.open(item.githubLink || undefined)}
              className="cursor-pointer"
            />
          </div>

          {item.githubLink && <div>{item.githubLink}</div>}
          {item.websiteLink && <div>{item.websiteLink}</div>}
        </div>
      ))}
    </div>
  );
}
