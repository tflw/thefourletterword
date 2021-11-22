import pandas as pd 
import pickle as pkl
from nltk.corpus import stopwords


file = 'dataset_en_basic.xlsx'
df = pd.read_excel(file)

for column in df.columns:
    df [column] = df[column].str.replace(r'\W', " ")
    df [column] = df[column].str.replace('user', "")


stop = (stopwords.words('english'))


pat = r'\b(?:{})\b'.format('|'.join(stop))
df["basic_clean_text"] = df["basic_clean_text"].str.replace(pat, '')
df["basic_clean_text"] = df["basic_clean_text"].str.replace(r'\s+', ' ')

df.to_csv(".\cleanfinal.csv")


    
