import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv("0022100908.csv")
df=df.sort_values(by='score', ascending=False)

name_list=df["球員"].to_list()
point_list=df["score"].to_list()

x1 = np.arange(len(name_list[0:12]))
x2=  np.arange(len(name_list[13:]))

width = 0.35  

fig, (ax1,ax2) = plt.subplots(2)
rects1 = ax1.bar(x1,point_list[0:12], width, label='球員')
rects2 = ax2.bar(x2,point_list[13:], width, label='球員')

ax1.set_ylabel('Scores')
ax1.set_title('Scores by every player')
ax2.set_ylabel('Scores')
ax2.set_title('Scores by every player')

ax1.set_xticks(x1, name_list[0:12],fontsize=8)
ax2.set_xticks(x2, name_list[13:],fontsize=8)
ax1.legend()
ax2.legend()

ax1.bar_label(rects1, padding=3)
ax2.bar_label(rects1, padding=3)

fig.tight_layout()

plt.show()
