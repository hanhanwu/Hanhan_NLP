
* SENSEI Annotated Corpur: http://sensei.group.shef.ac.uk/senseiCorpus/

* Google Perspective API: https://www.perspectiveapi.com


Abusive Language Detection

* Detect online abusive [2016]: https://github.com/hanhanwu/Hanhan_NLP/blob/master/Sentiment_Analysis_Resources/online_abusive.pdf
  * I guess, here they calculate both Agreement Rate and Fleiss's Kappa is to tell how much is shown to be agreed by all, and how much agreement among those should not be by chance
  * hatebase dataset: https://www.hatebase.org/
* Personal Attacks [2017]: https://github.com/hanhanwu/Hanhan_NLP/blob/master/Sentiment_Analysis_Resources/Personal_Attacks.pdf
  * I think the interesting thing in this paper are those data analysis at the end, talking about findings for their questions. Their machine learning part looks creative, they compared their model with "emsemble annotators", but their model gives continuous output (although later they set threshold), human beings are not good at annotating continuous values, so the comparisons are not fair to human beings; however if let these annotators annotate binary labels, not fair to their models. This makes me feel, when it comes to evaluating a model, maybe we should compare it with other models?
* In general, after reading the above 2 papers, I feel doing large scale sentiment analysis is challenging, because human experts define the meaning of lables (such as "abusive", "toxic") are different, and maybe in different context (such as Wiki data or Facebook data) the definition could also vary? How could researchers in sentiment analysis area find really reliable scientific method to prove their theories?

* Edtorial Criteria and Automation: https://isojjournal.wordpress.com/2015/04/15/picking-the-nyt-picks-editorial-criteria-and-automation-in-the-curation-of-online-news-comments/
  * I like `Automatically Computed Ratings` section, it talks about the auto rating methods can be used on crowd sourcing, and to measure Brevity, Readability (those indexes are trying to measure the number of years schooling), Degree of personal experience sharing
  * Crowd Sourcing criteria they used: Argument Quality, Criticality, Internal Coherence, Personal Experience, Readability, and Thoughtfulness

* Sentiment Analysis in video game
  * The paper: http://www.sciencedirect.com/science/article/pii/S0950705117304240?via%3Dihub
    * It's first 30 days was free, so I got the free one. But here, you have to pay for the authors :)
  ![sentiment analysis in video game](https://github.com/hanhanwu/Hanhan_NLP/blob/master/Sentiment_Analysis_Resources/video_game_sentiment_analysis.png)
  * Gammers submitted the games here: http://www.skillcraft.ca/
  * They used SO-CAL for the analysis: https://github.com/sfu-discourse-lab/SO-CAL
