"use client"

const content = {
    header: "hi, josh here",
    body: [
        "28 yo fullstack developer based in Seattle",
        "Fullstack by trade, frontend by passion.",
        "Founder of Sapling AI",
        "For Q&A, start a chat with Josh Support",
    ]
};

export default function AboutCard() {
    return (
        <div className="w-[98%]">
            <h2>{content.header}</h2>
            <div>
                {content.body.map((line, index) => (
                    <p key={index}>{line}</p>
                ))}
            </div>
        </div>
    )
}