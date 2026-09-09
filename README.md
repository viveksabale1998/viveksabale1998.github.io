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

## 🚀 Deployment Architecture: How It Works & The `gh-pages` Branch

This website uses a **dual-branch deployment model** automated through GitHub Actions:

```
┌───────────────────────────────────────┐
│              main Branch              │  <── WHERE YOU WORK
│  (Markdown, TOML, SASS, workflows)    │
└──────────────────┬────────────────────┘
                   │
                   │  git push (or ./deploy.sh)
                   ▼
┌───────────────────────────────────────┐
│        GitHub Actions Runner          │
│   shalzz/zola-deploy-action@v0.21.0   │  <── AUTOMATIC BUILD
│       (Compiles Zola site)            │
└──────────────────┬────────────────────┘
                   │
                   │  Publishes compiled HTML + .nojekyll
                   ▼
┌───────────────────────────────────────┐
│            gh-pages Branch            │  <── COMPILED ARTIFACTS
│ (index.html, styles, JS, subfolders)  │      (DO NOT DELETE OR EDIT DIRECTLY)
└──────────────────┬────────────────────┘
                   │
                   │  GitHub Pages CDN
                   ▼
┌───────────────────────────────────────┐
│ https://viveksabale1998.github.io/    │  <── LIVE WEBSITE
└───────────────────────────────────────┘
```

### Why Is the `gh-pages` Branch Required?

1. **Zola is not natively supported by GitHub Pages:**
   - GitHub Pages only has native, server-side compilation support for Jekyll. It does not natively run Zola.
   - To host a Zola site on GitHub Pages, GitHub Actions compiles your source templates into pure, pre-rendered static HTML, CSS, JavaScript, and KaTeX bundles inside a Docker container, then commits and pushes that ready-to-serve output to the `gh-pages` branch.

2. **Why deleting `gh-pages` breaks the site and shows only the README:**
   - For user sites named `<username>.github.io`, if the `gh-pages` branch is deleted or missing, GitHub Pages automatically falls back to running **Jekyll** on the `main` branch.
   - Because Jekyll does not recognize Zola templates or layouts, it ignores your site design entirely and simply renders [`README.md`](README.md) as the homepage `index.html`.
   - All subpages (`/collaboration/`, `/awards/`, `/codes/`, `/publications/`, `/posts/`) immediately return **404 Not Found**.
   - **Rule:** **Never delete the `gh-pages` branch.** It is the active deployment target that GitHub Pages serves to the internet.

### Required GitHub Pages Repository Settings

To ensure the site is always served from the compiled output:
1. In your GitHub repository, open **Settings** $\rightarrow$ **Pages** (under the "Code and automation" sidebar).
2. Under **Build and deployment**:
   - **Source:** `Deploy from a branch`
   - **Branch:** `gh-pages`
   - **Folder:** `/ (root)`
3. Click **Save** (if not already set).

> [!IMPORTANT]
> - Always make edits, commits, and pushes to the **`main`** branch.
> - Never push source markdown or manual edits to the `gh-pages` branch directly. The `gh-pages` branch is automatically generated and updated on every push by `.github/workflows/main.yml`.

---

## 🗺️ Quick Edit Map: What to Edit & Where

| Section on Website | File to Edit | Notes |
| :--- | :--- | :--- |
| **Hero Bio & Tagline** | [`content/_index.md`](content/_index.md) | In frontmatter (`hero_title`, `hero_bio`, etc.) |
| **Research Interests** | [`content/_index.md`](content/_index.md) | Bullet list in the markdown body |
| **Technical Skills** | [`content/_index.md`](content/_index.md) | Skill buttons in the markdown body |
| **Publications** | [`content/publications.md`](content/publications.md) | Papers list; citation stats auto-update weekly via GitHub Actions |
| **Education, Awards & CV** | [`content/awards.md`](content/awards.md) | Degrees, scholarships, conference grants, and embedded CV |
| **CV PDF File** | Replace [`static/assets/Vivek_Sabale_CV.pdf`](static/assets/Vivek_Sabale_CV.pdf) | Keep the exact filename so existing links work |
| **Codes / Repositories** | [`content/codes.md`](content/codes.md) | Directly add or edit repositories in `codes.md` frontmatter |
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

### 4. Adding or Updating Codes & Repositories
You can add or update repositories directly inside [`content/codes.md`](content/codes.md) without creating extra files!

Open [`content/codes.md`](content/codes.md) and add a new block at the bottom of the frontmatter:

```toml
[[extra.repositories]]
title = "My New Project"
description = "One-line summary of what this code does."
link = "https://github.com/viveksabale1998/my-new-repo"
image = "images/projects/quantum-states.png"  # image path in static/
tags = ["Python", "Qiskit", "Research"]
```
*(Alternatively, you can still add individual markdown files under `content/projects/` if you want a dedicated details page).*

---

### 5. Adding a Blog Post
Create a new file in `content/posts/my-post-title.md`:

```toml
+++
title = "My Post Title"
date = 2026-03-10
description = "A brief summary for previews."
[taxonomies]
tags = ["quantum", "research"]
[extra]
# Choose ONE of these 4 categories to place your post under that subtitle:
# - "Thesis Work"
# - "Research Articles"
# - "Collaboration Work"
# - "Quantum Information Educational"
category = "Thesis Work"
image = "images/posts/my-image.jpg"  # (optional: place image in static/images/posts/)
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

## 🔧 Troubleshooting & Common Build / GitHub Actions Errors

All website builds and deployments happen via GitHub Actions under the **Actions** tab of your GitHub repository. Here is how to diagnose and resolve the most common issues:

### 1. "Node.js XX is deprecated" Warnings in GitHub Actions
- **Why it happens:** GitHub periodically updates the default Node.js runtime on its hosted runners (e.g., migrating from Node 20 to Node 24). When a third-party or official GitHub action targets an older Node version, GitHub outputs a warning:
  ```text
  Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4...
  ```
- **How to fix it:**
  1. Check the action name in the warning (e.g., `actions/checkout` or `actions/setup-python`).
  2. Open your workflow files in [`.github/workflows/`](.github/workflows/):
     - [`.github/workflows/main.yml`](.github/workflows/main.yml)
     - [`.github/workflows/update-citations.yml`](.github/workflows/update-citations.yml)
  3. Bump the version tag to the newest major version supported on Node 24:
     - `actions/checkout@v4` $\rightarrow$ `actions/checkout@v5` (or latest)
     - `actions/setup-python@v5` $\rightarrow$ `actions/setup-python@v7` (or latest)
  4. Commit and push your changes to `main`.

> [!NOTE]
> **Warning on `actions/upload-artifact@v4` in `pages-build-deployment`:**  
> If you see this warning on a 7-step job named `pages-build-deployment`, this is GitHub's **internal** runner executing its automated CDN deployment step from the `gh-pages` branch. It is managed by GitHub's backend (not your repository files), does not fail the build, and GitHub will update its internal runner template automatically. Your own workflows in `.github/workflows/` are already on Node 24.

---

### 2. Zola Build Failure: TOML / Front Matter Syntax Errors
- **Symptom:** The workflow fails at the *Build and Deploy* step with `Failed to parse front matter`.
- **Common causes & fixes:**
  * **HTML comments in front matter:** Markdown files must NOT have `<!-- ... -->` between the `+++` fences. Inside `+++`, comments must use `#`.
  * **Multiline strings:** Multiline descriptions in front matter must be wrapped in triple double quotes:
    ```toml
    description = """First line.
    Second line."""
    ```
  * **Missing closing fence:** Ensure each post opens and closes with `+++`.

---

### 3. Zola Alias Collision
- **Symptom:** Build fails with `Failed to render ... collision with alias`.
- **Cause:** Adding an alias (like `aliases = ["cv"]`) to a file when a physical file already exists at that path (like `content/cv.md`).
- **Fix:** In Zola, an alias cannot overwrite a physical `.md` file. Either delete the redundant `.md` file or rename the alias.

---

### 4. 404 Error on Links or Images
- **Images:** Ensure all images are placed in `static/` (e.g. `static/images/posts/my-image.jpg` or `static/assets/my-photo.jpeg`). In markdown or frontmatter, refer to them without the `static/` prefix (e.g. `images/posts/my-image.jpg`).
- **Repository Links:** In [`content/codes.md`](content/codes.md), external links should start with `https://github.com/...`.

---

### 5. Site Shows Only the README or 404 on Subpages
- **Symptom:** Opening `https://viveksabale1998.github.io/` displays raw `README.md` text instead of your custom homepage, or navigation links like `/collaboration/` return 404.
- **Cause:**
  1. The **`gh-pages`** branch was deleted, or GitHub Pages settings were accidentally changed to deploy from `main`. When that happens, GitHub Pages falls back to default Jekyll, which cannot parse Zola and only serves `README.md`.
  2. Or, your browser has cached an old error response (`Cache-Control: max-age=600`).
- **How to fix it:**
  1. Check that the `gh-pages` branch exists under your repository's branches. If missing, push a commit or trigger the *Build and Deploy Zola Site* workflow in GitHub Actions to regenerate it.
  2. Go to **Settings** $\rightarrow$ **Pages** and confirm that **Source** is set to **`Deploy from a branch`**, branch is **`gh-pages`**, and folder is **`/ (root)`**.
  3. Force-refresh your browser to bypass cached HTML: press `Cmd + Shift + R` (Mac) or `Ctrl + F5` (Windows/Linux), or test in an Incognito window.

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