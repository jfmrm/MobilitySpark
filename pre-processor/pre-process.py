import pandas as pd

data = pd.read_csv("../producer/data/200118_240118.csv")
data = data.sort_values("Instante")
data.to_csv("../producer/data/test.csv", sep=",")
