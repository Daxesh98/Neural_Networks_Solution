import pandas as pd

def dummy_vars(df):
    # Create dummy variables for all 'object' type variables except 'Loan_Status'
    df = pd.get_dummies(df, columns=['University_Rating','Research']).astype(int)
    

    # Separate the input features and target variable
    x = df.drop(['Admit_Chance'], axis=1)
    y = df['Admit_Chance']

    return x, y