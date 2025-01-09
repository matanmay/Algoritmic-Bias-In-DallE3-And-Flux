# Algorithmic Bias in Adjective Representation
==============================================

**Course Project**
------------------

**Title:** Unveiling Algorithmic Bias: A Comparative Study of Age, Gender, and Ethnic Bias in Adjectives using DALL-E 3 and Flux  
**Team Members:** Matan Mayerowicz & Mohamed Sayed Ahmd
**Course Name:** Algorithmic Transparency Seminar
**Academic Term:** Winter 2025 
**Institution:** University of Haifa

## Table of Contents
-----------------

1. [Project Overview](#project-overview)
2. [Methodology](#methodology)
3. [Tools and Technologies](#tools-and-technologies)
4. [Dataset](#dataset)
5. [Results and Findings](#results-and-findings)
6. [Conclusion](#conclusion)
7. [Future Work](#future-work)
8. [How to Replicate](#how-to-replicate)
9. [References](#references)

## Project Overview
-----------------

This project investigates algorithmic bias in the generation of adjectives across age, gender, and ethnicities, leveraging two text-to-image synthesis tools: **DALL-E 3** (a state-of-the-art commercial model) and **Flux** (an open-source image generation from text tool). Our analysis is driven by a curated set of promotional prompts found in `myPromo.csv`, aiming to highlight potential biases in AI-generated content.

## Methodology
--------------

1. **Prompt Engineering:** Systematically modified `myPromo.csv` prompts to represent diverse age, gender, and ethnic groups.
2. **Text-to-Image Synthesis:**
   - **DALL-E 3:** Utilized for generating images and analyzing adjectives in text descriptions.
   - **Flux (Open-Source):** Employed in parallel to DALL-E 3, allowing for a comparative analysis of bias in open-source vs. commercial models.
3. **Bias Analysis:** Quantitative and qualitative assessment of generated adjectives for biases, comparing distributions across demographic categories and models.

## Tools and Technologies
-------------------------

- **DALL-E 3:** Commercial text-to-image synthesis model.
- **Flux:** **Open-Source** image generation from text tool, facilitating comparative bias analysis.
- **`myPromo.csv`:** Custom dataset of promotional prompts, varied by demographic attributes.
- **Analysis Framework:** [Specify any additional frameworks or libraries used for bias analysis, e.g., Python, Pandas, Matplotlib]

## Dataset
----------

- **Source:** `myPromo.csv`, containing [Insert number] base prompts, each modified to represent [Insert number] demographic variations.
- **Scope:** Comprehensive coverage of age, gender, and ethnic diversity in promotional contexts.

## Results and Findings
----------------------
TBD

## Conclusion
----------

This comparative study sheds light on the presence and nuances of algorithmic bias in adjective generation across commercial (DALL-E 3) and open-source (Flux) text-to-image models. Our findings emphasize the importance of model selection, dataset diversity, and ongoing bias mitigation strategies in AI development.

## Future Work
--------------

- **Model Customization:** Explore fine-tuning Flux for reduced bias, leveraging its open-source nature.
- **Expanded Demographic Analysis:** Incorporate additional demographic attributes into the study.

## How to Replicate
------------------

1. **Clone Repository:** `git clone [this repo's URL]`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Access DALL-E 3:** Follow official guidelines for API/key setup.
4. **Utilize Flux:** Clone from [Flux's open-source repository URL], integrate as per our documented methodology.
5. **Run Analysis Pipeline:** `python main.py --prompts myPromo.csv`

## References
------------
TBD
