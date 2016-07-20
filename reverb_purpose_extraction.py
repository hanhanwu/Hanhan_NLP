'''
Created on Jul 19, 2016
mac terminal command: 
java -Xmx512m -jar reverb-latest.jar all_purpose.csv > all_purpose_export.txt
Note: may need to use Levenshtein Distance or clustering if the final results are unique
      may also need to add " O" in the all_purpose_export.txt since some output is missing this..
      may need to replace all the " in the string to ''
'''

import re
import operator


def main():
    r_pre = "[your file path]all_purpose"                # origional text data
    f_path = "[your file path]all_purpose_export.txt"    # reverb export
    
    p1 = r_pre + "\.csv\t\d+\t(.*?)(\t\d+){6}"
    p2 = "(.*?)O\s*\t(.*?)"
    
    extracted_combo_dct = {}
    stemmed_exteacted_combo_dct = {}
    
    f = open(f_path)
    for l in f:
        r1 = re.search(p1, l)
        m1 = ' '.join(r1.group(1).split('\t'))
        r2 = re.search(p2, l)
        if r2 == None:
            print l
            break    # used to add missing " O"
        m2 = ' '.join([e for e in l.split(r2.group(1))[1].split('O')[1].split('\t') if e != ' ']).split('\n')[0]
        
        extracted_combo_dct.setdefault(m1, 0)
        stemmed_exteacted_combo_dct.setdefault(m2, 0)
         
        extracted_combo_dct[m1] += 1
        stemmed_exteacted_combo_dct[m2] += 1
         
    sorted_combos = sorted(extracted_combo_dct.items(), key=operator.itemgetter(1), reverse=True)
    sorted_stemmed_combos = sorted(stemmed_exteacted_combo_dct.items(), key=operator.itemgetter(1), reverse=True)
     
    for combo in sorted_combos:
        print combo
        
    print "************************"
    
    for stemmed_combo in sorted_stemmed_combos:
        print stemmed_combo
    
if __name__ == "__main__":
    main()
