library(httr)
library(twitteR)

api_key <- "[your api key]"
api_secret <- "[your api secret]"
token <- "[your token]"
token_secret <- "[your token secret]"

# search with search query and generate as datafream (divide each tweet into 16 features)
setup_twitter_oauth(api_key, api_secret, token, token_secret)
tweets <- searchTwitter("Ice-cream Mochi OR Mochi Ice-Cream OR MochiIce-cream OR #MochiIcecream", n=100, lang="en", since="2016-04-10")
tweets_df <- twListToDF(tweets)
tweets_df

# it also allows search through logitude and latitude
tweets <- searchTwitter("Ice-cream Mochi OR Mochi Ice-Cream OR MochiIce-cream OR #MochiIcecream", n=100, lang="en", geocode='34.04993,-118.24084,10mi', since="2016-04-10")
tweets_df <- twListToDF(tweets)
tweets_df
