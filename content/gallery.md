+++
title = " Gallery"
# date = 2024-01-01
template = "page.html"
+++

<!-- # Image Gallery -->

<div class="gallery">
    <div class="gallery-item">
      <img src="/sites/assets/QTML2024.jpeg" alt="QTML 2024">
      <p>QTML 2024</p>
    </div>
    <div class="gallery-item">
      <img src="/sites/assets/TCS2023.jpeg" alt="TCS 2023">
      <p>TCS 2024</p>
    </div>
</div>

<style>
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 20px;
}
.gallery-item img {
    width: 100%;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.gallery-item p {
    text-align: center;
    margin-top: 10px;
    font-style: italic;
}
</style>
