
# Example Website data source: http://www.theglobeandmail.com/opinion/dont-set-your-hair-on-fire-it-wont-help/article33683150/comments/
## Here, I am trying to find a web element with class = 'c29cjTJ', and trace back to its grand grand parent
test_ca = driver.find_element_by_class_name("c29cjTJ")
p = test_ca.find_element_by_xpath('../../../..').get_attribute("class")
print(test_ca.text, p)
if p.strip() == "c2LlVA7":
print('yes')
