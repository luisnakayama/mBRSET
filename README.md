# mBRSET: A Portable Retina Fundus Photos Benchmark Dataset for Clinical and Demographic Prediction 

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)


Welcome to the GitHub repository for mBRSET: A Portable Retina Fundus Photos Benchmark Dataset for Clinical and Demographic Prediction. This repository is dedicated to the technical validation, data analysis, quality assessment, and modeling of the m-BRSET, which is a comprehensive dataset of retinal images labeled according to demographics, anatomical parameters, quality control, and presumed diagnosis. The BRSET is a valuable resource for the ophthalmology research community and aims to reduce under-represented countries in the dataset pool used for the development of models.

## Table of Contents
- [Introduction](#introduction)
- [Dataset Description](#dataset-description)
- [Usage](#usage)
- [Data Analysis](#data-analysis)
- [Quality Assessment](#quality-assessment)
- [Modeling](#modeling)
- [Citation](#citation)
- [License](#license)

## Introduction
The Mobile Brazilian Retinal Dataset (mBRSET) presents a pioneering collection of retinal images captured via portable cameras, encompassing a diverse range of ethnic backgrounds from Itabuna, Bahia, Brazil. Comprising 5164 images from 1291 patients diagnosed with diabetes, this dataset is augmented with clinical and demographic metadata. Its significance lies in its provision as a resource for the development and validation of algorithms tailored for portable retinal cameras, which are increasingly being deployed, particularly in low and middle-income countries. By providing a dataset of retinal fundus photos captured via portable cameras, mBRSET offers an opportunity to develop and validate computer vision models for diabetic retinopathy. This resource has the potential to contribute to advancements in medical imaging and diagnostic technologies.

## Dataset Description
The m-BRSET dataset is publicly available on PhysioNet, and you can access it through the following DOI link:

- **PhysioNet:** [m-BRSET](https://www.physionet.org/content/mbrset/1.0/)

Please refer to the PhysioNet page for detailed information on the dataset structure, contents, and citation guidelines.

## Usage
To use the m-BRSET dataset and perform technical validation, data analysis, quality assessment, and modeling, you can follow these steps:

1. Clone this repository to your local machine:
```
git clone https://github.com/luisnakayama/mBRSET.git
```

2. Set up your Python environment and install the required libraries by running:

The Python version used here is `Python 3.9.7`
```
pip install -r requirements.txt
```

3. Explore the dataset and access the data for your analysis.

## Data Analysis
The data analysis for the BRSET can be found in the `eda.ipynb` notebook. It includes exploratory data analysis, plots, distributions, and an overview of the dataset. Feel free to use this notebook as a starting point for your own analysis.

## Quality Assessment
The quality assessment for the BRSET can be found in the `eda.ipynb` notebook. This section covers aspects such as missing values, data quality assessment, and the identification of duplicates. You can also generate a profiling report for further insights into the data quality.

## Modeling
To build and evaluate models using the BRSET dataset, we provide a step-by-step guide in the `Nclass_TARGET_MODEL.ipynb` and `modeling_embeddings.ipynb` notebook. These notebook demonstrates how to load the dataset, preprocess the images and labels, and train machine learning models for various tasks related to ophthalmology research.

### Pre-trained Embeddings
To facilitate the use and reduce computational costs, we offer pre-trained embeddings extracted from various backbone models. These embeddings can be extracted and used in ml tasks using the `modeling_embeddings.ipynb` file. You can find embeddings for the following backbone models:

- 'dinov2_small'
- 'dinov2_base'
- 'dinov2_large'
- 'dinov2_giant'
- 'clip_base'
- 'clip_large'
- 'convnextv2_tiny'
- 'convnextv2_base'
- 'convnextv2_large'
- 'convnext_tiny'
- 'convnext_small'
- 'convnext_base'
- 'convnext_large'
- 'swin_tiny'
- 'swin_small'
- 'swin_base'
- 'swin_v2'
- 'vit_base'
- 'vit_large'
- 'retfound'

These pre-trained embeddings can be utilized in your machine learning models to expedite the development and reduce computational overhead.


## Citation
If you use the BRSET dataset in your research, please cite the following publication:

**Physionet:** *Nakayama, L. F., Zago Ribeiro, L., Restrepo, D., Santos Barboza, N., Dias Fiterman, R., Vieira Sousa, M. l., Pereira, A. D. A., Regatieri, C., Malerbi, F. K., & Andrade, R. (2024). mBRSET, a Mobile Brazilian Retinal Dataset (version 1.0). PhysioNet. https://doi.org/10.13026/qxpd-1y65.*
