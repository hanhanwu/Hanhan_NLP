#!/bin/sh

echo "Preprocess Raw Text Input"
python3.5 text_preprocessing/preprocess.py  -i '../input/Raw_Text/BOOKS/' -o '../output/Preprocessed_Output/BOOKS/'
# python3.5 text_preprocessing/preprocess.py  -i '../input/Raw_Text/BOOKS/no1.txt' -o '../output/Preprocessed_Output/BOOKS/'
echo "Done! Generated Preprocessed Data"
