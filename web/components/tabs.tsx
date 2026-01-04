"use client";

interface TabsProps {
  tabs: string[];
  activeTab: string;
  handleTabChange: (a: string) => void;
}

export default function Tabs({ tabs, activeTab, handleTabChange }: TabsProps) {
  return (
    <>
      <div className="w-full flex h-full rounded-2xl bg-background py-1 px-2 font-bold">
        <div className="w-full flex gap-4">
          {tabs.map((tab, index) => (
            <span
              key={index}
              onClick={() => handleTabChange(tab)}
              className={`cursor-pointer ${tab === "contact" ? "ml-auto" : ""}
              ${
                activeTab === tab
                  ? "text-active-tab"
                  : "text-inactive-tab hover:text-inactive-tab-hover"
              }
              `}
            >
              {tab}
            </span>
          ))}
        </div>
      </div>
    </>
  );
}
