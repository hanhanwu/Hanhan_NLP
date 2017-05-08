library(rvest)

movie_url <- "http://www.imdb.com/search/title?count=100&release_date=2017,2017&title_type=feature"
webpage <- read_html(movie_url)

# Ranking Data - movies are sort by popularity, but the ranking is not based on the star score
## The whole class name for ranking data is: "lister-item-index unbold text-primary"
rank_data_html <- html_nodes(webpage,'.text-primary')
rank_data <- as.numeric(html_text(rank_data_html))
head(rank_data)
length(rank_data)


# Title Data
## The title text is in <a></a> under class "lister-item-header"
title_data_html <- html_nodes(webpage, '.lister-item-header a')
title_data <- html_text(title_data_html)
head(title_data)
length(title_data)


# Movie Description
## Some description is class "text-muted" under class "ratings-bar"
desp_data_html <- html_nodes(webpage, '.lister-item-header + .text-muted + .ratings-bar+ .text-muted')
desp_data <- html_text(desp_data_html)
desp_data <- gsub("\n", "", desp_data)
head(desp_data)
length(desp_data)  # 57

## Some movie has no class "ratings-bar", therefore the description can not be got from the above method
desp_data_html <- html_nodes(webpage, '.lister-item-header + .text-muted  + .text-muted')
desp_data <- html_text(desp_data_html)
desp_data <- gsub("\n", "", desp_data)
head(desp_data)
length(desp_data)   # 43

## In order to get all the descriptions in the movie ranking order, I'm using absolute xpath here
## NOTE: you can get absolution xpath, by right click the web element through Firebug, and choose "Copy XPath"
'%&%' <- function(x, y)paste0(x,y)
get_desp <- function(rk) {
  x_path <- "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[3]/div[" %&% rk %&% "]/div[3]/p[2]"
  desp_data_html <- html_node(webpage, xpath = x_path)
  desp_data <- html_text(desp_data_html)
  desp_data <- gsub("\n", "", desp_data)
  return(desp_data)
}
df <- data.frame(cbind(rank_data, title_data))
head(df)
df[, "Description"] <- as.character(df$rank_data)
df$Description <- sapply(df$Description, get_desp)
head(df)


# Runtime
'%&%' <- function(x, y)paste0(x,y)
get_runtime <- function(rk) {
  x_path <- "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[3]/div[" %&% rk %&% "]/div[3]/p[1]/span[3]"
  rt_data_html <- html_node(webpage, xpath = x_path)
  rt_data <- html_text(rt_data_html)
  rt_data <- gsub("\n", "", rt_data)
  return(rt_data)
}
df[, "Runtime"] <- as.character(df$rank_data)
df$Runtime <- sapply(df$Runtime, get_runtime)
head(df)


# Genre
'%&%' <- function(x, y)paste0(x,y)
get_genre <- function(rk) {
  x_path <- "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[3]/div[" %&% rk %&% "]/div[3]/p[1]/span[5]"
  genre_data_html <- html_node(webpage, xpath = x_path)
  genre_data <- html_text(genre_data_html)
  genre_data <- gsub("\n", "", genre_data)
  return(genre_data)
}
df[, "Genre"] <- as.character(df$rank_data)
df$Genre <- sapply(df$Genre, get_genre)
df$Genre <- gsub(" ", "", df$Genre)
df$Genre <- gsub(",.*", "", df$Genre)   # take the first genre as genre
head(df)


# Rating
'%&%' <- function(x, y)paste0(x,y)
get_rating <- function(rk) {
  x_path <- "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[3]/div[" %&% rk %&% "]/div[3]/div/div[1]/strong"
  rating_data_html <- html_node(webpage, xpath = x_path)
  rating_data <- html_text(rating_data_html)
  rating_data <- gsub("\n", "", rating_data)
  return(rating_data)
}
df[, "Rating"] <- as.character(df$rank_data)
df$Rating <- sapply(df$Rating, get_rating)
df$Rating <- as.numeric(df$Rating)
head(df)


# Votes
'%&%' <- function(x, y)paste0(x,y)
get_vote <- function(rk) {
  x_path <- "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[3]/div[" %&% rk %&% "]/div[3]/p[4]/span[2]"
  vote_data_html <- html_node(webpage, xpath = x_path)
  vote_data <- html_text(vote_data_html)
  vote_data <- gsub("\n", "", vote_data)
  return(vote_data)
}
df[, "Vote"] <- as.character(df$rank_data)
df$Vote <- sapply(df$Vote, get_vote)
df$Vote <- gsub(",", "", df$Vote)
df$Vote <- as.numeric(df$Vote)
head(df)


# Directors
'%&%' <- function(x, y)paste0(x,y)
get_director <- function(rk) {
  x_path <- "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[3]/div[" %&% rk %&% "]/div[3]/p[3]/a[1]"
  director_data_html <- html_node(webpage, xpath = x_path)
  director_data <- html_text(director_data_html)
  director_data <- gsub("\n", "", director_data)
  return(director_data)
}
df[, "Director"] <- as.character(df$rank_data)
df$Director <- sapply(df$Director, get_director)
head(df)


# Metascore
'%&%' <- function(x, y)paste0(x,y)
get_metascore <- function(rk) {
  x_path <- "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[3]/div[" %&% rk %&% "]/div[3]/div/div[3]/span"
  metascore_data_html <- html_node(webpage, xpath = x_path)
  metascore_data <- html_text(metascore_data_html)
  metascore_data <- gsub("\n", "", metascore_data)
  return(metascore_data)
}
df[, "Metascore"] <- as.character(df$rank_data)
df$Metascore <- sapply(df$Metascore, get_metascore)
df$Metascore <- gsub(" ", "", df$Metascore)
df$Metascore <- as.numeric(df$Metascore)
head(df)


# Certificates
'%&%' <- function(x, y)paste0(x,y)
get_cert <- function(rk) {
  x_path <- "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[3]/div[" %&% rk %&% "]/div[3]/p[1]/span[1]"
  cert_data_html <- html_node(webpage, xpath = x_path)
  cert_data <- html_text(cert_data_html)
  cert_data <- gsub("\n", "", cert_data)
  return(cert_data)
}
df[, "Certificate"] <- as.character(df$rank_data)
df$Certificate <- sapply(df$Certificate, get_cert)
head(df)


# Some rows, the Certificate shows Runtime while the Runtime shows the Certificate. Exchange them
df[grepl("min", df$Certificate) == T, c("Certificate", "Runtime")] <- df[grepl("min", df$Certificate) == T, c("Runtime", "Certificate")]
df$Certificate
df$Certificate <- gsub(" ", "", df$Certificate)
df$Runtime <- gsub(" ", "", df$Runtime)
df$Runtime
df$Genre[which(df$rank_data==47)]

# Some has no Runtime, but Genre is in Runtime place
df$Runtime[which(grepl("min", df$Runtime) == F)] <- NA
df$Runtime
df$Genre
df$Runtime <- gsub("min", "", df$Runtime)
df$Runtime <- as.numeric(df$Runtime)
df$Runtime


# visualization
library(ggplot2)
qplot(data = df,Runtime,fill = Genre,bins = 30)

ggplot(df,aes(x=Runtime,y=Rating))+geom_point(aes(size=Vote,col=Genre))
