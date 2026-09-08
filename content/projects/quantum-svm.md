+++
title = "Quantum Support Vector Machines (QSVM)"
date = 2025-01-10
description = "Cross-domain classification of quantum states using quantum kernel methods and support vector machines."
[taxonomies]
tags = ["Quantum ML", "Python", "Qiskit", "PennyLane"]
[extra]
link = "https://github.com/viveksabale1998/Quantum-States-Data-Set"
paper_url = "https://link.springer.com/article/10.1007/s42484-025-00274-4"
image = "images/projects/quantum-svm.png"
image_align = "center"
+++

# Quantum Support Vector Machines for State Classification

This project investigates quantum machine learning techniques—specifically **Quantum Support Vector Machines (QSVM)**—for the cross-domain classification of multi-qubit quantum states into entangled and separable families.

<div class="project-actions" style="margin: 1.5rem 0; display: flex; gap: 12px; flex-wrap: wrap;">
  <a href="https://github.com/viveksabale1998/Quantum-States-Data-Set" target="_blank" rel="noopener noreferrer" class="c-button c-button--primary c-button--small" style="text-decoration: none;">
    <i class="ion ion-logo-github" style="margin-right: 6px;"></i> View Repository on GitHub
  </a>
  <a href="https://link.springer.com/article/10.1007/s42484-025-00274-4" target="_blank" rel="noopener noreferrer" class="c-button c-button--secondary c-button--small" style="text-decoration: none;">
    <i class="ion ion-md-document" style="margin-right: 6px;"></i> Read 2025 Paper
  </a>
</div>

## 📌 Project Highlights

- **Quantum Feature Maps**: Encodes classical and density matrix parameters into quantum state space via parameterised quantum circuits (PQCs).
- **Quantum Kernel Estimation**: Evaluates state fidelities $\mathrm{Tr}(\rho \sigma)$ on quantum simulators and noisy devices to compute quantum kernel matrices.
- **Cross-Domain Generalization**: Tests trained models across disparate quantum state families (Werner, Horodecki, MEMS, and random density matrices).
- **Benchmarking**: Rigorous comparison with classical neural networks and support vector classifiers across multiple noise channels.

## 🔬 Associated Research Publication

**Harnessing quantum support vector machines for cross-domain classification of quantum states**  
*Diksha Sharma, Vivek Balasaheb Sabale, Parvinder Singh, Amit Kumar*  
**Quantum Machine Intelligence** 7 (1), 49 (2025)  
[DOI: 10.1007/s42484-025-00274-4](https://link.springer.com/article/10.1007/s42484-025-00274-4)

## 💻 Tech Stack & Tools

- **Languages**: Python, Julia
- **Quantum Frameworks**: PennyLane, Qiskit, QuTiP
