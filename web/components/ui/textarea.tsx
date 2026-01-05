import * as React from "react";

import { cn } from "@/lib/utils";

function Textarea({ className, ...props }: React.ComponentProps<"textarea">) {
  return (
    <textarea
      data-slot="textarea"
      className={cn(
        "file:text-foreground placeholder:text-inactive-tab selection:bg-primary selection:text-primary-foreground dark:bg-input/30 border-ring w-full min-w-0 rounded-md border bg-transparent px-3 py-2 text-base shadow-xs transition-[border-color] outline-none disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
        "focus-visible:border-active-tab",
        "aria-invalid:border-destructive",
        "min-h-[120px] resize-none",
        className
      )}
      {...props}
    />
  );
}

export { Textarea };
