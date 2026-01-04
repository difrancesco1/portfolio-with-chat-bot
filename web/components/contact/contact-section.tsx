"use client"

import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"

export default function ContactSection() {
    return (
        <div className="flex flex-col gap-2 p-4">
            <div className="flex gap-2">
                <Input id="name" type="text" placeholder="Name"/>
                <Input id="email" type="text" placeholder="Email"/>
            </div>
            <Textarea 
                id="message" 
                placeholder="Drop a note with any website feedback or career opportunities, or just say hi!"
            />
            
        </div>
    )
}