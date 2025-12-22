"use client";
import { useState } from "react";
import AddRoundedIcon from '@mui/icons-material/AddRounded';
import RemoveRoundedIcon from '@mui/icons-material/RemoveRounded';
import Typewriter from 'typewriter-effect';

export default function MainCard() {
  const [open, setOpen] = useState(false);

  const toggleOpen = () => {
    setOpen((prev) => {
      return !prev;
    })
  }
  return (
    <div className={` max-w-[28rem] ${open ? 'main-card-open' : 'main-card-collapsed'}`}>
      <div className='flex w-full items-center justify-between text-foreground'>
        <div className="flex gap-1 items-center">
          <span>Joshua DiFrancesco</span>
          <span className='text-sm'> ~ %</span>
          {!open && 
          <Typewriter
            options={{
              strings: [
                'ls projects',
                'cat skills.txt',
                './run typescript',
                'python main.py',
                'psql -d portfolio',
                'curl api/contact',
              ],
              autoStart: true,
              loop: true,
              cursor: '▎',
              cursorClassName: 'cursor-solid',
            }}
          />
        }
        </div>
        <div className={`${open ? "menu-button-open" : "menu-button-collapsed"}`}>
          { open ? <RemoveRoundedIcon onClick={toggleOpen}/> : <AddRoundedIcon onClick={toggleOpen}/> } 
        </div>
      </div>
    </div>
  );
}
