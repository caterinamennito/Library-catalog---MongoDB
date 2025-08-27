import pandas as pd
import numpy as np
import ast
import json

df = pd.read_csv('books.csv')

def fix_string_of_array(val):
    try:
        genres = ast.literal_eval(val)
        if isinstance(genres, list):
            return genres
        return [val]
    except Exception:
        return [val]

df['genres'] = df['genres'].apply(fix_string_of_array)
df['characters'] = df['characters'].apply(fix_string_of_array)
df['awards'] = df['awards'].apply(fix_string_of_array)
df['ratingsByStars'] = df['ratingsByStars'].apply(fix_string_of_array)
df['setting'] = df['setting'].apply(fix_string_of_array)

df = df.replace([np.nan, 'NaN', None, np.inf, -np.inf], None)

records = df.to_dict(orient='records')
with open('books_cleaned.json', 'w') as f:
    json.dump(records, f, indent=2)