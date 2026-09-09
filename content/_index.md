+++
title = "Home"
[extra]
hero_title = "Hi, I am Vivek Sabale"
hero_bio = "<strong>Quantum Information Researcher</strong> at IIT Jodhpur. I specialize in quantum information and computation, open quantum systems, and quantum machine learning."
hero_image = "assets/profile.jpeg"
cta_text = "Get in touch"
cta_link = "$BASE_URL/awards"
# secondary_cta_text = "See my codes"
# secondary_cta_link = "$BASE_URL/codes"
+++

<div class="home-sections">

<section class="home-section">
  <h2 class="home-section__title">Research Interests</h2>
  <ul class="interests-list">
    <li>Quantum entanglement & correlations</li>
    <li>Open quantum systems & non-Markovian dynamics</li>
    <li>Quantum batteries & energy transfer</li>
    <li>Tensor network methods for many-body systems</li>
    <li>Quantum computing & circuit synthesis</li>
    <li>Quantum machine learning (QNN & QSVM)</li>
  </ul>
</section>

<section class="home-section">
  <h2 class="home-section__title">Technical Skills</h2>
  <div class="skills-wrap">
    <span class="c-button c-button--secondary c-button--small">Julia</span>
    <span class="c-button c-button--secondary c-button--small">Python</span>
    <span class="c-button c-button--secondary c-button--small">Mathematica</span>
    <span class="c-button c-button--secondary c-button--small">QuTiP</span>
    <span class="c-button c-button--secondary c-button--small">Qiskit</span>
    <span class="c-button c-button--secondary c-button--small">PennyLane</span>
    <span class="c-button c-button--secondary c-button--small">ITensor</span>
    <span class="c-button c-button--secondary c-button--small">Yao.jl</span>
  </div>
</section>

<section class="home-section">
  <h2 class="home-section__title">Useful Links</h2>
  <div class="links-wrap">
    <a href="https://sciml.github.io/Scientific_Modeling_Cheatsheet/scientific_modeling_cheatsheet" target="_blank" rel="noopener noreferrer" class="c-button c-button--dark c-button--small">Scientific Modeling Cheatsheet ↗</a>
    <a href="https://cheatsheets.quantecon.org/julia-cheatsheet.html" target="_blank" rel="noopener noreferrer" class="c-button c-button--dark c-button--small">Julia Cheatsheet ↗</a>
  </div>
</section>

</div>

<style>
.home-sections {
  display: flex;
  flex-direction: column;
  gap: 3rem;
  margin-top: 1rem;
}

.home-section__title {
  font-size: 1.85rem;
  font-weight: 700;
  color: #110E38;
  margin-bottom: 1.25rem;
  position: relative;
  padding-bottom: 0.5rem;
}

.home-section__title::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 45px;
  height: 3px;
  background: #1495a7;
  border-radius: 2px;
}

.interests-list {
  font-size: 1.05rem;
  line-height: 1.8;
  color: #334155;
  padding-left: 1.25rem;
}

.interests-list li {
  margin-bottom: 0.35rem;
}

.skills-wrap, .links-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
</style>
