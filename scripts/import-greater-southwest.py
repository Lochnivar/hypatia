"""One-off: import tk-dfw chapters into Hypatia greater-southwest/the-incident."""
from pathlib import Path

# tk-dfw is a sibling repo of hypatia (same parent directory)
SRC = Path(__file__).resolve().parents[2] / "tk-dfw" / "chapters"
DST = Path(__file__).resolve().parents[1] / "greater-southwest" / "the-incident"

TITLES = [
    "The Event",
    "Organization",
    "Passenger Perspective",
    "Military Coordination",
    "Power Failure",
    "First Contact",
    "The Revelation",
    "The Investigation",
    "The Assembly",
    "The Arrival",
    "The Cabinet",
    "Government Structure",
    "Cultural Primer",
]


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    for i in range(1, 14):
        src_file = SRC / f"chapter-{i:02d}.md"
        text = src_file.read_text(encoding="utf-8")
        if "## Chapter Content" not in text:
            raise SystemExit(f"Missing marker in {src_file}")
        _, body = text.split("## Chapter Content", 1)
        body = body.strip()
        if not body:
            raise SystemExit(f"Empty body in {src_file}")
        fm = f"""---
layout: chapter
title: "Chapter {i} — {TITLES[i - 1]}"
world: greater-southwest
book: the-incident
order: {i}
---

"""
        out = DST / f"ch{i:02d}.md"
        out.write_text(fm + body + "\n", encoding="utf-8")
        print("Wrote", out.name, len(body), "chars")


if __name__ == "__main__":
    main()
