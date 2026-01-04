"use client";

interface AboutHeaderProps {
  title: string;
}

export default function AboutHeader({ title }: AboutHeaderProps) {
  return (
    <>
      <h1 className="text-3xl">{title}</h1>
    </>
  );
}
