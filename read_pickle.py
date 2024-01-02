#!/usr/bin/python3

### this code takes a .pkl ('pickle') file from AlphaFold2 and extracts the confidence values
### pLDDT, pTM and ipTM, and stores them in a csv file
### the pickle file contains a nested dictionary of the various NumPy arrays produced by the model
### as well as the confidence measures. pTM and ipTM are a single number (ipTM only for multimers) 
### pLDDT is per residue we average it

from pathlib import Path
import pandas as pd
import pickle as pkl
import numpy as np
import os

file_path = Path("/Users/gabrielleadmans/Documents/_11 Computational/2023-12-29_Good_AF_SnC2_models/")
file_names = []

pldtt_list = []
iptm_list = []
ptm_list = []

# Here we loop over files in the directory (file path)

for file_name in os.listdir(file_path):
    if file_name.endswith(".pkl"):      #looking only at pickle files
        file_names.append(file_name)
        with open(file_path / file_name, "rb") as f:
            object = pkl.load(f)

        print(type(object))             #showing the content of the dictionaries, optional

        #here we look for our three values of interest: plddt, ptm and iptm and add them to lists
        print(object.keys())
        for k, v in object.items():
            print(k, " ", type(v))
            if k == "plddt":
                print(v)
                print(np.mean(v))
                pldtt_list.append(np.mean(v))
            elif k == "iptm":
                print(v)
                iptm_list.append(v)
            elif k == "ptm":
                print(v)
                ptm_list.append(v)


#getting the date for output file name
from datetime import datetime
date = datetime.today().strftime('%Y-%m-%d')
print (date)


#now we save our values to a csv file
df = pd.DataFrame({"pLDDT": pldtt_list, "ipTM": iptm_list, "pTM": ptm_list}, index=file_names)
df.to_csv(file_path/f"{date}_AF_confidence_values.csv", index_label="model_name")
