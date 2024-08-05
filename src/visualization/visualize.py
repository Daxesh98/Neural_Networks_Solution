import matplotlib.pyplot as plt
import seaborn as sns

def plot_scatterplot(df):
    plt.figure(figsize=(15, 8))
    sns.scatterplot(data=df, x='GRE_Score', y='TOEFL_Score', hue='Admit_Chance')
    plt.title('Scatter Plot', fontsize=16)
    plt.show()
    
    
# Plotting loss curve
def loss_curve(MLP):
    
    loss_values = MLP.loss_curve_

# Plotting the loss curve
    plt.figure(figsize=(10, 6))
    plt.plot(loss_values, label='Loss', color='blue')
    plt.title('Loss Curve')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.show()