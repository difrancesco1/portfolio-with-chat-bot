"use client";
import { useForm } from "react-hook-form";

import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";

interface ContactFormData {
  name: string;
  email: string;
  message: string;
}

export default function ContactSection() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ContactFormData>();

  const onSubmit = (data: ContactFormData) => {
    alert(JSON.stringify(data));
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div className="flex flex-col p-1">
        <span className="mb-4 text-sm">
          Have a question or want to work together? Shoot me a message!
        </span>
        <div className="flex gap-2 w-full">
          <div className="flex flex-col w-full">
            <Input
              id="name"
              placeholder="name"
              {...register("name", {
                required: "Name is required",
              })}
            />
            <span className="text-destructive text-xs pl-2 min-h-[1.25rem]">
              {errors.name?.message as string}
            </span>
          </div>

          <div className="flex flex-col w-full">
            <Input
              id="email"
              placeholder="email"
              {...register("email", {
                required: "Email is required",
                pattern: { value: /^\S+@\S+$/i, message: "Invalid email" },
              })}
            />
            <span className="text-destructive text-xs pl-2 min-h-[1.25rem]">
              {errors.email?.message}
            </span>
          </div>
        </div>

        <div className="flex flex-col">
          <Textarea
            id="message"
            placeholder="message"
            {...register("message", {
              required: "Message is required",
            })}
          />
          <span className="text-destructive text-xs pl-2 min-h-[1.25rem]">
            {errors.message?.message}
          </span>
        </div>

        <Button type="submit">Send</Button>
      </div>
    </form>
  );
}
