import pandas as pd
from src.data.make_dataset import load_data
from src.visualization.visualize import plot_scatterplot, loss_curve
from src.models.train_model import split_data
from src.features.build_features import dummy_vars
#Data Path Definition
if __name__=="__main__":
    #Load Data
    data_path = "data\\raw\\Admission.csv"
    df =load_data(data_path)
    
    x,y = dummy_vars(df)
    
   # Plot scatter plot
    plot_scatterplot(df)
    
    MLP, grid = split_data(x,y)
    loss_curve(MLP)