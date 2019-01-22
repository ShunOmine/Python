import matplotlib.pyplot as plt
import pandas as pd

#ファイルを読み込む ---
df = pd.read_csv('kion10y.csv', encoding="utf-8")

#気温が３０度超えのデータを調べる　---
atui_bool = (df["気温"] > 30)

#データを抜きだす ---
atui = df[atui_bool]

#年ごとにカウント ---
cnt = atui.groupby(["年"])["年"].count()

#出力
print(cnt)
cnt.plot()
plt.savefig("tenki-over30.png")
plt.show()