# Awesome BAMresearch [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of repositories, tools, and projects maintained by the BAMresearch organization researchers.
The repositories are listed according to the overarching topic and sorted with respect to their field of application.
This list is updated once every month to record new developments at BAM. 

# List of repositories ordered by application

## 1. Digital Infrastructure & Research Data
Foundation layer providing data storage, management, interoperability, and FAIR access.
### Research Data Management & openBIS
- [bam-masterdata](https://github.com/BAMresearch/bam-masterdata) – Repository containing the masterdata definitions of the BAM Data Store project.
- [chatBIS](https://github.com/BAMresearch/chatBIS) – A conversational AI assistant for the openBIS research data management system. Uses RAG with Ollama to provide natural, accurate responses to queries about openBIS. Scrapes documentation, processes it into semantic chunks, and delivers helpful answers through a simple command-line interface.
- [pyrxiv](https://github.com/BAMresearch/pyrxiv) – A Python package for retrieving arXiv papers and filter them out with respect to some specific regex pattern.
### Ontologies & Semantic Infrastructure
- [Wet-Chemical Syntheses Ontology](https://github.com/BAMresearch/wcso) - Wet-Chemical Syntheses (WeChemSyn) Ontology (WCSO) provides a semantic framework for the structured representation of knowledge related to the production of (nano)particles by wet chemical synthesis.
- [LebeDigital](https://github.com/BAMresearch/LebeDigital) – The LeBeDigital Concrete Production and Testing Ontology - CPTO Repository.
### FAIR Research Infrastructure
- [NFDI4IngModelValidationPlatform](https://github.com/BAMresearch/NFDI4IngModelValidationPlatform) – A collection of benchmarks and methdology for provenance tracking for the validation of simulation models.
- [NFDI4IngScientificWorkflowRequirements](https://github.com/BAMresearch/NFDI4IngScientificWorkflowRequirements) – This is a repository to discuss, collect and store the requirements for scientific workflow systems
## 2. Scientific Workflow Systems
Software that orchestrates, documents, and automates scientific processes.
### General Workflow Frameworks
- [probeye](https://github.com/BAMresearch/probeye) – A general framework for setting up parameter estimation problems.
- [bayem](https://github.com/BAMresearch/bayem) – Implementation and derivation of "Variational Bayesian inference for a nonlinear forward model" for arbitrary, user-defined model errors.
- [fenics-constitutive](https://fenics-constitutive.readthedocs.io/en/latest/) – Complex constitutive models beyond the FEniCS UFL.
### Domain-Specific Workflow Engines
- [PepGM](https://github.com/BAMresearch/PepGM) - A probabilistic graphical model for taxonomic inference of viral proteome samples with associated confidence scores.
## 3. Computational Materials Chemistry & Materials Acceleration Platforms (MAPs)
Repositories focused on understanding and designing materials through atomic-scale modeling and automated laboratories.
### Bonding & Electronic Structure
- [LobsterPy](https://github.com/DigiMatChem/LobsterPy) – Package to automatically analyze Lobster runs.
### Machine-Learned Physical Models
- [autoplex](https://github.com/autoatml/autoplex) – Software for generating and benchmarking machine learning (ML) based interatomic potentials.
- [equitrain](https://github.com/BAMresearch/equitrain) - Equitrain is an open-source software package designed to simplify the training and fine-tuning of machine learning universal interatomic potentials (MLIPs).
### Materials Discovery
- [TransportNoveltyDistance](https://github.com/BAMeScience/TransportNoveltyDistance) - Metric for evaluating GenAI-Models for materials.
### Synthesis Prediction
- [SynCoTrainMP](https://github.com/BAMresearch/SynCoTrainMP) - Co-Training for Crystal Synthesizability Prediction.
### Structure–Property Learning
- [HEMPs-proton-conductivity](https://github.com/BAMresearch/HEMPs-proton-conductivity) – Statistical and empirical data analysis pipelines used to evaluate the structure-property relationships within High-Entropy Metal Phosphates (HEMPs).
### Autonomous Discovery
- [MAPs at BAM](https://github.com/BAMresearch/MAPz_at_BAM) - Materials Acceleration Platform Center at BAM.
- [WEBSLAMD](https://github.com/BAMresearch/WEBSLAMD) – Sequential Learning App for Materials Discovery ("SLAMD") - Web Version.
## 4. Scientific Analysis Libraries
Reusable scientific software components for data evaluation and interpretation.
### Scattering & Diffraction
- [MoDaCor](https://github.com/BAMresearch/MoDaCor) – new modular data corrections for any neutron or xray technique that produces 1D or 2D scattering/diffraction/imaging data.
- [McSAS3](https://github.com/BAMresearch/McSAS3) – Refactored McSAS for analysis of X-ray and neutron scattering data.
- [SasModelsExplorer](https://github.com/BAMresearch/SasModelsExplorer) - A PyQt-based interactive application to explore scattering models
- [SAXS workflow](https://github.com/BAMresearch/saxs_publication_project) - BESSY II µSpot in-situ flow-through SAXS data reduction pipeline, analytical uncertainty propagation, and publication dataset.
- [caco3-thin-films](https://github.com/BAMresearch/caco3-thin-films) – Crystallographic characterisation and analysis of CaCO3 thin films.
- [ZrV2O7-PDF-Refinement](https://github.com/BAMresearch/ZrV2O7-PDF-Refinement) - Python scripts specifically developed for structural refinement of Zirconium Vanadate (ZrV₂O₇).
### Spectroscopy
- [SOFA](https://bamresearch.github.io/SOFA/build/html/index.html) – SOftware for Force Analysis - Analyze Atomic Force Microscopy Force Spectroscopy data.
- [SyFoS](https://bamresearch.github.io/SyFoS/build/html/index.html) – Synthetic Force Spectroscopy.
- [HavNegpy](https://havnegpy.readthedocs.io/en/latest/index.html) – HavNegpy is a python fit package to anaylze dielectric spectroscopy data. HavNeg is an acronym for Havriliak and Negami function, and the fit module is written specifically to analyze the dielectric loss and real part of AC conductivity data.
- [ANNforPAT](https://github.com/BAMresearch/ANNforPAT) – This code accompanies the paper "Artificial neural networks for quantitative online NMR spectroscopy" ([https://doi.org/10.1007/s00216-020-02687-5](https://doi.org/10.1007/s00216-020-02687-5))
- [EISnet](https://github.com/BAMresearch/EISNet) - Code for model to Machine Learning-Assisted Equivalent Circuit Identification for Dielectric Spectroscopy of Polymers [https://doi.org/10.1016/j.electacta.2024.144474](https://doi.org/10.1016/j.electacta.2024.144474).
### Mass Spectrometry
- [Mistle](https://github.com/BAMeScience/Mistle) - Mistle is a fast spectral search engine. It uses a fragment-indexing technique and SIMD intrinsics to match experimental MS2 spectra to large spectral libraries at a high performance.
- [fiora](https://github.com/BAMeScience/fiora) - An in silico fragmentation algorithm designed to predict tandem mass spectra (MS/MS) with high accuracy. Using graph neural networks, FIORA models bond cleavages, fragment intensities, and estimates retention times (RT) and collision cross sections (CCS).
- [MALDI-peak identifier](https://github.com/BAMresearch/MALDI-peaks) –  This tool is designed for the rapid identification of polymer repeat units and end-groups in MALDI-TOF mass spectra.
### Microscopy & Imaging
- [DF-TEM-PAW](https://github.com/BAMresearch/DF-TEM-PAW) – This repository contains the necessary sources and scripts to conduct automated precipitate analysis as demonstrated in [10.1007/s40192-023-00331-5]
- [ctsimu-toolbox](https://github.com/BAMresearch/ctsimu-toolbox) – CTSimU Software Toolbox.
- [PassiveSmartDust](https://github.com/BAMresearch/PassiveSmartDust) – An adjustable image segmentation filter, combined with data procession used in the PSD project.
- [automatic-sem-image-segmentation](https://github.com/BAMresearch/automatic-sem-image-segmentation) – Workflow for Simulation and Automatic Semantic Segmentation of Electron Microscopy Images.
- [Roughness-Analysis-by-Electron-Microscopy](https://github.com/BAMresearch/Roughness-Analysis-by-Electron-Microscopy) – Roughness analysis approach by electron microscopy for spherical microparticles.
## 5. Digital Twins & Virtual Experiments
Virtual representations of materials, structures, and processes.
### Digital Twins
- [NibelungenbrueckeDemonstrator](https://github.com/BAMresearch/NibelungenbrueckeDemonstrator) – Provides a representative and repeatable workflow for the implementation of a stochastic Digital Twin (DT) of the Nibelungenbrücke in Worms (Germany).
- [SpecTwin](https://github.com/cakirtufan/SpecTwin) - Modular Python application for X-ray Emission spectroscopy workflows.
### Physics-Based Simulation
- [aRTist-handbook](https://bamresearch.github.io/aRTist-PythonLib/) – The radiographic simulator aRTist.
## 6. Application Demonstrators
Software developed for specific application domains and demonstrator projects.
### Energy Systems
- [bam-hpt-analysis-webapp](https://github.com/BAMresearch/bam-hpt-analysis-webapp) - Heat-pump data analysis WebApp.
- [bam-load-based-testing](https://github.com/BAMresearch/bam-load-based-testing) - Two-mass building model for load-based testing of heat pumps. The model is used to define the inertial behavior of the heat sink.
### Fire Safety
- [Fire_Propagation](https://github.com/BAMresearch/Fire_Propagation) – Code base for the creation of a fire propagation dataset by combining burned area shapefiles and active fire detections.
- [wildfire_prop_database](https://github.com/BAMresearch/wildfire_prop_database) – Example for merging swath paths into a single scene and extracting a burned area polygon from the resulting image. 
### Non-Destructive Testing
- [PyParSeis](https://github.com/BAMresearch/PyParSeis) - Python code for Parallel Seismic test valuation (determination of foundation depth).
- [gnss-visual-inter-robot-tracking](https://github.com/BAMresearch/gnss-visual-inter-robot-tracking) – Software repository for GNSS/visual inter-robot tracking associated with [this paper](https://github.com/BAMresearch/gnss-visual-inter-robot-tracking/blob/main/Lohrke_Sensors_2025_accepted_repo_copyright_notice.pdf)
- [WavenumberAnalysis](https://github.com/BAMresearch/WavenumberAnalysis) – This project allows to perform wavenumber mapping using Matlab.
- [virtual-gas-camera](https://github.com/BAMresearch/virtual-gas-camera) – Software repository for the so-called 'virtual gas camera' associated with the paper 'Robotic Scanning Absorption Spectroscopy for Methane Leak Detection: the Virtual Gas Camera'.
- [SRGDM](https://github.com/BAMresearch/SRGDM) – Super-Resolution for Gas Distribution Mapping.
### Reference Materials & Certification
- [RefMat-BAM-N010-PP-analysis](https://github.com/BAMresearch/RefMat-BAM-N010-PP-analysis) - Code for analyzing measurements of N010 reference material candidate (Polypropylene Nanoparticles).
- [pyNanoRMcert_tools](https://github.com/BAMresearch/pyNanoRMcert_tools) - Numerical routines for nano reference material certification statistics calculations.
- [b-least-analysis](https://github.com/BAMresearch/b-least-analysis) – Calibration tool for measurement data with ISO 6143-based model fitting and uncertainty estimation.

## License

This list is licensed under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license.
