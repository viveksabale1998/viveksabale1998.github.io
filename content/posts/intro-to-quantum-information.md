+++
title = "Foundations of Quantum Information: From Qubits and Superposition to Density Matrices"
date = 2026-03-09
description = "An educational guide to the mathematical foundations of quantum information: pure states, the geometry of the Bloch sphere, and density operators."
[taxonomies]
tags = ["educational", "quantum-computing", "density-matrices", "qubits", "quantum-mechanics"]
[extra]
category = "Quantum Information Educational"
image = "images/posts/intro-to-quantum-information.jpg"
+++

Quantum information science combines quantum mechanics with computer science and information theory. While classical computation encodes information into binary bits ($0$ or $1$), quantum systems operate in complex Hilbert spaces, unlocking phenomena like superposition, entanglement, and interference.

This article provides a pedagogical introduction to the core mathematical language of quantum information.

---

## 1. What is a Qubit?

A **qubit** (quantum bit) is the fundamental unit of quantum information. Unlike a classical bit, a qubit can exist in a linear combination—or **superposition**—of its computational basis states $\{|0\rangle, |1\rangle\}$:

$$|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$$

where $\alpha, \beta \in \mathbb{C}$ are complex probability amplitudes satisfying the normalization constraint:

$$|\alpha|^2 + |\beta|^2 = 1$$

When a projective measurement is performed in the standard basis:
- The probability of obtaining outcome $0$ is $P(0) = |\alpha|^2$.
- The probability of obtaining outcome $1$ is $P(1) = |\beta|^2$.

---

## 2. Geometric Representation: The Bloch Sphere

Because global phase is physically unobservable ($e^{i\gamma}|\psi\rangle \sim |\psi\rangle$), any pure single-qubit state can be uniquely parameterized by two real angles $\theta \in [0, \pi]$ and $\phi \in [0, 2\pi)$:

$$|\psi\rangle = \cos\left(\frac{\theta}{2}\right) |0\rangle + e^{i\phi} \sin\left(\frac{\theta}{2}\right) |1\rangle$$

This establishes a 1-to-1 mapping between pure single-qubit states and points on the surface of a unit sphere in $\mathbb{R}^3$, known as the **Bloch Sphere**:

- **North Pole** ($\theta = 0$): $|0\rangle$
- **South Pole** ($\theta = \pi$): $|1\rangle$
- **Equator** ($\theta = \pi/2$): Superpositions such as:
  $$|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \quad |-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}, \quad |+i\rangle = \frac{|0\rangle + i|1\rangle}{\sqrt{2}}$$

Any single-qubit unitary gate corresponds to a 3D rotation of the state vector on this sphere!

---

## 3. Pure States vs. Mixed States

In idealized closed quantum systems, states are described by state vectors $|\psi\rangle$ (pure states). However, in the real world:
1. Systems interact with noisy environments (decoherence).
2. We may only possess statistical knowledge about which quantum state was prepared.

Such states cannot be written as a single ket $|\psi\rangle$. Instead, they form a **statistical ensemble**:

$$\{\left(p_i, |\psi_i\rangle\right)\}, \quad \text{where } p_i \ge 0 \text{ and } \sum_i p_i = 1$$

This leads directly to the **Density Matrix Formalism**.

---

## 4. The Density Operator Formalism

The density operator $\rho$ representing a quantum ensemble is defined as:

$$\rho = \sum_i p_i |\psi_i\rangle \langle \psi_i|$$

### Essential Properties of Density Matrices
1. **Hermiticity**: $\rho^\dagger = \rho$ (observable probabilities are real).
2. **Unit Trace**: $\text{Tr}(\rho) = 1$ (total probability equals 1).
3. **Positive Semi-definiteness**: $\rho \ge 0$ (all eigenvalues $\lambda_i \ge 0$).

### Purity Criterion
To distinguish whether a quantum state $\rho$ is pure or mixed, we compute its **purity** $\gamma$:

$$\gamma = \text{Tr}(\rho^2)$$

- **Pure state**: $\text{Tr}(\rho^2) = 1$ (the state lies on the **surface** of the Bloch sphere, radius $r = 1$).
- **Mixed state**: $\text{Tr}(\rho^2) < 1$ (the state lies in the **interior** of the Bloch sphere, radius $r < 1$).
- **Maximally mixed state**: $\rho = \frac{I}{2}$ with $\text{Tr}(\rho^2) = \frac{1}{2}$ (the exact **center** of the sphere, $r = 0$, representing complete ignorance).

---

## 5. Connecting to Open Quantum Systems & QML

Understanding density matrices is the indispensable bridge to advanced topics in modern research:
- **Open Quantum Systems**: Environmental interactions transform pure states into mixed states via dynamical maps $\rho(t) = \mathcal{E}_t[\rho(0)]$.
- **Quantum Machine Learning**: Quantum classifiers and neural networks operate directly on density matrices to distinguish entangled from separable mixtures without requiring full quantum state tomography.

---

## Summary Cheat-Sheet

| Concept | Pure State | Mixed State |
| :--- | :--- | :--- |
| **Mathematical Object** | State vector $|\psi\rangle$ | Density operator $\rho = \sum p_i |\psi_i\rangle\langle\psi_i|$ |
| **Bloch Sphere Location** | Surface ($r = 1$) | Interior ($0 \le r < 1$) |
| **Purity $\text{Tr}(\rho^2)$** | Exactly $1$ | Less than $1$ (down to $1/d$) |
| **Entropy $S(\rho)$** | $0$ (zero classical uncertainty) | $> 0$ (statistical mixedness) |

For more hands-on practice, check out our [Quantum Computing Lab Notebooks](/projects/quantum-computing-lab) or read our research posts on [Non-Markovian Dynamics](/posts/exploring-non-markovian-depolarizing-channels) and [Quantum Machine Learning](/posts/qml-quantum-state-classification).
