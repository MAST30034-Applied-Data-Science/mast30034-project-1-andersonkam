# MAST30034 Project 1 README.md
- Name: Un Leng Kam
- Student ID: 1178863

**Research Goal:** My research goal is predict high value trips given a location and time.

**Timeline:** The timeline for the research area is 2016 January to 2017 May.

## Dataset
**TLC trip record data:**  https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page \n
**New York City Weather:** https://www.visualcrossing.com/weather/weather-data-services

To run the pipeline, please visit the `scripts` directory and run the files in order:
1. `download.py`: This downloads the raw data into the `data/raw` directory.
2. `preprocess.ipynb`: This notebook details all preprocessing steps and outputs it to the `data/curated` directory.
3. `analysis.ipynb`: This notebook is used to conduct analysis on the curated data.
4. `model.py` and `model_analysis.ipynb`: The script is used to run the model from CLI and the notebook is used for analysing and discussing the model.
