"use client";
import AboutBody from "./about-body";
import AboutHeader from "./about-header";
const title = "hi josh here 👋";

// temp biography before we pull from BE
const biography = [
  {
    id: 0,
    bulletPoint:
      "I'm a full stack engineer and  content creator passionate about building modern web applications, UI/UX and AI solutions while sharing my knowledge through tutorials and project walkthroughs.",
    order: 1,
  },
];

export default function AboutSection() {
  return (
    <div className="flex flex-col gap-4 px-2 h-full">
      <AboutHeader title={title} />
      <AboutBody biography={biography} />
    </div>
  );
}
