# RecB DNA binding article

This repository contains the latex files, data and Python scripts used in the article:
Thédié D., Lepore A., McLaren L, El Karoui, M. (2024). (Insert title here) bioRxiv. DOI: (Insert DOI here)

## Data storage
The [Dataset list](./Dataset_list.csv) table lists all datasets used in this study, with a unique identifier ("Name"), and other basic information (ciprofloxacin concentration, strain used, overexpressed proteins...). Dataset names can be used to find:
- Raw images on (link to be added)
- Processed BACMMAN datasets (see the [BACMMAN datasets](./BACMMAN_datasets/) folder)

## Steps to reproduce the analysis workflow
1. Clone this repository to your computer
    - If you do not wish to re-process the images in BACMMAN, skip to step 5.
2. Download the raw images from (update when available)
3. Install the [BACMMAN Fiji plugin](https://github.com/jeanollion/bacmman/wiki)
4. Open the BACMMAN plugin in Fiji
    - Set the `BACMMAN_datasets` folder of this repository as working directory
    - Open the dataset of interest (refer to [Dataset_list](./Dataset_list.csv) for more details)
    - Run Pre-processing, Processing, Measurements and Extract Measurements
5. Open a Jupyter Notebook from the [Notebooks](./Notebooks/) folder
    - If you have not already, install the [PyBerries package](https://gitlab.com/MEKlab/pyberries) and its dependencies
    - Run the cells of the Notebook to generate Figures (the code does not need to be updated)
