# Vivek Sabale - Academic Website

This website is built with [Zola](https://www.getzola.org/) using a customized version of the [Vonge](https://github.com/paberr/vonge-zola-theme) theme.

## Workflow & Deployment

This site uses **GitHub Actions** for automatic deployment.

1.  **Make Changes**: Edit files locally or directly on GitHub.
2.  **Commit & Push**: Commit your changes and push them to the `main` branch.
    ```bash
    git add .
    git commit -m "Description of changes"
    git push origin main
    ```
3.  **Automatic Build**: The GitHub Action will automatically build the site and deploy it to the `gh-pages` branch.
4.  **Manual Trigger**: You can also manually trigger the deployment from the "Actions" tab in your GitHub repository if needed.

## Customization Guide

Most site-wide settings are controlled in `config.toml`.

### 1. Navigation Menu (Top)
To add, remove, or rename menu items:
1.  Open `config.toml`.
2.  Find the `[extra]` section and look for `navigation = [...]`.
3.  Edit the list of links.
    ```toml
    navigation = [
        # { url = "$BASE_URL", title = "Home" }, # Commented out to hide
        { url = "$BASE_URL/projects", title = "Codes" },
        ...
    ]
    ```

### 2. Homepage Body Sections
The homepage is built from blocks defined in `config.toml` under `[[extra.content_blocks]]`.

-   **Hero Section**: The top section with your photo and bio.
    -   Edit `title`, `description_html`, `image`, and buttons.
-   **Research Interests**:
    -   Find the block with `title = "Research Interests"`.
    -   Edit the `description_html` to change the list of interests.
-   **Technical Skills**:
    -   Find the block with `title = "Technical Skills"`.
    -   The skills are HTML buttons. To add a new skill, add a line like:
        ```html
        <a href="#" class="c-button c-button--secondary c-button--small" style="margin: 5px;">New Skill</a>
        ```
-   **Quick Links**:
    -   Find the block with `title = "Quick Links"`.
    -   Edit the HTML to add/remove button links.

### 3. Footer
-   **Footer Menu**:
    -   In `config.toml`, find `[extra.footer]`.
    -   Edit the `menu` list to change the links at the bottom.
-   **Social Icons**:
    -   In `config.toml`, find `social_icons` under `[extra]`.
    -   Add or remove entries. Supported icons depend on the Ionicons set used by the theme.

### 4. Project Cards & Colors
The project cards on the homepage use **dynamic pastel colors** instead of images.
-   **Logic**: The color is generated automatically based on the project's position (index) in the list using HSL: `hsl(index * 60 + 200, 60%, 80%)`.
-   **Adding a Project**:
    1.  Create a file in `content/projects/` (e.g., `new-project.md`).
    2.  Ensure it has the correct front matter (see below).
    3.  The site will automatically assign it the next color in the sequence.

## How to Update Content

### Adding a New Project
Create a new markdown file in `content/projects/` with this front matter:
```toml
+++
title = "My New Project"
date = 2024-01-01
description = "Short description."
[extra]
link = "https://github.com/your-repo" # Optional link
+++
```
*(Note: `image` is no longer used for the card background, but you can keep it for the project page itself if needed.)*

### Adding a New Blog Post
1.  Navigate to `content/posts/`.
2.  Create a new Markdown file (e.g., `my-new-post.md`).
3.  Add the following front matter at the top of the file:
    ```toml
    +++
    title = "My New Post"
    date = 2024-01-01
    description = "A short summary of the post."
    [taxonomies]
    tags = ["research", "update"]
    +++
    ```
4.  Write your content below the `+++` using standard Markdown.


### Updating the CV
1.  **Edit Content**: Modify `content/cv.md` to update the text sections (Education, Research Interests, etc.).
2.  **Update PDF**:
    *   Replace the file `static/assets/Vivek_Sabale_CV.pdf` with your new PDF.
    *   **Important**: Keep the filename exactly `Vivek_Sabale_CV.pdf`, or if you change it, you must also update the links in `content/cv.md`.

### Updating Other Pages
Edit files like `content/awards.md` or `content/gallery.md`. **Always ensure the `date` field is present** in the front matter if required by the template.

## Local Development
1.  Install Zola.
2.  Run `zola serve`.
3.  Visit `http://127.0.0.1:1111`.

## SCSS Architecture

The project follows a modular SCSS architecture (based on ITCSS/7-1 pattern) located in `sass/css/`.

### 0-settings
Configuration and global variables.
- `_A_variables.scss`: Global variables for fonts, sizes, spacing, and breakpoints.
- `_B_color-scheme.scss`: Color palette definitions and theme colors.
- `_C_mixins.scss`: General utility mixins (clearfix, list-reset, screen-reader).
- `_D_helpers.scss`: Helper classes for spacing, alignment, etc.

### 1-tools
Mixins and functions.
- `_A_normalize.scss`: CSS normalization to ensure consistent rendering across browsers.
- `_B_reset.scss`: CSS reset to remove default browser styling.
- `_C_shared.scss`: Shared styles and placeholders.
- `_D_syntax-highlighting.scss`: Styles for code block syntax highlighting.
- `_E_grid.scss`: Grid system mixins and classes for layout.
- `_F_tiny-slider.scss`: Styles for the Tiny Slider plugin.
- `_G_animate.scss`: Animation keyframes and classes.

### 2-base
Boilerplate code.
- `_base.scss`: Base HTML element styles (body, headings, links, typography).

### 3-modules
Reusable UI components.
- `_header.scss`: Site header, navigation menu, and mobile menu styles.
- `_footer.scss`: Site footer styles.
- `_pagination.scss`: Pagination control styles.
- `_scroll-button-top.scss`: Styles for the "Back to top" button.
- `_sections.scss`: General section container styles.
- `_social-links.scss`: Styles for social media icon links.

### 4-layouts
Page-level layouts.
- `_page-layout.scss`: Main page layout structure and container styles.

### Components
Specific functional components.
- `_blog-card.scss`: Styles for blog post preview cards.
- `_button.scss`: Button styles (primary, secondary, etc.).
- `_contact-form.scss`: Contact form input and button styles.
- `_content.scss`: Styles for the main content area.
- `_hero.scss`: Styles for the homepage hero section.
- `_newsletter.scss`: Styles for the newsletter subscription form.
- `_page-heading.scss`: Styles for page titles and descriptions.
- `_page-image.scss`: Styles for featured images on pages.
- `_posts-list.scss`: Styles for the list of blog posts.
- `_project-card.scss`: Styles for project portfolio cards (including dynamic colors).
- `_testimonial-card.scss`: Styles for testimonial cards.
- `_testimonials-section.scss`: Layout styles for the testimonials section.

### Global Files
- `global.scss`: Main entry point that imports all other SCSS files.
- `tag.scss`: Specific styles for tag archive pages.