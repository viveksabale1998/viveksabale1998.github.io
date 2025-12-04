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
Create a file in `content/posts/`:
```toml
+++
title = "My Post"
date = 2024-01-01
description = "Summary."
[taxonomies]
tags = ["tag1", "tag2"]
+++
```

### Updating Pages
Edit files like `content/experience.md` or `content/cv.md`. **Always ensure the `date` field is present** in the front matter.

## Local Development
1.  Install Zola.
2.  Run `zola serve`.
3.  Visit `http://127.0.0.1:1111`.