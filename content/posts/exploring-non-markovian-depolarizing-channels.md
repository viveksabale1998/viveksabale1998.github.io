+++
title = "Exploring Non-Markovian Dynamics in Depolarizing Maps"
date = 2026-03-08
description = "A comprehensive exploration of memory effects, CP-divisibility breakdown, and information backflow in isotropic quantum depolarizing channels, published in Physical Review A."
[taxonomies]
tags = ["open-quantum-systems", "non-markovian", "depolarizing-channel", "quantum-information", "pra"]
[extra]
image = "images/posts/exploring-non-markovian-depolarizing-channels.jpg"
+++

In the study of open quantum systems, the **depolarizing channel** is widely regarded as the prototypical benchmark noise model. Because it degrades quantum information isotropically across all three spatial Pauli directions ($X$, $Y$, and $Z$), it represents the most egalitarian—and often the most destructive—form of environmental noise in quantum processors and communication links.

Standard textbook treatments assume that noise is **Markovian** (memoryless): once quantum coherence leaks into the environment, it is lost forever. However, when quantum systems interact with structured reservoirs, high-density spin baths, or engineered photonic cavities, the bath retains memory of past interactions.

In our paper published in *Physical Review A*, we conducted an in-depth investigation into the non-Markovian dynamics of depolarizing channels:

> **Exploring the non-Markovian dynamics in depolarizing maps**  
> *A. Abu-Nada, S. Banerjee, and Vivek Balasaheb Sabale*  
> **Physical Review A** 110 (5), 052209 (2024)  
> 🔗 [Read on Physical Review A ↗](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.110.052209) | [Google Scholar ↗](https://scholar.google.com/citations?user=LdMLDdwAAAAJ&hl=en)

Here is a breakdown of the core physics, the mathematical criteria for non-Markovianity, and the operational advantages brought by information backflow.

---

## 1. From Markovian Decay to Non-Markovian Memory

An isotropic single-qubit depolarizing channel $\Phi_t$ transforms an arbitrary initial density matrix $\rho(0)$ into a mixture of the original state and the maximally mixed state $I/2$:

$$\Phi_t[\rho] = (1 - p(t)) \rho + p(t) \frac{I}{2}$$

Geometrically, this corresponds to an isotropic contraction of the **Bloch sphere** toward its origin ($r \to 0$).

Under the standard Lindblad master equation with constant decay rate $\gamma > 0$, the depolarization parameter grows monotonically:

$$p(t) = \frac{3}{4} \left( 1 - e^{-\gamma t} \right)$$

In this Markovian limit, the Bloch sphere shrinks continuously, monotonically erasing quantum information.

### The Time-Local Master Equation
In realistic structured environments, the dynamics are governed by a **time-dependent generator**:

$$\frac{d\rho(t)}{dt} = \mathcal{L}_t[\rho(t)] = \sum_{k=1}^3 \gamma_k(t) \left( \sigma_k \rho(t) \sigma_k - \rho(t) \right)$$

where $\gamma_k(t)$ are time-dependent canonical decay rates and $\sigma_k \in \{\sigma_x, \sigma_y, \sigma_z\}$.

The crucial turning point occurs when the environment has memory:
- If all $\gamma_k(t) \ge 0$ for all $t$, the intermediate propagator $\Phi_{t_2, t_1} = \Phi_{t_2} \Phi_{t_1}^{-1}$ remains a completely positive (CP) map. This is known as **CP-divisibility**.
- When the decay rates turn **temporarily negative** ($\gamma_k(t) < 0$), CP-divisibility breaks down! Negative decay rates signify that the channel is temporarily acting in reverse, returning coherence to the system.

---

## 2. Witnessing Memory via Information Backflow (BLP Measure)

How do we rigorously quantify this memory effect?

One of the most physically intuitive measures was introduced by Breuer, Laine, and Piilo (BLP). It relies on the **trace distance** $D(\rho_1, \rho_2)$ between two distinct quantum states:

$$D(\rho_1(t), \rho_2(t)) = \frac{1}{2} \text{Tr}\left[ \sqrt{(\rho_1(t) - \rho_2(t))^\dagger (\rho_1(t) - \rho_2(t))} \right]$$

Trace distance quantifies the maximal probability of distinguishing between state $\rho_1$ and state $\rho_2$ in a single measurement.

### The Contractivity Principle
Under any CP-divisible (Markovian) channel, state distinguishability can never increase:

$$\sigma(t, \rho_{1,2}) = \frac{d}{dt} D(\rho_1(t), \rho_2(t)) \le 0 \quad \forall t$$

Whenever $\sigma(t) > 0$, information that previously leaked into environmental degrees of freedom is flowing back into the system:

$$\mathcal{N}_{\text{BLP}} = \max_{\rho_{1,2}(0)} \int_{\sigma > 0} \sigma(t, \rho_{1,2}) \, dt > 0$$

In our paper, we derived analytical expressions for the trace distance under time-dependent depolarizing noise, identifying the precise temporal intervals where $\frac{d}{dt} D > 0$ produces distinct **revival peaks**.

---

## 3. Revivals in Channel Capacity

Beyond theoretical state distinguishability, does non-Markovian memory provide tangible benefits for quantum communication?

Yes! We examined how information backflow directly revives communication capacities:

1. **Entanglement-Assisted Classical Capacity ($C_{\text{ea}}$)**: Measures the rate at which classical bits can be transmitted across the quantum channel when sender and receiver share prior entanglement.
2. **Quantum Capacity ($Q$)**: Quantifies the rate of transmitting coherent quantum information.

In the Markovian regime, both capacities decay monotonically to zero. Under non-Markovian depolarizing dynamics:
- As negative decay rates kick in, both capacities experience **transient revivals**, temporarily rebounding above zero even after having decayed significantly.
- This demonstrates that non-Markovian memory can be exploited to construct synchronized transmission protocols that pulse information during periods of maximal information return.

---

## 4. Physical Realization & Reservoir Engineering

Where do such non-Markovian depolarizing channels manifest in laboratory settings?

- **Photonic Systems with Structured Spectral Densities**: Passing photons through Fabry-Pérot cavities or photonic bandgap crystals induces non-Lorentzian, structured reservoir modes that feed photon polarization states back into the optical mode.
- **Solid-State Spin Baths**: A central electron spin (e.g., in a Nitrogen-Vacancy center or quantum dot) surrounded by an interacting bath of nuclear spins experiences non-Markovian collective back-action.
- **Simulated Quantum Processors**: Modern superconducting transmon architectures (IBM Quantum, Google Sycamore) can artificially engineer time-dependent dissipative maps through auxiliary ancilla qubits and Floquet driving.

---

## Summary of Insights

| Property | Markovian Depolarizing | Non-Markovian Depolarizing (Our Work) |
| :--- | :--- | :--- |
| **Decay Rates $\gamma(t)$** | Strictly positive constant ($\gamma > 0$) | Oscillates with **negative intervals** ($\gamma(t) < 0$) |
| **CP-Divisibility** | Always CP-divisible | **CP-divisibility breakdown** |
| **Trace Distance Rate $\sigma(t)$** | $\sigma(t) \le 0$ (monotonic loss) | $\sigma(t) > 0$ (**Information Backflow**) |
| **Bloch Sphere Evolution** | Monotonically shrinks to $I/2$ | **Expands and contracts** during revival windows |
| **Channel Capacity** | Permanently degrades | Exhibits **capacity revivals** |

---

## Read the Full Article

For full mathematical derivations, plots of the decay rates, and detailed proofs of CP-divisibility bounds, explore our published paper:

* **Physical Review A**: [Phys. Rev. A 110, 052209 (2024)](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.110.052209)  
* **Google Scholar**: [Vivek Sabale's Publications](https://scholar.google.com/citations?user=LdMLDdwAAAAJ&hl=en)  
* Have questions or interested in collaborating? Check out the [Collaboration page](/collaboration) or [get in touch](/cv).
