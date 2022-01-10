# -*- coding: utf-8 -*-
"""

tutorial follow along

"""

import csv

data = open('example.csv', encoding = 'utf-8')

#print(data)

csv_data = csv.reader(data)

data_lines = list(csv_data)

