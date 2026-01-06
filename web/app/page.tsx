import MainCard from "../components/main-card";

// fetch the data
//

export default function Home() {
  return (
    <div>
      <div className="flex flex-col items-center justify-center h-screen w-full bg-gradient-to-bl from-zinc-100 to-indigo-200 dark:from-zinc-900 dark:to-indigo-900">
        <MainCard />
      </div>
    </div>
  );
}
