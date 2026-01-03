"use client";

import Image from "next/image";
import SaplingLogo from "@/public/plant.png";
import InvestCloudLogo from "@/public/investCloud-logo.png";
const ExperienceItems = [
  {
    id: 0,
    order: 1,
    companyName: "Sapling AI",
    role: "Technical Founder",
    dateFrom: "11/24",
    dateTo: "Present",
    companyImage: SaplingLogo,
    bulletPoint: [
      "Architected full-stack AI tutoring platform using Python FastAPI, TypeScript Next.js, and PostgreSQL maintaining cloud infrastructure and serving over 2,000 users.",
      "Built SSE streaming system that validates and renders AI-generated educational questions as interactive React components using Zod schemas.",
      "Built a custom agentic AI orchestration system with RAG integration, engineered prompts with dynamic context injection, and LangSmith monitoring for lesson generation workflows.",
      "Built RESTful API endpoints with dependency injection, JWT authentication, and Pydantic schemas ensuring type safety across Python backend and TypeScript frontend.",
      "Optimized application performance using React Query for server-state caching and Zustand for efficient client-state management, reducing API calls and improving load times.",
    ],
  },
  {
    id: 1,
    order: 2,
    companyName: "Invest Cloud",
    role: "Software Engineer",
    dateFrom: "03/22",
    dateTo: "11/24",
    companyImage: InvestCloudLogo,
    bulletPoint: [
      "Led development for companies enterprise trading interface processing over 100,000+ daily transactions for Wells Fargo and other banks, utilizing React/JavaScript, REST/WebSocket APIs, and PowerBI embeddings.",
      "Collaborated with the design team to build a reusable React component library to display Power BI data visualizations, implementing themed CSS design tokens for consistent spacing, colors, and typography across all client platforms.",
      "Enhanced application performance using React Developer Tools and profiling techniques, reducing Time to First Paint by 65% while implementing Jest/RTL unit tests with 90% coverage.",
    ],
  },
];

export default function ExperienceJobCard() {
  return (
    <div>
      <div className="w-full rounded-lg border border-black/10 p-2 flex gap-3 flex-col">
        {ExperienceItems.map((item) => (
          <div key={item.id}>
            <div className="flex items-center gap-3">
              <Image
                className="rounded-full bg-white object-cover border border-gray-300 flex-shrink-0 mb-auto"
                alt="Sapling"
                src={item.companyImage}
                width={48}
                height={48}
              />
              <div className="flex flex-col w-full">
                <span className="font-semibold">{item.companyName}</span>
                <div className="flex justify-between w-full text-inactive-tab text-sm">
                  <div>{item.role}</div>
                  <div>
                    {item.dateFrom} - {item.dateTo}
                  </div>
                </div>
              </div>
            </div>
            <div className="flex flex-col w-full text-sm gap-1">
              <div className="flex flex-col pl-16">
                {item.bulletPoint.map((item, index) => (
                  <div className="flex gap-2 pr-8" key={index}>
                    <span className="flex-shrink-0">•</span>
                    <span className="flex-1">{item}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
