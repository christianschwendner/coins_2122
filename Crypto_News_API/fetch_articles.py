import pandas as pd
from newsapi import NewsApiClient


# console input
print("Bitte Datum im Format YYYYMMDD eingeben: ")
date = str(input())


# Init
newsapi = NewsApiClient(api_key='ff25f8ba048b4928b4db576d9a4f614b')


# method to fetch data
def news_fetcher(q="bitcoin", from_param='2021-11-05', to='2021-11-07'):
    # /v2/top-headlines
    articles = newsapi.get_everything(q=q,
                                      language='en',
                                      from_param=from_param,
                                      to=to,
                                      sort_by='relevancy')
    return articles


# fetch articles
print('fetch articels')
articles_bitcoin = news_fetcher(q="bitcoin")
articles_ethereum = news_fetcher(q="ethereum")
articles_dogecoin = news_fetcher(q="dogecoin")
articles_shibainucoin = news_fetcher(q="shiba inu coin")
articles_solana = news_fetcher(q="solana")
articles_Chainlink = news_fetcher(q="Chainlink")
articles_ethereum2 = news_fetcher(q="ethereum 2")


# expand json files
print('normalize json files')
articles_bitcoin_df = pd.json_normalize(articles_bitcoin['articles'])
articles_ethereum_df = pd.json_normalize(articles_ethereum['articles'])
articles_dogecoin_df = pd.json_normalize(articles_dogecoin['articles'])
articles_shibainucoin_df = pd.json_normalize(articles_shibainucoin['articles'])
articles_solana_df = pd.json_normalize(articles_solana['articles'])
articles_Chainlink_df = pd.json_normalize(articles_Chainlink['articles'])
articles_ethereum2_df = pd.json_normalize(articles_ethereum2['articles'])


# adding query col
articles_bitcoin_df['Query'] = "bitcoin"
articles_ethereum_df['Query'] = "ethereum"
articles_dogecoin_df['Query'] = "dogecoin"
articles_shibainucoin_df['Query'] = "shibainucoin"
articles_solana_df['Query'] = "solana"
articles_Chainlink_df['Query'] = "Chainlink"
articles_ethereum2_df['Query'] = "ethereum2"


# list of dataframes to concat
articles_list = [articles_bitcoin_df,
                articles_ethereum_df,
                articles_dogecoin_df,
                articles_shibainucoin_df,
                articles_solana_df,
                articles_Chainlink_df,
                articles_ethereum2_df]


print('concat and save dataframe')
articles_all = pd.concat(articles_list, axis=0, ignore_index=True)
print('arcitle fetched: ' + str(len(articles_all)))
articles_all.to_excel("output/" + date + "articles_all.xlsx")

print('Job finished.')
