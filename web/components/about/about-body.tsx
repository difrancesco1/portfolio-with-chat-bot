"use client";

import ChatPrompt from "./chat-prompt";
import ContentTabs from "./content-tabs";
import GitHubCalendar from "./github-calendar";
import { Tabs, TabsContent } from "@/components/ui/tabs";

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
    <div className="flex flex-col gap-2 h-full">
      {biography.map((item) => (
        <span key={item.id}>{item.bulletPoint}</span>
      ))}
      <Tabs defaultValue="chatbot" className="flex-1 flex flex-col gap-2">
        <ContentTabs />
        <TabsContent value="chatbot" className="flex-1 mt-0">
          <ChatPrompt />
        </TabsContent>
        <TabsContent value="github" className="flex-1 mt-0">
          <GitHubCalendar />
        </TabsContent>
      </Tabs>
    </div>
  );
}
