import textacy
import json


def generate_corpus(comment_json):
    my_corpus = []
    with open(comment_json) as input_file:
        article_comments = json.load(input_file)

    comments = list(article_comments.values())[0]['comments']
    for cmt in comments:
        md = {'comment_author':cmt['comment_author'], 'comment_time':cmt['comment_time']}
        doc = textacy.Doc(cmt['comment'], metadata=md)
        my_corpus.append(doc)

    return my_corpus


def main():
    content1 = '''
             The very first clause of your article demonstrates why TWU shouldn be accredited.
             "Going  godless." As though there were something wrong with that.
             And TWU agrees with you. On the page about  Transforming Culture,
             the school talks all about how its students are expected to go out and convert  people,
             in every area of their lives, to change non-believers,
             to guard against "false" ideologies  supported by Satan,
             to turn institutions into Christian "institutions. So heres what we " have.
             A school that would have these people go out and
             a)Abuse their positions as lawyers and  judges to convert their
             clients - a violation of professional ethics - and those who appear before them  in court -
             a violation of the Charter, b) Discriminate against those of different faiths or no  faith at all,
             and, c) Discriminate against gay people.
             It is ludicrous for the school to bang  on about having a faith-based education,
             to brag about these terrible views on its website, and  then turn around and say,
             "No, our law students will be unlike all of our other students and throw off
              "all of the bigotry weve instilled "in them because REASONS." Three "strikes and youre out.
             '''
    metadata1 = {
                 'TotalVotes': 66,
                 'descendantsCount': 13,
                 'negVotes': 23,
                 'posVotes': 89,

                }
    doc1 = textacy.Doc(content1, metadata=metadata1)

    content2 = '''
             Well, youre certainly familiar with legal language tricks.
             "TWUs statement about "students going out and living as Christians in every part of their lives
             does not conflict with the professional ethics of the legal community.
             There are, after all, many Christians who are lawyers.
             They conduct themselves with the same professionalism you can expect of anyone else.
             This is a school where Christian students can focus on their education,
             rather than being forced to defend their choices from the atheist culture so common in higher education.
             There is a reason any serious investigation into the quality of
             education of this school always gives it top marks abcd@gmail.com.
             '''
    metadata2 = {
                 'TotalVotes': 54,
                 'descendantsCount': 6,
                 'negVotes': 15,
                 'posVotes': 69,
                }
    doc2 = textacy.Doc(content2, metadata=metadata2)


    # Preprocess
    t1 = textacy.preprocess.preprocess_text(doc1.text, fix_unicode=True, lowercase=True, transliterate=True,
                    no_urls=True, no_emails=True, no_phone_numbers=True,
                    no_numbers=True, no_currency_symbols=True, no_punct=True,
                    no_contractions=True, no_accents=True)
    print(t1)
    t2 = textacy.preprocess.preprocess_text(doc2.text, fix_unicode=True, lowercase=True, transliterate=True,
                    no_urls=True, no_emails=True, no_phone_numbers=True,
                    no_numbers=True, no_currency_symbols=True, no_punct=True,
                    no_contractions=True, no_accents=True)
    print(t2)


    # Extract
    ## extract name entities
    nes = textacy.extract.named_entities(doc2, include_types=None, exclude_types=None, drop_determiners=True, min_freq=1)
    for ne in nes:
        print(ne)

    ## extract noun chunks
    NNs = textacy.extract.noun_chunks(doc2, drop_determiners=True, min_freq=1)
    for nn in NNs:
        print(nn)

    # Convert each doc to bag of words
    bag_of_words1 = doc1.to_bag_of_words(lemmatize=False, as_strings=False)
    bag_of_words2 = doc2.to_bag_of_words(lemmatize=False, as_strings=False)
    print(bag_of_words1)
    print(bag_of_words2)
    
    # Convert each doc to bag of terms
    ## I think, when the text in a doc is small, lemmatize can be used after getting bag of terms
    bag_of_terms1 = doc1.to_bag_of_terms(ngrams=2, named_entities=True, lemmatize=False, as_strings=True)
    bag_of_terms2 = doc2.to_bag_of_terms(ngrams=4, named_entities=True, lemmatize=False, as_strings=True)
    print(bag_of_terms1)
    print(bag_of_terms2)


    # Extract top topics with LDA/NMF/LSA
    comment_input = "[my file folder path]/article33683150_comment_reaction.json"
    my_corpus = generate_corpus(comment_input)
    
    doc_term_matrix, id2term = textacy.vsm.doc_term_matrix(
     (doc.to_terms_list(ngrams=1, named_entities=True, as_strings=True)
      for doc in my_corpus), weighting='tfidf', normalize=True, smooth_idf=True, min_df=2, max_df=0.95)
    
    topics_num = 3
    m = 'lda'
    model = textacy.tm.TopicModel(m, n_topics=topics_num)
    model.fit(doc_term_matrix)
    doc_topic_matrix = model.transform(doc_term_matrix)
    print(doc_topic_matrix.shape)
    for topic_idx, top_terms in model.top_topic_terms(id2term, top_n=topics_num):
        print('topic', topic_idx, ':', ' '.join(top_terms))



if __name__ == "__main__":
    main()
