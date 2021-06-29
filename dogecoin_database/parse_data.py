import os
import pandas as pd

# Database columns
coin_header = [
    'Open Time',
    'Open',
    'High',
    'Low',
    'Close',
    'What',
    'Close Time',
    'Quote asset volume',
    'Trades',
    'Taker buy base asset volume',
    'Taker buy quote asset volume',
    'Ignore'
]
clean_columns = [0, 1, 4, 6, 8]

src_folder = 'Source'
clean_folder = 'Cleaned'

def clean_coin(coin):
    coin_source = os.path.join(coin, src_folder)
    coin_cleaned = os.path.join(coin, clean_folder)
    if not os.path.exists(coin_cleaned):
        os.mkdir(coin_cleaned)
    for file in os.listdir(coin_source):
        coin_path = os.path.join(coin_source, file)
        coin_dest = os.path.join(coin_cleaned, file)
        coin_df = pd.read_csv(coin_path, names=coin_header, index_col=False).iloc[:, clean_columns]
        coin_df.to_csv(coin_dest, index=False)

clean_coin(os.getcwd())