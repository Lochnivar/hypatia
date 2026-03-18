# Hypatia — Agent Instructions

Hypatia is a static GitHub Pages site for self-published stories. When this project is in context, follow these conventions.

## Site Hierarchy

- **Index** → Author intro + list of worlds
- **World** → World intro + list of books
- **Book** → Book description + list of chapters
- **Chapter** → Story text + sidebar TOC (chapters in this book)

## File Structure (Flat)

Content lives at repo root. No `content/` prefix.

```
/
├── index.md                 # Main page
├── terra-nova/
│   ├── index.md             # World (layout: world)
│   ├── first-chronicle/
│   │   ├── index.md         # Book (layout: book)
│   │   ├── ch01.md
│   │   ├── ch02.md
│   │   └── ...
│   └── second-chronicle/
└── another-world/
```

- **meta/** — Excluded from build. Librarian voice guide, styling, examples. For author/AI reference only.
- **library/** — The Librarian (MJFL) and staff. MJFL is the Hypatia footnote voice; staffers are Kronvoldt, Auto, Claudette. See `meta/librarian/mjfl.md`.

## Frontmatter

| Type   | Required fields                                    |
|--------|----------------------------------------------------|
| World  | `layout: world`, `title`, `world: <slug>`, `order` |
| Book   | `layout: book`, `title`, `world`, `book: <slug>`, `order` |
| Chapter| `layout: chapter`, `title`, `world`, `book`, `order` |

Use kebab-case slugs: `terra-nova`, `first-chronicle`.

## Adding Content

- **New world**: Create `world-slug/index.md` with world frontmatter.
- **New book**: Create `world-slug/book-slug/index.md` with book frontmatter.
- **New chapter**: Create `world-slug/book-slug/ch01.md` (zero-pad: ch01, ch02, … ch10).

## Footnotes (Librarian Voice)

Footnotes are meta-commentary from a snarky Librarian—not part of the narrative.

```markdown
Sentence with a footnote.[^1]

[^1]: *The Librarian notes: One wonders if the author has ever actually met a dragon.*
```

- Use italic for footnote body
- Snarky, pedantic, academic tone
- Comments *on* the text, not explanatory
- See `meta/librarian/` for voice guide and examples
