import pandas as pd
import numpy as np
import python.labr as l


filename = 'data/labr_data/reviews.tsv'
file=l.LABR.read_review_file(l,filename)

print(file[0])