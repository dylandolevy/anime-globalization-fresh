# Anime Globalization — Data + Analysis (2010–2025)

**Short:** Analysis of how global interest in Japanese pop culture (especially anime) evolved from 2010–2025 using MyAnimeList metadata and Google Trends.

**Author:** Dylan Dole-Vy (GitHub: [@dylandolevy](https://github.com/dylandolevy))  
**Status:** Working project — cleaned environment & notebooks (see `notebooks/`)

---

## 📘 Project Overview

This project builds a reproducible pipeline to:

- Clean and preprocess MyAnimeList metadata (`anime.csv`, `rating.csv`).
- Compute yearly metrics (titles produced, average score, membership).
- Pull Google Trends for *anime* (2010–2025) and aggregate to yearly.
- Merge and visualize global interest vs output, and compute correlations.
- Provide baseline predictive models for MAL score from metadata.

Notebook-driven, reproducible with a clean virtual environment.

---

## 🧰 Reproduce Locally

### 1. Clone

```bash
git clone https://github.com/dylandolevy/anime-globalization-fresh.git
cd anime-globalization-fresh

###2. Create & Activate Environment

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3. Jupyter Kernel
bash
Copy code
python -m ipykernel install --user --name=anime-fresh --display-name "Python (anime-fresh)"
4. Place Raw Data
Put anime.csv (and rating.csv if using) into data/raw/ (not committed if large).
If you used Kaggle, keep kaggle.json at ~/.kaggle/kaggle.json.

5. Run the Notebooks
Open VS Code / Jupyter and run:

notebooks/02_cleaning_exploration.ipynb
notebooks/04_anime_modeling.ipynb
notebooks/06_trend_analysis.ipynb
The notebooks will save processed CSVs to data/processed/
and figures to outputs/figures/.

Design Decisions & Notes
Raw large files are recommended to remain outside the repo.
Use Git LFS for medium-large assets, or host raw data externally (Zenodo, Google Drive).

Notebooks are the canonical analysis; the src/ folder contains reusable helpers.

requirements.txt lists the package versions used for reproducibility.

✨ Key Findings (Summary)
Global search interest for “anime” rises sharply after 2015.

Anime production (titles per year) increases in parallel.

Strong positive correlation between production volume and search interest.

Results Overview
Global Growth of Anime (2010–2025)
Visualizing global search interest for anime (Google Trends) versus the number of anime produced each year.
Interest and production volume both rise sharply after 2015, signaling the global “anime boom.”

<p align="center"> <img src="outputs/figures/japan_culture_boom.png" alt="Global anime interest vs production (2010–2025)" width="700"> </p>
Correlation Between Output, Scores, and Global Interest
A correlation heatmap comparing yearly anime production, average scores, and worldwide search interest.

<p align="center"> <img src="outputs/figures/anime_trends_correlation.png" alt="Correlation heatmap: anime output vs global interest" width="500"> </p>
Top Genres by Volume
Top 10 genres on MyAnimeList by number of titles produced.

<p align="center"> <img src="outputs/figures/top_genres.png" alt="Top 10 anime genres" width="500"> </p>
License
This repository is distributed under the MIT License — see LICENSE (or change as desired).

Citation & Data Sources
MyAnimeList dataset (Kaggle)

Google Trends (pytrends)

Jikan API (optional) for anime metadata enrichment

yaml
Copy code

---

### ✅ Key fixes in this version:
1. Added **blank lines** between sections and code fences → GitHub Markdown renders correctly.  
2. Used **triple backticks with language hints** for code blocks.  
3. Wrapped text in consistent width and used `<p align="center">` only inside HTML blocks separated by blank lines.  
4. Added emoji section headers for clarity (works great on GitHub).  
5. Linked your username properly (`[@dylandolevy](https://github.com/dylandolevy)`).