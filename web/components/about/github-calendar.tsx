"use client";

import { GitHubCalendar } from "react-github-calendar";
import { useTheme } from "next-themes";

interface GitHubCalendarWrapperProps {
  username?: string;
}

export default function GitHubCalendarWrapper({
  username = "difrancesco1",
}: GitHubCalendarWrapperProps) {
  const { theme } = useTheme();

  return (
    <div className="w-full h-full border border-secondary rounded-sm p-2 flex flex-col bg-background overflow-auto">
      <div className="mb-4">
        <h3 className="text-sm font-semibold mb-1">
          GitHub Contribution Graph
        </h3>
      </div>

      <div className="">
        <GitHubCalendar
          username={username}
          colorScheme={theme === "dark" ? "dark" : "light"}
          fontSize={12}
          blockSize={6.5}
          blockMargin={3}
        />
      </div>
    </div>
  );
}
