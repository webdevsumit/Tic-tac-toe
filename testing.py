
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.pipeline import Pipeline
from sklearn import metrics

import joblib

import pandas as pd
df = pd.read_csv("data.csv", index_col=0)
print(df.shape)

x = df.drop(["9"],axis=1)

data = df.drop_duplicates(subset = x.columns,keep='last')
print(data.shape)

x = df.drop(["9"],axis=1)
y = df.drop(x.columns,axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=1)

pipe = Pipeline([
    ('model' ,RandomForestClassifier(max_depth=4, n_estimators=10, max_features=9 ),)
])

mod = GridSearchCV(estimator = RandomForestClassifier(),
                                param_grid={'max_depth' : [1,2,3,4,5,6,7,8,9,10]},
                                cv=3)

mod.fit(x_train,y_train)
pre = mod.predict(x_test)

print()
print()
print("RandomForestClassifier",metrics.accuracy_score(y_test,pre))
print()
print()

pipe = Pipeline([
    ('model' ,DecisionTreeClassifier(max_depth=4)),
])

mod = GridSearchCV(estimator = DecisionTreeClassifier(),
                                param_grid={'max_depth' : [1,2,3,4,5,6,7,8,9,10]},
                                cv=3)

mod.fit(x_train,y_train)
pre = mod.predict(x_test)

print()
print()
print("DecisionTreeClassifier",metrics.accuracy_score(y_test,pre))
print()
print()

pipe = Pipeline([
    ('model' ,AdaBoostClassifier()),
])

#mod = GridSearchCV(estimator = AdaBoostClassifier(), cv=3)

#mod.fit(x_train,y_train)
#pre = mod.predict(x_test)

pipe.fit(x_train,y_train)
pre = pipe.predict(x_test)

print()
print()
print("AdaBoostClassifier",metrics.accuracy_score(y_test,pre))
print()
print()


#mod = GridSearchCV(estimator = KNeighborsClassifier(),cv=3)

#mod.fit(x_train,y_train)
#pre = mod.predict(x_test)
pipe = Pipeline([
    ('model' ,KNeighborsClassifier()),
])


pipe.fit(x_train,y_train)
pre = pipe.predict(x_test)

print()
print()
print("KNeighborsClassifier",metrics.accuracy_score(y_test,pre))
print()
print()


pipe = joblib.load("model.joblib")


pre = pipe.predict(x_test)
print()
print()
print("from model",metrics.accuracy_score(y_test,pre))
print()
print()
#joblib.dump(pipe,"model.joblib")