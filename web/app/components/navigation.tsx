"use client"

interface NavigationItem {
    title: string;
}

interface Props {
    items: NavigationItem[];
    activeItem: number;
    setActiveItem: (index: number) => void;
}

export default function Navigation( {items, activeItem, setActiveItem}: Props ) {
    return (
        <>
            <nav className="flex gap-4 flex-start w-[98%] text-primary cursor-pointer">
                {items.map((item, index) => (
                    <a 
                        key={item.title}
                        onClick={() => setActiveItem(index)}
                        className={`hover:text-black ${activeItem === index ? "text-black" : ""} ${index === items.length - 1 ? "ml-auto" : ""}`}
                    >
                        {item.title}
                    </a>
                ))}
            </nav>
        </>
    )
}