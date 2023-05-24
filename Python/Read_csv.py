import sys
import pandas as pd
import os
import ROOT
from tqdm import tqdm
import numpy as np
import csv
from datetime import datetime


#checks on file extension and command line value for time ordering
if len(sys.argv) < 3:
    print(f"You should run like this--> python3 Read_csv.py 'name_of_your_csv_file.csv' 'time order:0/1'")
    sys.exit(-1)
elif sys.argv[1].endswith(".csv")== False:
    print(f"Input file must be a csv file")
    sys.exit(-1)
elif (int(sys.argv[2])>1): 
    print(f"Time ordering can be 0 (ascending) or 1 (descending).\nPlease run again changing the second command line argument")
    sys.exit(-1)

file_data = sys.argv[1]
time_ordering = int(sys.argv[2])

#read data from csv and sort it by date of birth accordingly to the second command line argument
df = pd.read_csv(file_data)
df['Date of birth'] = pd.to_datetime(df['Date of birth'], format='mixed')
df.sort_values('Date of birth', inplace=True, ascending=True if time_ordering== 0 else False)
#Print the sorted CSV file
print("\nSorted CSV file = \n", df)

