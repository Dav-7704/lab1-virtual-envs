import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("bottle.csv", usecols=["Salnty", "T_degC"], encoding="latin-1")
df = df.dropna()
print("Строк после очистки:", len(df))

X = df[["Salnty"]]
y = df["T_degC"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression().fit(X_train, y_train)
print("Коэффициент:", model.coef_[0])
print("Свободный член:", model.intercept_)
print("R^2 на тесте:", model.score(X_test, y_test))

plt.scatter(X_test[:5000], y_test[:5000], s=3, color="b")
plt.plot(X_test[:5000], model.predict(X_test[:5000]), color="k")
plt.xlabel("Salnty"); plt.ylabel("T_degC")
plt.savefig("result2.png", dpi=120)
print("График сохранён: result2.png")