# Anime Globalization — Data + Analysis (2010–2025)

**Short:** Analysis of how global interest in Japanese pop culture (especially anime) evolved from 2010–2025 using MyAnimeList metadata and Google Trends.

**Author:** Dylan Dole-Vy (GitHub: @dylandolevy)  
**Status:** Working project — cleaned environment & notebooks (see `notebooks/`)

---

## Project overview

This project builds a reproducible pipeline to:
- Clean and preprocess MyAnimeList metadata (`anime.csv`, `rating.csv`).
- Compute yearly metrics (titles produced, average score, membership).
- Pull Google Trends for *anime* (2010–2025) and aggregate to yearly.
- Merge and visualize global interest vs output, and compute correlations.
- Provide baseline predictive models for MAL score from metadata.

Notebook-driven, reproducible with a clean virtual environment.

---

## 🧰 Reproduce (local)

1. Clone
```bash
git clone https://github.com/<your-username>/anime-globalization-fresh.git
cd anime-globalization-fresh


2. Create & activate environment

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


3. Jupyter kernel

python -m ipykernel install --user --name=anime-fresh --display-name "Python (anime-fresh)"


4. Place raw data
Put anime.csv (and rating.csv if using) into data/raw/ (not committed if large). If you used Kaggle, keep kaggle.json at ~/.kaggle/kaggle.json.

5. Run the notebooks
Open VS Code / Jupyter and run:
notebooks/02_cleaning_exploration.ipynb
notebooks/04_anime_modeling.ipynb
notebooks/06_trend_analysis.ipynb

The notebooks will save processed CSVs to data/processed/ and figures to outputs/figures/.


Design decisions & notes
-Raw large files are recommended to remain outside the repo. Use Git LFS for medium-large assets, or host raw data externally (Zenodo, Google Drive), and link in data/README.md.
-Notebooks are the canonical analysis; the src/ folder contains reusable helpers.
-requirements.txt lists the package versions used for reproducibility.


Key findings (summary placeholder)
-Global search interest for “anime” rises sharply after 2015.
-Anime production (titles per year) increases in parallel.
-Strong positive correlation between production volume and search interest. ()

📊 Results Overview
### Global Growth of Anime (2010–2025)
Visualizing global search interest for *anime* (Google Trends) versus the number of anime produced each year.  
Interest and production volume both rise sharply after 2015, signaling the global “anime boom.”

<p align="center">
  <img src="outputs/figures/japan_culture_boom.png" alt="Global anime interest vs production (2010–2025)" width="700">
</p>

---

### Correlation Between Output, Scores, and Global Interest
A correlation heatmap comparing yearly anime production, average scores, and worldwide search interest.

<p align="center">
  <img src="outputs/figures/anime_trends_correlation.png" alt="Correlation heatmap: anime output vs global interest" width="500">
</p>

---

### Top Genres by Volume
Top 10 genres on MyAnimeList by number of titles produced.

<p align="center">
  <img src="outputs/figures/top_genres.png" alt="Top 10 anime genres" width="500">
</p>




License
This repo is distributed under the MIT License — see LICENSE (or change as desired).


Citation & data sources
-MyAnimeList dataset (Kaggle)
-Google Trends (pytrends)
-Jikan API (optional) for anime metadata enrichment