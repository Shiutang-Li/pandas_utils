#!/usr/bin/python
# -*- coding:utf-8 -*-

# description     : Output a list of lists where each small list contains coulmns of the same value 
# author          : Shiu-Tang Li
# last update     : 5/22/2018
# python_version  : 3.5.2

import pandas as pd
import numpy as np

def duplicate_columns(df):
    
    # Input:
    # df:                target dataframe
    # show_result:       print output if set to True
    
    # Output:            list of lists where each small list contains duplicate coulmns 
    #                    (Won't include any column which doesn't repeat with other columns) 
    
    repeated_columns = []
    for column1 in df.columns:
        for column2 in df.columns:
            if df[column1].equals(df[column2]) and (column1 < column2):
                flag = 0 
                for item in repeated_columns:
                    if (column1 in item) and (column2 not in item):
                        item.append(column2)
                        flag = 1
                    elif (column1 in item) and (column2 in item):
                        flag = 1
                if flag == 0:
                    repeated_columns.append([column1, column2])
    return repeated_columns
