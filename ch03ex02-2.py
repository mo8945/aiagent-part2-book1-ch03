import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({
    "hour": [9,15,18,21],
    "views": [120,340,560,290]
})

plt.plot(df["hour"], df["views"])

plt.title("시간대별 기사 조회 수")
plt.xlabel("시간")
plt.ylabel("조회수")

plt.show()