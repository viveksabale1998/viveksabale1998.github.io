# Vivek Sabale - Academic Website

> **Live Website:** [https://viveksabale1998.github.io/](https://viveksabale1998.github.io/)

This website is built using [Zola](https://www.getzola.org/) and hosted with **GitHub Pages**. All updates are built and deployed automatically via **GitHub Actions**.

---

## ⚡ The 3-Step Update Flow

You don't need any local compilers or tools to update the website.

```
┌─────────────────┐       ┌───────────────────────┐       ┌───────────────────────┐
│ 1. Edit File    │ ───>  │ 2. Push to GitHub     │ ───>  │ 3. Live in ~1 minute  │
│ (Markdown/TOML) │       │ (./deploy.sh or git)  │       │ (GitHub Actions)      │
└─────────────────┘       └───────────────────────┘       └───────────────────────┘
```

1. **Edit the file** you want to update (see the table below).
2. **Push your changes** using the quick helper script:
   ```bash
   ./deploy.sh "Updated publications"
   ```
   *(Or standard git: `git add . && git commit -m "Update" && git push`)*
3. **Wait ~1-2 minutes**: GitHub Actions automatically builds the site and publishes it to your live link.

---

## 🗺️ Quick Edit Map: What to Edit & Where

| Section on Website | File to Edit | Notes |
| :--- | :--- | :--- |
| **Hero Bio & Tagline** | [`content/_index.md`](content/_index.md) | In frontmatter (`hero_title`, `hero_bio`, etc.) |
| **Research Interests** | [`content/_index.md`](content/_index.md) | Bullet list in the markdown body |
| **Technical Skills** | [`content/_index.md`](content/_index.md) | Skill buttons in the markdown body |
| **Publications** | [`content/publications.md`](content/publications.md) | Papers list; citation stats auto-update weekly via GitHub Actions |
| **Education & Awards** | [`content/awards.md`](content/awards.md) | Degrees, scholarships, and conference grants |
| **CV (PDF & Embed)** | Replace [`static/assets/Vivek_Sabale_CV.pdf`](static/assets/Vivek_Sabale_CV.pdf) | Keep the exact filename so existing links work |
| **Codes / Projects** | [`content/codes.md`](content/codes.md) & [`content/projects/`](content/projects/) | Edit intro in `codes.md`; add `.md` files in `content/projects/` |
| **Blog Posts** | [`content/posts/`](content/posts/) | Add a new `.md` file for each post |
| **Collaboration** | [`content/collaboration.md`](content/collaboration.md) | Areas of collaborative research and contact |
| **Gallery** | [`content/gallery.md`](content/gallery.md) | Add image card; place images in [`static/assets/`](static/assets/) |
| **Nav Menu & Socials** | [`config.toml`](config.toml) | Under `navigation` and `social_icons` |

---

## 📝 Common Tasks (Copy-Paste Templates)

### 1. Adding a New Publication
Open [`content/publications.md`](content/publications.md) and paste at the top of the list:

```markdown
**Paper Title Here**  
Co-author 1, Vivek Balasaheb Sabale, Co-author 3  
*Journal Name Volume (Issue), Page/Article ID (Year)*  
[View Publication →](https://doi.org/your-doi-link)
```

---

### 2. Updating Your CV
1. Export your latest CV as a PDF named **`Vivek_Sabale_CV.pdf`**.
2. Replace the file at:
   ```
   static/assets/Vivek_Sabale_CV.pdf
   ```
3. Run `./deploy.sh "Updated CV"`. Both the downloadable link and the PDF viewer on the `/cv` page will update automatically.

---

### 3. Updating Bio, Skills, or Research Interests (Homepage)
Open [`content/_index.md`](content/_index.md):
- **Bio & Photo**: Edit `hero_title`, `hero_bio`, or `hero_image` in the `[extra]` frontmatter.
- **Research Interests**: Edit the bulleted list under `## Research Interests`.
- **Technical Skills**: Edit or add skills under `## Technical Skills`.
- **Useful Links**: Edit or add links under `## Useful Links`.

---

### 4. Adding a Code / Project Card
Create a new file in `content/projects/my-new-project.md`:

```toml
+++
title = "Project Name"
date = 2025-01-01
description = "One-line summary of what this code does."
[extra]
link = "https://github.com/viveksabale1998/your-repo"
+++

Detailed description or documentation for the project goes here.
```
*(Project cards automatically receive pastel color styling).*

---

### 5. Adding a Blog Post
Create a new file in `content/posts/my-post-title.md`:

```toml
+++
title = "My Post Title"
date = 2025-01-01
description = "A brief summary for previews."
[taxonomies]
tags = ["quantum", "research"]
+++

Write your content here in standard Markdown.
```

---

### 6. Adding a Photo to the Gallery
1. Save your picture into `static/assets/` (e.g. `static/assets/conference2025.jpeg`).
2. Open [`content/gallery.md`](content/gallery.md) and add:
   ```html
   <div class="gallery-item">
     <img src="/assets/conference2025.jpeg" alt="Conference 2025">
     <p>Conference 2025</p>
   </div>
   ```

---

<details>
<summary>🛠️ <strong>Advanced / Developer Notes (Click to expand)</strong></summary>

### Local Testing (Optional)
If you wish to preview locally before pushing:
1. Install Zola (`brew install zola` on macOS).
2. Run `zola serve` from the project root.
3. Open `http://127.0.0.1:1111`.

### SCSS Architecture
Custom styling resides in `sass/css/`:
- `0-settings/`: Global variables & colors (`_A_variables.scss`, `_B_color-scheme.scss`)
- `1-tools/`: Mixins, reset, grid
- `2-base/`: Base typography & HTML styling
- `3-modules/`: Header, footer, navigation
- `Components/`: Cards, buttons, hero, gallery

### GitHub Action Details
Workflow configuration is stored in [`.github/workflows/main.yml`](.github/workflows/main.yml). It listens on pushes to `main` and uses `shalzz/zola-deploy-action@v0.21.0` to compile and publish to the `gh-pages` branch.
</details>