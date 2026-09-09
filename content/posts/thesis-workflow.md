+++
title = "From Quantum Correlations to Their Microscopic Origin: A Journey Through Noise, Memory, and Open-System Dynamics"
date = 2026-03-01
description = "How quantum correlations can be characterized, protected, understood under correlated noise, and ultimately connected to their microscopic physical origin."
[taxonomies]
tags = ["thesis", "quantum-correlations", "open-quantum-systems", "non-markovian", "teleportation"]
[extra]
image = "images/posts/thesis-workflow.jpg"
+++

Quantum technologies rely on phenomena that have no direct classical counterpart. Among them, **quantum correlations**—and particularly entanglement—play a central role in quantum communication, computation, sensing, and information processing. Yet there is a fundamental difficulty: quantum correlations are fragile. Interaction with an environment can degrade them, memory in a quantum channel can modify their dynamics, and collective interactions with a common environment can produce behavior that is very different from that of independently evolving systems.

My doctoral research investigates this problem from several complementary perspectives. Rather than treating quantum correlations, noise, memory, and open-system dynamics as separate topics, the thesis develops a progression:

<div class="thesis-horizontal-flow">
  <span class="step-pill">Characterization</span>
  <span class="step-arrow">→</span>
  <span class="step-pill">Protection</span>
  <span class="step-arrow">→</span>
  <span class="step-pill">Channel Memory</span>
  <span class="step-arrow">→</span>
  <span class="step-pill">Microscopic Dynamics</span>
</div>

The central question evolves along the way:

> **How can quantum correlations be characterized, protected, understood under correlated noise, and ultimately connected to their microscopic physical origin?**

---

## 1. Why start with quantum correlations?

Quantum correlations are not merely mathematical features of quantum states. They can serve as resources for information-processing tasks.

Quantum teleportation is one of the clearest examples. In the standard teleportation protocol, an unknown quantum state can be reconstructed at a distant location using a shared entangled state and classical communication. Experimental demonstrations of quantum teleportation established that this is not merely a theoretical possibility but a realizable quantum-information protocol.

However, the usefulness of an entangled state is not determined simply by whether it is entangled. Its **structure and strength of correlations** matter.

This immediately raises the first question:

> **How should we characterize the correlations contained in a complex multipartite quantum state?**

For two-qubit systems, quantities such as concurrence provide powerful tools. For larger systems, however, the situation becomes considerably more complicated. A multipartite state can contain correlations at different orders, and pairwise measures do not necessarily reveal the complete hierarchy of many-body correlations.

This motivates the first part of the thesis.

---

## 2. Stage I — Characterizing multipartite quantum correlations

The first research direction focuses on the **structure of quantum correlations**.

The central idea is to use connected correlations—or cumulants—to separate genuine higher-order contributions from correlations that can be constructed from lower-order terms. This leads to the **Cumulant-Norm Entanglement Index (CNEI)**, a correlation-based framework designed to characterize multipartite entanglement.

The use of cumulants is particularly natural because cumulants are designed to isolate irreducible correlations. Instead of asking only whether a multipartite state is entangled, the approach asks a more refined question:

> **What order of correlation is genuinely present in the state?**

The resulting index is investigated with respect to separability, local-unitary properties, and different multipartite states. It is also compared with conventional entanglement measures to understand what additional structural information can be obtained from connected correlations.

This first stage establishes the **structural viewpoint** of the thesis:

$$
\text{Quantum state}
\quad\longrightarrow\quad
\text{correlation structure}
\quad\longrightarrow\quad
\text{quantitative characterization}.
$$

But characterization is only the beginning.

A correlation can be quantified perfectly and still be practically useless if environmental noise destroys it before it can be used.

This leads to the second question:

> **Once quantum correlations have been characterized, how can they be protected?**

---

## 3. Stage II — Protecting quantum correlations from noise

Real quantum systems are open systems. They interact with their surroundings, and these interactions introduce decoherence and dissipation.

For quantum teleportation, this has a direct operational consequence. The shared entangled resource becomes degraded, and the quality of the teleported state decreases.

Teleportation fidelity is therefore a natural quantity for measuring the performance of the protocol. But average fidelity alone does not tell the entire story. A protocol may perform well on average while treating different input states differently.

This is where **fidelity deviation** becomes important. It measures the variation of teleportation fidelity over the input-state space and provides a way of assessing the uniformity required for universal quantum teleportation.

This motivates the second stage of the thesis:

> **Can quantum correlations be actively protected against noisy evolution?**

One approach investigated in the thesis is **weak measurement (WM) and weak-measurement reversal (RWM)**.

Weak measurement provides a way of extracting partial information from a quantum system while introducing less disturbance than a projective measurement. A subsequent reversal operation can partially compensate for the measurement-induced disturbance.

The idea is not merely theoretical. Kim *et al.* demonstrated experimentally that weak measurement and measurement reversal can be used to protect entanglement from decoherence and even circumvent entanglement sudden death under suitable conditions.

The thesis extends this protection perspective to different noise environments and examines their consequences for quantum correlations and teleportation.

The analysis includes Markovian and non-Markovian noise processes and examines how WM/RWM affects:

* entanglement,
* teleportation fidelity,
* fidelity deviation,
* information back-flow,
* and the usefulness of imperfectly entangled states for teleportation.

This research direction is also directly connected to the article [**“Toward Realization of Universal Quantum Teleportation Using Weak Measurements,”**](https://onlinelibrary.wiley.com/doi/10.1002/andp.202300392) which investigates weak measurements, memory effects, and non-Markovian dynamics in the context of universal quantum teleportation.

The important conceptual transition is:

$$
\text{Characterize correlations}
\quad\rightarrow\quad
\text{Protect correlations}.
$$

But this raises another issue.

The environment does not always act independently at every stage.

---

## 4. Stage III — When the noise itself has memory

The previous stage treats noise as a dynamical process acting on the quantum system. But in realistic communication scenarios, **successive uses of a quantum channel may themselves be correlated**.

This creates an important distinction between two types of memory.

### Environmental memory

A system interacts with an environment that retains information about its previous state and can subsequently return information to the system.

### Channel-use memory

Different applications of a quantum channel are correlated. The noise acting during one channel use is therefore not statistically independent of the noise acting during another.

These two ideas of memory are conceptually distinct, and their interplay has been studied explicitly in correlated quantum channels. Addis *et al.*, for example, showed how correlations between multiple channel uses can be related to non-Markovianity in the resulting dynamical map.

This distinction forms the basis of the third stage of the thesis.

Instead of asking:

> “How can we protect correlations from noise?”

the question becomes:

> **“What happens when the noise process itself possesses correlations?”**

A correlation parameter $\mu$ is used to interpolate between independent and fully correlated channel action:

$$
\mu=0
\quad\rightarrow\quad
\text{uncorrelated channel},
$$

$$
0<\mu<1
\quad\rightarrow\quad
\text{partially correlated channel},
$$

$$
\mu=1
\quad\rightarrow\quad
\text{fully correlated channel}.
$$

This framework allows the influence of channel correlation to be studied independently of the underlying noise model.

The thesis investigates both **unital and non-unital correlated channels** and examines their non-Markovian behavior using complementary indicators. These include entanglement dynamics, the volume of accessible states, and temporal self-similarity.

The resulting work was developed into the article [**“Facets of Correlated Non-Markovian Channels.”**](https://onlinelibrary.wiley.com/doi/10.1002/andp.202400151) The study examines the interplay between channel correlations and intrinsic non-Markovian dynamics, including entanglement evolution and the geometry of accessible states for both unital and non-unital channels.

An important outcome of this analysis is that channel correlation does not necessarily behave as simply “more noise.”

Instead, correlations can modify memory effects in ways that may sometimes be useful.

For example, the thesis investigates **freezing of quantum correlations**, where a correlation measure remains approximately constant over a period despite ongoing noisy evolution.

It also examines **quantum error correction under correlated non-Markovian noise**.

Thus, the third stage changes the perspective once again:

$$
\text{Noise}
\quad\rightarrow\quad
\text{correlated noise}
\quad\rightarrow\quad
\text{memory as a dynamical resource}.
$$

But there is still a deeper question.

If a correlated channel changes the dynamics, **where does that correlation physically come from?**

---

## 5. Stage IV — From effective channels to microscopic dynamics

A quantum channel is an effective description. It tells us how a quantum state changes:

$$
\rho(0)\rightarrow\rho(t),
$$

but it does not necessarily tell us *why* the evolution has that particular form.

This limitation motivates the final stage of the thesis.

Instead of starting from a prescribed channel, we explicitly model the **system–environment interaction**.

A particularly interesting situation occurs when multiple quantum emitters interact with a common environment. In such a setting, the environment can mediate correlations between the systems.

Now spatial geometry becomes important.

If two emitters are separated by a distance $r_{12}$, the strength of their collective interaction with the environment can depend on that separation. Consequently, the same environment can produce very different entanglement dynamics depending on the spatial configuration of the quantum systems.

This connects the thesis to the Ficek–Tanaś framework of dissipative two-atom dynamics. Their work demonstrated that spontaneous emission and common-environment interactions can generate entanglement and produce phenomena such as transient entanglement and long-lived correlations.

Related work by Ficek and Tanaś also examined entanglement sudden birth and sudden death for two atoms interacting with a common reservoir, showing how collective behavior can produce qualitatively different entanglement dynamics.

This provides the physical setting for the final stage of the thesis.

The analysis considers correlated dephasing and amplitude-damping dynamics and then moves to spatially separated quantum emitters interacting through a common environment.

The key question becomes:

> **How does the physical geometry of the system–environment interaction control the evolution of quantum correlations?**

This leads naturally to phenomena such as:

* entanglement sudden death,
* entanglement sudden birth,
* entanglement revival,
* collective decay,
* subradiant behavior,
* and entanglement trapping.

A common environment therefore does not merely destroy entanglement. Depending on the coupling structure, it can also create, revive, or preserve correlations.

This microscopic perspective completes the transition:

$$
\text{effective correlated channel}
\quad\longrightarrow\quad
\text{physical interaction}
\quad\longrightarrow\quad
\text{correlated open-system dynamics}.
$$

---

## 6. Connecting the four stages

The most important feature of the thesis is therefore not any individual noise model or correlation measure. It is the **connection between levels of description**.

The research can be summarized as:

<div class="thesis-flowchart-card">
  <div class="flow-step">
    <span class="flow-badge">Structure</span>
    <span class="flow-question">How are correlations characterized?</span>
  </div>
  <div class="flow-down-arrow">↓</div>
  <div class="flow-step">
    <span class="flow-badge">Control</span>
    <span class="flow-question">How can correlations be protected?</span>
  </div>
  <div class="flow-down-arrow">↓</div>
  <div class="flow-step">
    <span class="flow-badge">Channel Memory</span>
    <span class="flow-question">How does correlated noise modify their dynamics?</span>
  </div>
  <div class="flow-down-arrow">↓</div>
  <div class="flow-step">
    <span class="flow-badge">Microscopic Origin</span>
    <span class="flow-question">What physical interactions generate those correlations?</span>
  </div>
</div>

This progression is useful because each stage addresses a limitation of the previous one.

| Stage | Question | Description |
| :--- | :--- | :--- |
| **Chapter 2** | What correlations are present? | Structural |
| **Chapter 3** | Can they be protected? | Operational |
| **Chapter 4** | What if the channel has memory? | Channel-level |
| **Chapter 5** | Where does that correlated dynamics come from? | Microscopic |

The thesis therefore moves from **measurement of a resource** to **control of the resource**, then to **understanding the structure of the noise**, and finally to **identifying the physical mechanism behind the noise**.

---

## 7. What I learned from this workflow

One of the broader lessons of this research is that quantum noise should not always be viewed simply as an obstacle.

At first, the environment appears to be an adversary:

$$
\text{environment}
\rightarrow
\text{decoherence}
\rightarrow
\text{loss of correlations}.
$$

Weak-measurement control changes this picture by showing that the dynamics can be actively manipulated.

Correlated channels change it further:

$$
\text{memory}
\rightarrow
\text{modified dynamics}
\rightarrow
\text{potentially useful behavior}.
$$

Finally, microscopic open-system models show that the environment itself can participate in the generation and preservation of quantum correlations.

Thus, the goal is not always to eliminate environmental effects completely. A more useful perspective is to understand their **structure**, identify when they are detrimental, and determine when their correlations or memory can instead be exploited.

Recent work on weak-measurement protection in channels with memory similarly illustrates this idea: channel memory can improve teleportation fidelity under appropriate conditions, while weak measurement can provide an additional layer of protection.

---

## 8. The broader picture

The journey from CNEI to correlated open-system dynamics can therefore be viewed as a change in perspective.

At the beginning, the question is:

> **What is the correlation?**

Then:

> **Can I preserve it?**

Then:

> **How does memory in the channel change it?**

And finally:

> **What microscopic interaction produces that behavior?**

This is ultimately the central theme connecting the thesis:

<div class="thesis-horizontal-flow">
  <span class="step-pill">Correlation</span>
  <span class="step-arrow">→</span>
  <span class="step-pill">Protection</span>
  <span class="step-arrow">→</span>
  <span class="step-pill">Memory</span>
  <span class="step-arrow">→</span>
  <span class="step-pill">Microscopic Origin</span>
</div>

Rather than studying quantum correlations in isolation, the thesis follows them across different levels of description—from multipartite state structure, through operational quantum-information protocols, to correlated channels and finally to microscopic open-system dynamics.

That progression provides a unified way of thinking about quantum correlations: **first characterize them, then protect them, understand how memory modifies them, and finally identify the physical mechanisms responsible for their dynamics.**

---

## Selected research articles behind the thesis

For readers who want to follow the technical development, several papers provide useful entry points:

* **Weak-measurement protection:** Kim *et al.*, [“Protecting entanglement from decoherence using weak measurement and quantum measurement reversal,”](https://www.nature.com/articles/nphys2170) *Nature Physics* **8**, 117–120 (2012). The work experimentally demonstrated the use of weak measurement and reversal for entanglement protection.

* **Universal quantum teleportation and weak measurements:** Sabale, Kumar and Banerjee, [“Toward Realization of Universal Quantum Teleportation Using Weak Measurements,”](https://onlinelibrary.wiley.com/doi/10.1002/andp.202300392) *Annalen der Physik* **536**, 2300392 (2024). This work connects weak measurements, non-Markovianity, memory, teleportation fidelity, and fidelity deviation.

* **Correlated quantum channels:** Addis *et al.*, [“Dynamical Memory Effects in Correlated Quantum Channels,”](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.94.032121) *Physical Review A* **94**, 032121 (2016). This is particularly useful for understanding the distinction between channel-use correlations and dynamical non-Markovianity.

* **Correlated non-Markovian channels:** Sabale *et al.*, [“Facets of Correlated Non-Markovian Channels,”](https://onlinelibrary.wiley.com/doi/10.1002/andp.202400151) *Annalen der Physik* **536**, 2400151 (2024). The article develops the correlated-channel/non-Markovianity analysis involving unital and non-unital channels, accessible-state volume, entanglement dynamics, and error correction.

* **Microscopic correlated dynamics:** Ficek and Tanaś, work on two-atom entanglement and common-reservoir dynamics, provides the physical background for understanding collective dissipation, entanglement generation, sudden death, and sudden birth.

<style>
.thesis-flowchart-card {
  max-width: 540px;
  margin: 2.25rem auto;
  padding: 1.5rem;
  background: #ffffff;
  border: 2px solid #003687;
  border-radius: 14px;
  box-shadow: 0 6px 20px rgba(0, 54, 135, 0.08);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.65rem;
}
.flow-step {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 0.85rem 1.25rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  transition: transform 0.2s ease, border-color 0.2s ease;
}
.flow-step:hover {
  transform: translateY(-2px);
  border-color: #1495a7;
}
.flow-badge {
  font-weight: 700;
  font-size: 1.05rem;
  color: #003687;
  margin-bottom: 0.35rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.flow-question {
  font-size: 0.95rem;
  color: #334155;
  font-style: italic;
}
.flow-down-arrow {
  font-size: 1.6rem;
  font-weight: 800;
  color: #1495a7;
  line-height: 1;
}

.thesis-horizontal-flow {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin: 1.75rem 0;
  padding: 1rem 1.25rem;
  background: #f0f4fc;
  border: 1px solid #d0deee;
  border-radius: 12px;
}
.step-pill {
  background: #003687;
  color: #ffffff;
  font-weight: 600;
  font-size: 0.92rem;
  padding: 0.45rem 1rem;
  border-radius: 20px;
  display: inline-block;
  box-shadow: 0 2px 6px rgba(0, 54, 135, 0.15);
}
.step-arrow {
  color: #1495a7;
  font-weight: 800;
  font-size: 1.3rem;
}
@media (max-width: 600px) {
  .thesis-flowchart-card {
    padding: 1rem;
  }
  .thesis-horizontal-flow {
    gap: 0.4rem;
  }
  .step-pill {
    font-size: 0.8rem;
    padding: 0.35rem 0.75rem;
  }
}
</style>
