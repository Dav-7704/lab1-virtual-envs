import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:, np.newaxis, 2]
X_train, X_test = X[:-20], X[-20:]
y_train, y_test = y[:-20], y[-20:]

regr = linear_model.LinearRegression().fit(X_train, y_train)
y_pred = regr.predict(X_test)

print("numpy:", np.__version__)
print("Коэффициенты:", regr.coef_)
print("MSE: %.2f" % mean_squared_error(y_test, y_pred))
print("R^2: %.2f" % r2_score(y_test, y_pred))

plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)
plt.savefig("result1.png", dpi=120)
print("График сохранён: result1.png")