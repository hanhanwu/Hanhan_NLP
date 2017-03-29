#!/bin/sh

echo "Preprocess Raw Text Input"
# python3.5 text_preprocessing/preprocess.py  -i '../input/Raw_Text/BOOKS/' -o '../output/Preprocessed_Output/BOOKS/'   # used on preprocess.py
python3.5 text_preprocessing/preprocess2.py  -i '/Users/devadmin/Documents/CF_big_comment_files/CF_big_comment_files' -o '../output/Preprocessed_Output/CF_big_comment_files_test/' -a 'tokenize,ssplit,pos'  # used on preprocess2.py
echo "Done! Generated Preprocessed Data"
