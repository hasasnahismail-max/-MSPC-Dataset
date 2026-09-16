# Mechanical Surface & Piston Cracks Dataset (MSPC-Dataset)

## Dataset Description
- **1. Overview:** The MSPC-Dataset is a specialized computer vision dataset designed for industrial inspection, specifically focusing on the detection and classification of surface defects and structural cracks in engine pistons and mechanical components.
- **2. Data Composition:** Contains high-resolution grayscale and RGB images captured under controlled workshop lighting conditions.
- **3. Classes:**
  - `0_healthy`: Intact surfaces with standard manufacturing finishes.
  - `1_micro_crack`: Fine, hairline surface cracks caused by thermal fatigue.
  - `2_structural_fracture`: Deep structural cracks and severe mechanical failures.

## Directory Structure
mspe-dataset/
│
├── train/
│   ├── healthy/
│   ├── micro_crack/
│   └── structural_fracture/
├── test/
    ├── healthy/
    ├── micro_crack/
    └── structural_fracture/

## Dataset Curation & Preprocessing
Images undergo automated resizing to 640x640 pixels, contrast enhancement via CLAHE (Contrast Limited Adaptive Histogram Equalization), and noise reduction to simulate real-world edge-computing constraints.

## Licensing & Citation
- **License:** Creative Commons Attribution 4.0 International (CC-BY 4.0).
- **Intended Use:** For academic research, non-destructive testing (NDT), and edge-AI industrial monitoring systems.
