# Footnote Styling Conventions

Footnotes use the Librarian voice. Styling should signal that they are **meta-commentary**, not part of the narrative.

## Markdown Syntax

```markdown
Here is a sentence with a footnote.[^1]

[^1]: *The Librarian notes: One wonders if the author has ever actually met a dragon.*
```

## Conventions

- **Italic** for the footnote body (Librarian voice)
- Optional prefix: "*The Librarian notes:*" or "*The Librarian observes:*" to establish voice
- Keep footnotes concise—one or two sentences
- Place footnote definitions at the end of the chapter

## CSS (in assets/css/main.css)

- `.footnotes` — Block at end of content; italic, muted color, subtle border
- `sup` — Superscript for inline refs
- Distinct from narrative body text
