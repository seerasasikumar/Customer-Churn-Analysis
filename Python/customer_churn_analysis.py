import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CustomerChurn_Project.csv")
print(df.head())
print(df["Churn"].value_counts())
print(df["Churn"].value_counts(normalize = True)*100)
print(df.groupby("Contract")["Churn"].value_counts())
print(df.groupby("Churn")["MonthlyCharges"].mean())
print(df.groupby("Churn")["tenure"].mean())


df["Churn"].value_counts().plot(kind = "bar")
plt.show()
df.groupby("Contract")["Churn"].count().plot(kind = "bar")
plt.show()
df.groupby("Churn")["MonthlyCharges"].mean().plot(kind = "bar")
plt.show()
df.groupby("Churn")["tenure"].mean().plot(kind = "bar")
plt.show()
df.groupby("Churn")["PaymentMethod"].count().plot(kind = "bar")
plt.show()
