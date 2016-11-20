import json
import re


class ScrapeNewsPipeline(object):

    def open_spider(self, spider):
        self.file_article = open('[my output folder root path]/output/test_article_output.json', 'w')
        self.file_comment = open('[my output folder root path]/output/test_comment_output.json', 'w')


    def process_item(self, item, spider):
        article_id_ptn = '\d{8}'
        m_article = re.match(article_id_ptn, list(item.keys())[0])
        if m_article != None:
            print("********pipeline, article*******", m_article.group(0))
            line = json.dumps(item) + "\n"
            self.file_article.write(line)
        else:
            line = json.dumps(item) + "\n"
            self.file_comment.write(line)

        return(item)


    def close_spider(self, spider):
        self.file_article.close()
        self.file_comment.close()
