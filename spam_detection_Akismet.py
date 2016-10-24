# Akismet is a spam detection tool initially used on WordPress to filter out spam commet
from akismet import Akismet, AkismetError

AKISMET_API_KEY = "[YOUR AKISMET API KEY]"
pageurl = "https://www.reddit.com/r/GRE/comments/58uvg4/are_we_given_pencilsscratch_paper_for_the/"    # choose a serious topic


# check whether a comment is spam
def isspam(comment, comment_author, ip_address):
  try:
    amt = Akismet(key=AKISMET_API_KEY, blog_url=pageurl)
    valid = amt.verify_key()
    if valid:
      akismet_data = { 'comment_type': 'comment',
                       'user_ip': ip_address,
                       'user_agent': '',
                       'comment_author_email': comment_author }
      return amt.comment_check(comment, data=akismet_data, build_data=True)
    else:
      print "Invalid Key"
      return False
  except AkismetError, e:
    print e.response, e.statuscode
    return False
    
    
cmt = "****casino, onlie casino!!!"
cmt_author = "xxxx@spam.com"
ip_address = "127.0.0.1"

isspam(cmt, cmt_author, ip_address)
