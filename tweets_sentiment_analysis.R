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
tweets_df$text <- sapply(tweets_df$text,function(row) iconv(row, "latin1", "ASCII", sub=""))  # remove emoji
tweets_df
  
# it also allows search through logitude and latitude
tweets <- searchTwitter("Ice-cream Mochi OR Mochi Ice-Cream OR MochiIce-cream OR #MochiIcecream", n=100, lang="en", geocode='34.04993,-118.24084,10mi', since="2016-04-10")
tweets_df <- twListToDF(tweets)
tweets_df

tweet_txt  <- as.character(tweets_df$text)
tweet_txt


# sentiment analysis with syuzhet
library(syuzhet)
##let's remove people names
tweet_txt <- gsub("@\\w+","",tweet_txt)
## remove urls
tweet_txt <- gsub("http[^[:blank:]]+","",tweet_txt)
##let's remove punctuations
tweet_txt <- gsub("[[:punct:]]"," ",tweet_txt)
##let's remove number (alphanumeric)
tweet_txt <- gsub("[^[:alnum:]]"," ",tweet_txt)
## trim leading or trailing whitespace
trim <- function (x) gsub("^\\s+|\\s+$", "", x)
tweet_txt <- trim(tweet_txt)

tweet_txt

tweet_sentiment <- get_nrc_sentiment(tweet_txt)


# visualize sentiment total scores
library(ggplot2)
## Get the sentiment score for each emotion
tweet_sentiment_positive <- sum(tweet_sentiment$positive)
tweet_sentiment_anger <- sum(tweet_sentiment$anger)
tweet_sentiment_anticipation <- sum(tweet_sentiment$anticipation)
tweet_sentiment_disgust <- sum(tweet_sentiment$disgust)
tweet_sentiment_fear <- sum(tweet_sentiment$fear)
tweet_sentiment_joy <- sum(tweet_sentiment$joy)
tweet_sentiment_sadness <- sum(tweet_sentiment$sadness)
tweet_sentiment_surprise <- sum(tweet_sentiment$surprise)
tweet_sentiment_trust <- sum(tweet_sentiment$trust)
tweet_sentiment_negative <- sum(tweet_sentiment$negative)

## showing in bar chart
yAxis <- c(tweet_sentiment_positive,
           tweet_sentiment_anger,
           tweet_sentiment_anticipation,
           tweet_sentiment_disgust,
           tweet_sentiment_fear,
           tweet_sentiment_joy,
           tweet_sentiment_sadness,
           tweet_sentiment_surprise,
           tweet_sentiment_trust,
           tweet_sentiment_negative)

xAxis <- c("Positive","Anger","Anticipation","Disgust","Fear","Joy","Sadness","Surprise","Trust","Negative")
colors <- c("green","red","blue","orange","black","pink","yellow","maroon","grey","cyan1")
yRange <- range(0,yAxis)
barplot(yAxis, names.arg = xAxis, 
        xlab = "Emotional valence", ylab = "Score", main = "Twitter Sentiment for Ice-cream Mochi!", col = colors, border = "black", ylim = yRange, xpd = F, axisnames = T, cex.axis = 0.8, cex.sub = 0.8)
colSums(tweet_sentiment)

