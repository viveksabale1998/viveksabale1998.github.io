+++
title = "Decoherence, Protection, and Machine Learning: The Four Pillars of My PhD Research"
date = 2026-03-01
description = "A deep dive into my PhD thesis workflow connecting four core publications: from non-Markovian open quantum dynamics and correlated noise to error mitigation and quantum machine learning."
[taxonomies]
tags = ["thesis", "open-quantum-systems", "non-markovian", "teleportation", "qml"]
[extra]
image = "images/posts/thesis-workflow.jpg"
+++

Quantum technologies—ranging from scalable quantum computing to distributed quantum communication networks—promise exponential speedups over classical computing. However, their primary obstacle remains **decoherence**: the inevitable, noisy interaction between fragile quantum systems and their surrounding thermal environments.

My doctoral research addresses this fundamental challenge through an integrated, four-stage workflow:

1. **Characterize**: Diagnosing memory effects and information backflow in open quantum systems.
2. **Correlate**: Uncovering how structured multi-qubit correlated environments influence coherence.
3. **Protect**: Designing active quantum error mitigation schemes using weak measurements to preserve protocols like quantum teleportation.
4. **Classify & Benchmark**: Leveraging Quantum Machine Learning (QML) to classify complex quantum states across domains without exponential measurement overhead.

Here is the narrative of how these four investigations connect into a cohesive scientific journey.

---

## 1. Exploring Non-Markovian Dynamics in Depolarizing Maps

The conventional description of open quantum systems relies on the **Markovian approximation** (the Lindblad master equation), assuming that the environment has zero memory and continuously absorbs information from the system. In realistic solid-state architectures, superconducting qubits, and cavity QED systems, however, environmental memory effects cannot be ignored.

In our work published in *Physical Review A*, we investigated non-Markovian dynamics under depolarizing noise channels:

> **Exploring the non-Markovian dynamics in depolarizing maps**  
> *A. Abu-Nada, S. Banerjee, and Vivek Balasaheb Sabale*  
> **Physical Review A** 110 (5), 052209 (2024) — [Read on Physical Review A ↗](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.110.052209)

### Key Contributions & Insights
- **CP-Divisibility Breakdown**: We analyzed the transition from completely positive divisible (CP-divisible) dynamics to non-Markovian regimes where decay rates turn temporarily negative.
- **Information Backflow**: By tracking the Breuer-Laine-Piilo (BLP) trace distance witness, we demonstrated that non-Markovian reservoirs act as temporary information reservoirs, returning quantum distinguishability and coherence back into the qubit system.
- **Channel Capacity Revivals**: Memory effects enable transient revivals in quantum communication capacities, proving that noise memory can be harnessed rather than merely endured.

---

## 2. Facets of Correlated Non-Markovian Channels

While single-qubit open systems provide fundamental insights, practical quantum processors involve multi-qubit registers interacting with shared baths. In such multi-qubit systems, spatial and temporal correlations in the environment create collective noise effects that differ drastically from independent local noise.

In our study published in *Annalen der Physik*, we investigated the behavior of correlated non-Markovian channels:

> **Facets of Correlated Non‐Markovian Channels**  
> *Vivek Balasaheb Sabale, N. R. Dash, A. Kumar, and S. Banerjee*  
> **Annalen der Physik** 536 (10), 2400151 (2024) — [Read on Annalen der Physik ↗](https://onlinelibrary.wiley.com/doi/10.1002/andp.202400151)

### Key Contributions & Insights
- **Cross-Talk & Environmental Memory**: We modeled multi-qubit systems undergoing correlated non-Markovian dynamics, analyzing how environmental correlation parameters interact with reservoir memory times.
- **Entanglement Preservation**: We identified sub-spaces and correlation regimes where environmental correlations shield multi-qubit entanglement against sudden death, slowing down decoherence rates compared to uncorrelated baths.
- **Quantum Correlation Metrics**: We quantified quantum discord, concurrence, and coherence measures, demonstrating how spatial correlations determine the boundary between destructive and constructive noise interference.

---

## 3. Active Protection: Universal Quantum Teleportation via Weak Measurements

Characterizing noise is essential, but protecting quantum information processing tasks is the ultimate engineering goal. Quantum teleportation is the foundational primitive for quantum repeaters and distributed quantum computing, yet amplitude damping (energy dissipation) readily destroys the shared entanglement between sender and receiver.

To overcome this, we developed a measurement-based error mitigation strategy published in *Annalen der Physik*:

> **Toward realization of universal quantum teleportation using weak measurements**  
> *Vivek Balasaheb Sabale, A. Kumar, and S. Banerjee*  
> **Annalen der Physik** 536 (4), 2300392 (2024) — [Read on Annalen der Physik ↗](https://onlinelibrary.wiley.com/doi/10.1002/andp.202300392)

### The Weak Measurement Protection Protocol
1. **Pre-measurement (Weak Measurement)**: Prior to sending an entangled qubit through a lossy channel, a weak non-unitary measurement gently nudges the state towards the ground state $|0\rangle$, which is invariant under amplitude damping.
2. **Channel Traversal**: Because the qubit spends less time in the excited state $|1\rangle$, photon loss probability is heavily suppressed.
3. **Quantum Measurement Reversal (QMR)**: Upon exiting the noisy channel, a post-measurement operation undoes the pre-measurement deformation, restoring the original high-fidelity entangled Bell pair.

### Crucial Breakthrough
- Standard weak measurement protocols often depend on knowing the input state beforehand. Our work established a **universal scheme**: regardless of the arbitrary input qubit state $|\psi_{\text{in}}\rangle$, the average teleportation fidelity can be systematically maintained above the classical threshold of $2/3$, even under strong dissipation.

---

## 4. Cross-Domain Quantum Machine Learning for Quantum State Classification

As quantum circuits grow in depth and qubit count, validating state fidelity and classifying states (e.g., distinguishing separable from entangled states, or identifying noise signatures) becomes intractable. **Full Quantum State Tomography (QST)** requires $4^N - 1$ expectation values, scaling exponentially with qubit count $N$.

In our article published in *Quantum Machine Intelligence*, we demonstrated how **Quantum Support Vector Machines (QSVM)** can bypass full tomography by performing cross-domain state classification:

> **Harnessing quantum support vector machines for cross-domain classification of quantum states**  
> *D. Sharma, Vivek Balasaheb Sabale, P. Singh, and A. Kumar*  
> **Quantum Machine Intelligence** 7 (1), 49 (2025) — [Read on Springer ↗](https://link.springer.com/article/10.1007/s42484-025-00274-4)

### Key Contributions & Insights
- **Quantum Kernel Hilbert Space**: We utilized parameterized quantum circuits to map quantum density matrices into high-dimensional Hilbert spaces, computing inner products via quantum fidelity kernels $|\langle \phi(x_i) | \phi(x_j) \rangle|^2$.
- **Cross-Domain Generalization**: We trained classifiers in one domain (e.g., Werner or Bell states under specific noise levels) and demonstrated that the quantum model accurately generalizes across unseen noise parameters and mixing ratios.
- **Entanglement vs. Separability Boundary**: The QSVM successfully identified the entanglement threshold without reconstructing the density matrix, offering a scalable diagnostic tool for experimental quantum devices.

---

## Summary of the PhD Thesis Workflow

| Stage | Research Focus | Primary Publication | Key Takeaway |
| :--- | :--- | :--- | :--- |
| **Stage 1: Open Dynamics** | Non-Markovian depolarizing maps | *Phys. Rev. A* 110, 052209 (2024) | Environmental memory enables information backflow and capacity revivals. |
| **Stage 2: Correlated Noise** | Multi-qubit correlated reservoirs | *Ann. Phys.* 536, 2400151 (2024) | Spatial correlations can protect entanglement against sudden death. |
| **Stage 3: Mitigation** | Universal teleportation via weak measurements | *Ann. Phys.* 536, 2300392 (2024) | Weak pre/post measurements beat classical limits for all arbitrary input states. |
| **Stage 4: AI & QML** | QSVM for state classification | *Quantum Mach. Intell.* 7, 49 (2025) | Quantum kernel methods classify states across noise domains without full tomography. |

---

## Looking Forward

By progressing from the mathematical foundations of open quantum systems to active error mitigation and machine learning-driven state classification, this research bridges the gap between theoretical quantum information and near-term quantum hardware diagnostics. 

If you are interested in collaborating or discussing any of these publications, feel free to [get in touch](/cv) or explore my full list of works on [Google Scholar](https://scholar.google.com/citations?user=LdMLDdwAAAAJ&hl=en).
