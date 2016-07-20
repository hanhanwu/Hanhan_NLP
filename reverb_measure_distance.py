'''
Created on Jul 19, 2016
Method 1: calculate Levenshtein distance between reverb extracted combinations
'''

import Levenshtein
import re
import operator


def main():
    r_pre = "[your file path]/all_purpose"
    f_path = "[your file path]/all_purpose_export.txt"
    
    p1 = r_pre + "\.csv\t\d+\t(.*?)(\t\d+){6}"
    p2 = "(.*?)O\s*\t(.*?)"
    
    extracted_combo_set = set()
    extracted_stemmed_combo_set = set()
    
    f = open(f_path)
    for l in f:
        r1 = re.search(p1, l)
        m1 = ' '.join(r1.group(1).split('\t'))
        r2 = re.search(p2, l)
        if r2 == None:
            print l
            break    # used to add missing " O"
        m2 = ' '.join([e for e in l.split(r2.group(1))[1].split('O')[1].split('\t') if e != ' ']).split('\n')[0]
        
        extracted_combo_set.add(m1.lower())
        extracted_stemmed_combo_set.add(m2.lower())
        
    extracted_combo_lst = list(extracted_combo_set)
    
    ## test only
    target = extracted_combo_lst[-1]
    print 'target: ', target
    print
    match_dct = {}
    
    for i in range(len(extracted_combo_lst)-1):
        dst = Levenshtein.ratio(target, extracted_combo_lst[i])
        match_dct[extracted_combo_lst[i]] = dst
        
    sorted_match_lst = sorted(match_dct.items(), key = operator.itemgetter(1), reverse = True)
    for itm in sorted_match_lst:
        print itm
    
if __name__ == "__main__":
    main()
