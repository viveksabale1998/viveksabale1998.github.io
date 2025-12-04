# Vivek Sabale - Academic Website

This website is built with [Zola](https://www.getzola.org/) using the [Vonge](https://github.com/paberr/vonge-zola-theme) theme.

## Project Structure

- **`content/`**: Contains all the markdown content for your site.
    - **`projects/`**: Individual project pages (e.g., `qnn-classification.md`).
    - **`posts/`**: Blog posts.
    - **`*.md`**: Standalone pages like `experience.md`, `cv.md`, `contact.md`.
- **`static/`**: Static assets like images and PDFs. Place your images in `static/assets/`.
- **`themes/`**: Contains the Vonge theme submodule.
- **`config.toml`**: Main configuration file for the site.
- **`.github/workflows/`**: GitHub Actions workflow for automatic deployment.

## How to Update Content

### Adding a New Project
1. Create a new markdown file in `content/projects/` (e.g., `my-new-project.md`).
2. Add the following front matter to the top of the file:
   ```toml
   +++
   title = "My New Project"
   date = 2024-01-01
   description = "A brief description of the project."
   [extra]
   image = "assets/your-image.jpg" # Path relative to static/
   link = "https://github.com/your-repo" # Optional link to code
   +++
   ```
3. Write your project description below the `+++`.

### Adding a New Blog Post
1. Create a new markdown file in `content/posts/` (e.g., `my-first-post.md`).
2. Add the following front matter:
   ```toml
   +++
   title = "My First Post"
   date = 2024-01-01
   description = "Summary of the post."
   [taxonomies]
   tags = ["quantum", "physics"]
   [extra]
   image = "assets/post-image.jpg" # Optional
   +++
   ```
3. Write your post content.

### Updating Pages (Experience, CV, etc.)
1. Open the relevant file in `content/` (e.g., `content/experience.md`).
2. Edit the markdown content.
3. **Important**: Ensure the front matter always includes a `date` field, as the theme requires it:
   ```toml
   +++
   title = "Experience"
   date = 2024-01-01
   template = "page.html"
   +++
   ```

## Configuration
Edit `config.toml` to change site-wide settings:
- **`title`**: Your name or site title.
- **`extra.navigation`**: Links in the top navigation bar.
- **`extra.social_icons`**: Social media links in the footer.
- **`extra.content_blocks`**: Sections on the homepage (Hero, Projects, etc.).

## Local Development
To preview changes locally:
1. Install Zola:
   ```bash
   brew install zola  # macOS
   ```
2. Run the server:
   ```bash
   zola serve
   ```
3. Open `http://127.0.0.1:1111` in your browser.

## Deployment
Deployment is automated via GitHub Actions.
1. Commit your changes:
   ```bash
   git add .
   git commit -m "Update content"
   ```
2. Push to the `main` branch:
   ```bash
   git push origin main
   ```
3. The workflow will automatically build and deploy the site to the `gh-pages` branch. You can check the progress in the "Actions" tab of your repository.