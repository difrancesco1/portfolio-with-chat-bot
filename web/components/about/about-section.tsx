"use client";
import AboutBody from "./about-body";
import AboutFooter from "./about-footer";
import AboutHeader from "./about-header";
const title = "hi josh here 👋";

interface AboutProps {
  handleExternalLink: (a: string) => void;
}

// temp biography before we pull from BE
const biography = [
  {
    id: 0,
    bulletPoint: "28 yo fullstack developer based in Seattle",
    order: 1,
  },
  {
    id: 1,
    bulletPoint: "Fullstack by trade, front-end by passion.",
    order: 2,
  },
  {
    id: 2,
    bulletPoint: "Founder of Sapling AI",
    order: 3,
  },
  {
    id: 3,
    bulletPoint: "For Q&A, start a chat with Josh Support",
    order: 4,
  },
];

export default function AboutSection({ handleExternalLink }: AboutProps) {
  return (
    <div className="flex flex-col gap-4 px-2">
      <AboutHeader title={title} />
      <AboutBody biography={biography} />
      <AboutFooter handleExternalLink={handleExternalLink} />
    </div>
  );
}
