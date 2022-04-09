# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tabula as tb
import pandas as pd
file ="sem1.pdf"
table = tb.read_pdf(file)

csv_table = tb.convert_into(file,"pdf_convert.csv")
df=pd.concat(table)
excel_file =df.to_excel("sem1_convert.xlsx") 
                  

