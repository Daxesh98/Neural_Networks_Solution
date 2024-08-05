#Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Function Definition
def load_data(data_path):
    df = pd.read_csv(data_path)
    
    print("Print Head",df.head())
    
    print("Data Shape",df.shape)
    
    print("Check data type",df.dtypes)
    
    # Converting the target variable into a categorical variable
    df['Admit_Chance'] = (df['Admit_Chance'] >= 0.8).astype(int)
    
    print("Print Head of Target Variable ",df.head())

    # Drop any unnecessary columns
    df = df.drop(['Serial_No'], axis=1)
    print("Print Head After Droping unnecessary columns",df.head())

    print("Data Shape After Droping unnecessary columns",df.shape)
    
    print("Check data type After Droping unnecessary columns",df.dtypes)
    
    print("Describe After Droping unnecessary columns",df.describe())
    
    return df

    


    
    