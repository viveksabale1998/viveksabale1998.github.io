# Vivek Sabale - Academic Website

This is the source code for my academic website, built with [Zola](https://www.getzola.org/).

## Project Structure

- `content/`: Markdown files for pages and projects.
- `static/`: Static assets (images, PDFs).
- `templates/`: HTML templates.
- `sass/`: SCSS stylesheets.
- `config.toml`: Site configuration.

## Deployment

This site is configured to automatically deploy to GitHub Pages using GitHub Actions.
Any push to the `main` branch will trigger a build and deploy to the `gh-pages` branch.

## Local Development

1. Install Zola:
   ```bash
   brew install zola  # macOS
   ```
2. Run the development server:
   ```bash
   zola serve
   ```
3. Open `http://127.0.0.1:1111` in your browser.
