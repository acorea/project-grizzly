from typing import List
from pandas.core.frame import DataFrame
from textblob import TextBlob
import pandas as pd

elon_df = pd.read_csv('elon.csv')

def add_tb_data(df: DataFrame, attrs: List[str]) -> DataFrame:
    def tb(tweet, _attr: str):
        _tb = TextBlob(tweet)
        return _tb.__getattribute__(_attr)
    
    for attr in attrs:
        df[attr] = df['tweet'].apply(tb, _attr=attr)

    return df

elon_df = elon_df[['id', 'tweet', 'created_at']]

def fix_time(t: str):
    suffix_est = ' Eastern Standard Time'
    suffix_edt = ' Eastern Daylight Time'
    return t.replace(suffix_edt, '').replace(suffix_est, '')

elon_df['created_at'] = elon_df['created_at'].apply(lambda x: fix_time(x))

add_attrs = ['noun_phrases', 'polarity', 'subjectivity']

elon_df = add_tb_data(elon_df, add_attrs)

elon_df.to_csv('elon_sentsubj.csv', index=False)


