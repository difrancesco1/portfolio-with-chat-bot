"use client";

interface BiographyItem {
  id: number;
  bulletPoint: string;
  order: number;
}

interface AboutBodyProps {
  biography: BiographyItem[];
}

export default function AboutBody({ biography }: AboutBodyProps) {
  return (
    <div className="flex flex-col gap-1">
      {biography.map((item) => (
        <span key={item.id}>{item.bulletPoint}</span>
      ))}
    </div>
  );
}
