# Hypatia

Static GitHub Pages site for self-published stories. Flat hierarchy: Index → World → Books → Chapters.

## Structure

- **Index**: Author intro + world list
- **World**: World intro + book list
- **Book**: Book description + chapter list
- **Chapter**: Story text + sidebar TOC

## Local Development

```bash
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000

## Content

Add worlds as `world-slug/index.md`, books as `world-slug/book-slug/index.md`, chapters as `world-slug/book-slug/ch01.md`. See [docs/STRUCTURE.md](docs/STRUCTURE.md) for frontmatter and conventions.

## Footnotes

Footnotes use the Librarian voice (snarky meta-commentary). See `meta/librarian/` for the voice guide.
