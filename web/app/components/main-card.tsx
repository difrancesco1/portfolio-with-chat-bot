"use client";
import { useState } from "react";
import Topbar from "./topbar"

export default function MainCard() {
  const [open, setOpen] = useState(false);

  const toggleOpen = () => {
    setOpen((prev) => {
      return !prev;
    })
  }
  
  return (
    <div className={`max-w-[28rem] ${open ? 'main-card-open' : 'main-card-collapsed'}`}>
      <Topbar toggleOpen={toggleOpen} open={open}/>
    </div>
  );
}
