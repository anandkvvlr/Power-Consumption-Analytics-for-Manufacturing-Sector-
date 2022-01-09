# Energy Consumption Classification

# DECISION TREE
# importing libraries
import pandas as pd
import numpy as np
import statsmodels.api as smf
from sklearn.preprocessing import StandardScaler, MinMaxScaler,RobustScaler
import scipy.stats as stats


# loading the dataframe

beverage = pd.read_excel(r'C:\Users\Aniket Annam\Desktop\Data Science\Deployement\dataset\DATA - Copy.xlsx')
beverage.shape
beverage.info()
beverage=beverage.drop(['Timestamp'], axis = 1)

# converting continous data into categorical dataset using binning
categorical=pd.cut(beverage.allplant,bins=[250,358,462],labels=['low','high'])
beverage.insert(10,'energy_consumption',categorical)

beverage=beverage.drop(['allplant'], axis = 1)
colnames = list(beverage.columns)

# taking predictors and target
predictors = colnames[:9]
target = colnames[9]

# Building Decision tree model
from sklearn.tree import DecisionTreeClassifier as DT

model = DT(criterion = 'entropy',max_depth=9)
model.fit(beverage[predictors], beverage[target])

# saving the model
# importing pickle
import pickle
pickle.dump(model, open('model.pkl', 'wb'))

# load the model from disk
model = pickle.load(open('model.pkl', 'rb'))

# checking for the results
list_value = pd.DataFrame(beverage.iloc[0:1,:9])
list_value

print(model.predict(list_value))
