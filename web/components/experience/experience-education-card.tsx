"use client";

import Image from "next/image";
import Ucf from "@/public/ucf.jpg";
import Usf from "@/public/usf.png";

const ExperienceItems = [
  {
    id: 0,
    order: 1,
    schoolName: "University of South Florida",
    major: "Physics",
    dateFrom: "01/16",
    dateTo: "12/20",
    companyImage: Usf,
    bulletPoint: [
      "Architected full-stack AI tutoring platform using Python FastAPI, TypeScript Next.js, and PostgreSQL maintaining cloud infrastructure and serving over 2,000 users.",
    ],
  },
  {
    id: 1,
    order: 2,
    schoolName: "University of Central Florida - Bootcamp",
    major: "Computer Science",
    dateFrom: "12/21",
    dateTo: "03/22",
    companyImage: Ucf,
    bulletPoint: [
      "Led development for companies enterprise trading interface processing over 100,000+ daily transactions for Wells Fargo and other banks, utilizing React/JavaScript, REST/WebSocket APIs, and PowerBI embeddings.",
    ],
  },
];

export default function ExperienceEducationCard() {
  return (
    <div>
      <div className="w-full rounded-lg p-2 flex gap-3 flex-col">
        {ExperienceItems.map((item) => (
          <div key={item.id}>
            <div className="flex gap-3">
              <Image
                className="rounded-full bg-white object-cover border border-gray-300 flex-shrink-0 mb-auto"
                alt="Sapling"
                src={item.companyImage}
                width={48}
                height={48}
              />
              <div className="flex flex-col w-full">
                <span className="font-semibold">{item.schoolName}</span>
                <div className="flex justify-between w-full text-inactive-tab text-sm">
                  <div>{item.major}</div>
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
