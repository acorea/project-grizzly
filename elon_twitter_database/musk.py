import pandas as pd
from pandas.core.frame import DataFrame

import matplotlib.pyplot as plt

df: DataFrame = pd.read_csv('elon_sentsubj.csv', parse_dates=['created_at'], date_parser=pd.to_datetime)

df = df.sort_values(by='created_at')

def is_subject(subject_field, subject_set):
    subjects = set([i.lower().replace("'", '') for i in subject_field.strip('[]').split(', ')])
    check_subject = list(subject_set & subjects) != []
    if check_subject:
        return 1
    else:
        return 0
    # return check_subject

tesla_fields = set(['tesla', 'autopilot'])
btc_fields = set(['btc', 'bitcoin'])
eth_fields = set(['ethereum', 'eth'])
doge_fields = set(['dogecoin', 'doge', 'egod'])
crypto_fields = {*btc_fields, *eth_fields, *doge_fields, *['crypto', 'moon', 'currency']}

df['is_tesla'] = df['noun_phrases'].apply(func=is_subject, subject_set=tesla_fields)
df['is_crypto'] = df['noun_phrases'].apply(func=is_subject, subject_set=crypto_fields)

crypto_tweets: DataFrame = df.loc[df['is_crypto']==True]

#
# bitcoin stuff
btc = R'buttcoin\cleaned\BTCUSDT.csv'

btc_df = pd.read_csv(btc)

for col in ['Open time', 'Close time']:
    btc_df[col] = pd.to_datetime(btc_df[col], unit='ms')

btc_df = btc_df.drop(columns=['Close', 'Close time'])
#
# values in time window


# only joins to nearest btc timestamp
    # crypto_tweets.set_index('created_at', inplace=True)
    # btc_df.set_index('Open time', inplace=True)
    # td = pd.Timedelta('30 minutes')
    # joined = pd.merge_asof(crypto_tweets, btc_df, left_index=True, right_on='Open time', direction='nearest', tolerance=td)



def timedelta(ts, interval: str = '5 minutes'):
    td = pd.Timedelta(interval)

    df = btc_df.where(btc_df['Open time'].between(ts, ts+td)).dropna()

    try:
        dfmin = df['Open'].iloc[0]
        dfmax = df['Open'].iloc[-1]

        change = (dfmax - dfmin) / dfmin

        return change
    except Exception as e:
        print(e)
        print(df)
        return None

intervals = ['5 minutes', '30 minutes']

for interval in intervals:
    col = f'{interval} pct change'
    crypto_tweets[col] = crypto_tweets['created_at'].apply(func=timedelta, interval=interval)

print(crypto_tweets)

# # plt.show()

# # df.plot(x='created_at', y='is_crypto', kind='scatter')

# # plt.show()