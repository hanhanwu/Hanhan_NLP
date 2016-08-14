## INSTALL R TEXT MINING PACKAGE
Needed <- c("tm", "SnowballCC", "RColorBrewer", "ggplot2", "wordcloud", "biclust", "cluster", "igraph", "fpc")   
install.packages(Needed, dependencies=TRUE) 
install.packages("Rcampdf", repos = "http://datacube.wu.ac.at/", type = "source") 


## LOAD DATA
path<- "[your text file directory path]"
library(tm)   
docs <- Corpus(DirSource(path))   
summary(docs)
inspect(docs[1])  # inspect one of the docs


## TEXT PREPROCESSING
docs <- tm_map(docs, removePunctuation)

# when you want to remove special characters in the txts, specialize them here
for(j in seq(docs))   
{   
  docs[[j]] <- gsub("/", " ", docs[[j]])   
  docs[[j]] <- gsub("@", " ", docs[[j]])   
  docs[[j]] <- gsub("\\|", " ", docs[[j]])   
}

docs <- tm_map(docs, removeNumbers)  
docs <- tm_map(docs, tolower)
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removeWords, c("attachment", "attached"))  # remove specified stop words

# combine words that should stay together and convert them to standard format
for (j in seq(docs))
{
  docs[[j]] <- gsub("credit line", "LOC", docs[[j]])
  docs[[j]] <- gsub("credit line", "LOC", docs[[j]])
  docs[[j]] <- gsub("line of credit", "LOC", docs[[j]])
  docs[[j]] <- gsub("vancity", "Vancity", docs[[j]])
}

# stemming and strip unnecessary white space created by stemming
## the stemming here is not as powerful as python nltk stemming
library(SnowballC)   
docs <- tm_map(docs, stemDocument) 
docs <- tm_map(docs, stripWhitespace)

# this is the necessary end for text preprocessing in R, by telling it to treat your data as plain text
docs <- tm_map(docs, PlainTextDocument) 


## DOCUMENT TERM MATRIX
dtm <- DocumentTermMatrix(docs)   
dtm
tdm <- TermDocumentMatrix(docs)   # transpose of dtm
tdm 

## DATA EXPLORATION
sorted_dtm <- t(apply(as.matrix(dtm),1,sort))  # sort terms by frequency

# remove sparse terms if there is any
sparse_dtm <- removeSparseTerms(dtm, 0.1)  # make a matrix 10% empty space
inspect(sparse_dtm)
sparse_dtm

freq <- colSums(as.matrix(dtm))   
length(freq)
ord <- order(freq) 
freq[head(ord)]    # least frequent words
freq[tail(ord)]    # most frequent words
# best way to find most frequent and least frequent words
freq <- sort(colSums(as.matrix(dtm)), decreasing=TRUE)   
head(freq, 20)
tail(freq, 20)

# word term correlations - doesnt' work well
findAssocs(dtm, c("property", "mortgage"), corlimit=0.5)

# word cloud - I think word cloud is just something created for fun
library(wordcloud) 
set.seed(410)   
wordcloud(names(freq), freq, min.freq=25) 
set.seed(410)   
wordcloud(names(freq), freq, max.words=50)  
set.seed(410) 
wordcloud(names(freq), freq, min.freq=20, scale=c(5, .1), colors=brewer.pal(6, "Dark2"))
set.seed(410)   
dark2 <- brewer.pal(6, "Dark2")   
wordcloud(names(freq), freq, max.words=50, rot.per=0.2, colors=dark2) 

# cluster by term similarity
dtm_matrix <- as.matrix(dtm)
dim(dtm_matrix)
filtered_matrix <- dtm_matrix[,dtm_matrix[nrow(dtm_matrix),]>10]   # filter out low frequency terms, otherwise the plot is not clear
dim(as.matrix(filtered_matrix))
library(cluster)   
d <- dist(filtered_matrix, method="euclidian")   
fit <- hclust(d=d, method="ward")   
fit 
plot(fit, hang=-1)
groups <- cutree(fit, k=5)   # 5 clusters here  
rect.hclust(fit, k=5, border="red")

library(fpc)   
d <- dist(filtered_matrix, method="euclidian")   
kfit <- kmeans(d, 3)    # 3 keamns cluster
clusplot(as.matrix(d), kfit$cluster, color=T, shade=T, labels=2, lines=0) 

# get optimal number of clusters
wss <- 2:20
for (i in 2:20) wss[i] <- sum(kmeans(filtered_matrix,centers=i,nstart=5)$withinss)
plot(2:20, wss[2:20], type="b", xlab="Number of Clusters",ylab="Within groups sum of squares")
d <- dist(filtered_matrix, method="euclidian")   
kfit <- kmeans(d, 3)    # 3 keamns cluster is the optimal since SSE droped dramatically
clusplot(as.matrix(d), kfit$cluster, color=T, shade=T, labels=2, lines=0) 
