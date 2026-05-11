

> A mathematical optimization framework for designing a cost-efficient and resilient global MRI manufacturing supply chain.

This project was developed by **Swaraj Pradhan** and **Areen Mahich** as part of the **CHE652 course project** at Indian Institute of Technology Kanpur. The work focuses on optimizing sourcing, transportation, labor allocation, packaging, and assembly decisions in MRI machine manufacturing using Mixed Integer Linear Programming (MILP). 

---

## 📖 Project Overview

MRI manufacturing involves a highly complex supply chain with components sourced globally, strict logistics requirements, high transportation costs, and multiple operational constraints.

This project aims to build an optimization model capable of:

* Minimizing total supply chain cost
* Optimizing sourcing and transportation strategies
* Improving labor and assembly allocation
* Reducing operational inefficiencies
* Increasing resilience against disruptions and uncertainties

The optimization framework considers:

* Component sourcing
* Air and sea transportation
* Packaging decisions
* Labor and assembly costs
* Import duties and logistics overheads
* Manufacturing constraints

---

## 🧠 Problem Statement

MRI machines require several high-precision components such as:

* Superconducting magnets
* Gradient coils
* RF coils
* Amplifiers
* Imaging systems
* Safety systems

These components are sourced from multiple countries and assembled through a globally distributed supply chain.

The challenge is to determine:

* Where components should be sourced from
* Which transportation mode should be selected
* Where assembly should occur
* How labor and packaging should be allocated

while minimizing the total operational cost under real-world constraints.

---

## ⚙️ Methodology

The supply chain problem was formulated as a:

### Mixed Integer Linear Programming (MILP) Model

The model includes:

### Decision Variables

* Sourcing decisions
* Transportation mode selection
* Labor allocation
* Packaging choices
* Assembly location selection

### Constraints

* Manufacturing capacity
* Transportation limits
* Labor availability
* Procurement budget
* Shipping time constraints
* Packaging requirements

### Optimization Techniques

* Branch and Bound
* Simplex Method
* Linearization of nonlinear terms

The optimization was solved using industrial solvers including:

* Gurobi
* IBM CPLEX



---

## 🛠 Tech Stack

* Python
* Gurobi Optimizer
* IBM CPLEX
* Operations Research
* Mathematical Optimization
* Supply Chain Modeling

---

## 📊 Features

* Global sourcing optimization
* Air vs Sea transportation analysis
* Labor and assembly optimization
* Packaging cost minimization
* Sensitivity analysis
* Scenario testing
* Bottleneck analysis
* Geographic supply chain mapping
* Cost decomposition analysis

---

## 📈 Key Insights

The optimization model demonstrated:

* Reduced total supply chain cost
* Better transportation planning
* Improved sourcing strategies
* Efficient labor utilization
* Lower logistics overheads
* More resilient supply chain configurations

The study also analyzed trade-offs between:

* Cost vs delivery time
* Air vs sea freight
* Centralized vs distributed assembly
* Efficiency vs resilience



---

## 📂 Repository Structure

```text
CHE652/
│
├── Report/
│   └── MRI_Supply_Chain_Optimization_Report.pdf
│
├── Data/
│   └── Input datasets and parameters
│
├── Model/
│   └── Optimization model implementation
│
├── Results/
│   └── Solver outputs and analysis
│
├── Visualizations/
│   └── Graphs and supply chain mappings
│
└── README.md
```

---

## 🌍 Applications

This framework can be extended to:

* Medical equipment manufacturing
* Healthcare logistics
* Industrial supply chain optimization
* High-value manufacturing systems
* Smart manufacturing and Industry 4.0 applications

---

## 📚 Course Information

**Course:** CHE652
**Project Type:** Course Project
**Domain:** Supply Chain Optimization & Operations Research

👨‍💻 Authors
 
Swaraj Pradhan
Areen Mahich

 Acknowledgements

We would like to thank the instructors and mentors of CHE652 for their guidance and support throughout the project.


## 🔗Project Repository

[GitHub Repository](https://github.com/swaanu/CHE652)

