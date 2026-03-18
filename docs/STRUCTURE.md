# Hypatia Structure Reference

Portable reference for AI and authors. Hypatia is a static Jekyll site for self-published stories on GitHub Pages.

## Directory Tree

```
/
├── _config.yml
├── _data/
│   └── author.yml           # Author intro (bio)
├── _layouts/
├── _includes/
├── assets/css/
├── index.md
├── library/
│   ├── mjfl.md              # The Librarian (MJFL)
│   └── staff/
│       ├── kronvoldt.md
│       ├── auto.md
│       └── claudette.md
├── <world-slug>/
│   ├── index.md             # World intro
│   ├── <book-slug>/
│   │   ├── index.md         # Book page
│   │   ├── ch01.md
│   │   ├── ch02.md
│   │   └── ...
│   └── ...
└── meta/                    # Excluded from build
    └── librarian/
        ├── voice.md
        ├── styling.md
        └── examples.md
```

## Naming Conventions

- **Slugs**: kebab-case (`terra-nova`, `first-chronicle`)
- **Chapters**: Zero-padded (`ch01.md`, `ch02.md`, … `ch10.md`) for correct sort
- **World/book pages**: `index.md` in each folder

## Frontmatter Schema

### World (`world-slug/index.md`)

```yaml
---
layout: world
title: "Terra Nova"
world: terra-nova
order: 1
---
```

### Book (`world-slug/book-slug/index.md`)

```yaml
---
layout: book
title: "First Chronicle"
world: terra-nova
book: first-chronicle
order: 1
---
```

### Chapter (`world-slug/book-slug/ch01.md`)

```yaml
---
layout: chapter
title: "Chapter 1"
world: terra-nova
book: first-chronicle
order: 1
---
```

## Checklist: Adding Content

### New World

1. Create `world-slug/` directory
2. Create `world-slug/index.md` with world frontmatter
3. Add body (world intro)

### New Book

1. Create `world-slug/book-slug/` directory
2. Create `world-slug/book-slug/index.md` with book frontmatter
3. Add body (book description)

### New Chapter

1. Create `world-slug/book-slug/chNN.md` (zero-pad)
2. Add chapter frontmatter with `world`, `book`, `order`
3. Add story content

## Footnotes

Syntax:

```markdown
Text with a footnote.[^1]

[^1]: *The Librarian notes: Snarky meta-commentary here.*
```

- Librarian voice: snarky, pedantic, academic
- Comments *on* the text, not explanatory
- See `meta/librarian/` for voice and examples
