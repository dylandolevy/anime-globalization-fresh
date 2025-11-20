# run this in your notebook or as a small script
from IPython.display import display

import pandas as pd
from pathlib import Path

p = Path("data/raw/anime.csv")
print("exists:", p.exists())
if p.exists():
    df = pd.read_csv(p, nrows=5)
    print("shape:", pd.read_csv(p).shape)
    print("columns:", df.columns.tolist())
    display(df.head())
else:
    print("Place anime.csv into data/raw/ and rerun.")
