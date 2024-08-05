from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV


def split_data(x, y):
    # Splitting the dataset into train and test data
    xtrain, xtest, ytrain, ytest =  train_test_split(x, y, test_size=0.2, random_state=123)
    
    print(f"Training Set: {xtrain.shape}, Testing Set: {xtest.shape}")
    
    # fit calculates the mean and standard deviation
    scaler = MinMaxScaler()
    scaler.fit(xtrain)

    # Now transform xtrain and xtest
    Xtrain = scaler.transform(xtrain)
    Xtest = scaler.transform(xtest)
        
    # fit/train the model. Check batch size.
    MLP = MLPClassifier(hidden_layer_sizes=(3), batch_size=50, max_iter=100, random_state=123)
    MLP.fit(Xtrain,ytrain)

    # make Predictions
    ypred = MLP.predict(Xtest)
    
    
    confusion_matrix(ytest, ypred)
    
    print("Confusion Matrix",confusion_matrix)
    
    
    accuracy_score(ytest, ypred)
    print("Accuracy Score", accuracy_score)
    
    
    MLP.get_params
    
    # we will try different values for hyperparemeters
    params = {'batch_size':[20, 30, 40, 50],
          'hidden_layer_sizes':[(2,),(3,),(3,2)],
         'max_iter':[50, 70, 100]}

    # create a grid search
    grid = GridSearchCV(MLP, params, cv=10, scoring='accuracy')
    grid.fit(x, y)
    
    
    grid.best_params_
    
    
    grid.best_score_
    
    
    grid.estimator
    
    return MLP,grid