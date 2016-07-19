'''
Created on Jul 18, 2016
'''

import re

def main():
    r_pre = "[your file path]reverb_sample_data"
    f_path = "[your file path]reverb_export.txt"
    
    p1 = r_pre + "\.txt\t\d+\t(.*?)(\t\d+){6}"
    p2 = "(.*?)O\t(.*?)"
    
    f = open(f_path)
    for l in f:
        r1 = re.search(p1, l)
        m1 = ' '.join(r1.group(1).split('\t'))
        r2 = re.search(p2, l)
        m2 = ' '.join(l.split(r2.group(1))[1].split('O\t')[1].split('\t'))
        
        print m1
        print m2
        print
    
if __name__ == "__main__":
    main()
