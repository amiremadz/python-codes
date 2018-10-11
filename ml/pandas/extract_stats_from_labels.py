import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("preds.csv")
df["MainName"] = df["Filename"].apply(lambda s: s.split("HE")[0])

res = df.groupby(["MainName","Predictions"]).count().reset_index()        
res = res.drop("Labels", axis=1)
res.rename(columns={"Filename":"count"}, inplace=True)

res = pd.pivot_table(res, columns="Predictions", values="count", index="MainName")
res = res.reset_index()
res.columns = ["MainName", "0" , "1"]
res = res.fillna(0)
res["0"] = res["0"].astype("int32")
res["1"] = res["1"].astype("int32")
res["Labels"] = res["MainName"].apply(lambda s: s[0])

res["Predictions"] = res.apply(lambda row: "0" if row["0"] > row["1"] else "1", axis=1)

print(res.groupby("Predictions").count())
print(res.groupby("Labels").count())

y_test = res["Labels"]
preds_test = res["Predictions"]

print(classification_report(y_test, preds_test))
print(confusion_matrix(y_test, preds_test))
