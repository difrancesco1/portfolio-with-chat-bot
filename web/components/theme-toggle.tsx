"use client";

import { FaRegMoon } from "react-icons/fa";
import { LuSun } from "react-icons/lu";
import { useTheme } from "next-themes";
import { useEffect, useState } from "react";

export function ThemeToggle() {
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  // useEffect only runs on the client, so now we can safely show the UI
  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return (
      <button
        className="p-2 rounded-lg transition-all duration-300"
        aria-label="Toggle theme"
      >
        <div className="w-5 h-5" />
      </button>
    );
  }

  const toggleTheme = () => {
    setTheme(theme === "dark" ? "light" : "dark");
  };

  return (
    <button
      onClick={toggleTheme}
      className="p-2 rounded-lg hover:bg-secondary transition-all duration-300"
      aria-label={`Switch to ${theme === "dark" ? "light" : "dark"} mode`}
    >
      {theme === "dark" ? (
        <LuSun className="w-5 h-5 text-foreground transition-transform duration-300 hover:rotate-45" />
      ) : (
        <FaRegMoon className="w-5 h-5 text-foreground transition-transform duration-300 hover:-rotate-12" />
      )}
    </button>
  );
}
