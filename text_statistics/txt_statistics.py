import os
import sys
from os import path
from collections import Counter

class Text_stats:

    def __init__(self, file_path, words_count):
        self.file_path = file_path
        self.words_count = words_count
        

root_dir = os.path.expanduser('~')
txt_files = list() 

for root, dirs, files in os.walk(root_dir, topdown=True):
    if '.txt' in files:
        texts = []
        words_count = list(Counter(texts[0]).most_common(1)[0])
