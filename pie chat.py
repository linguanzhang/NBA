# Libraries

import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data
df=pd.read_csv("0022100908.csv")
df=df.drop(columns=["score"])
#df = pd.DataFrame({
#'group': ['lebron','curry','durant','4','5','6'],
#'score': [1, 1.5, 30, 4,5,62],
#'blocks': [29, 10, 9, 34,1,54],
#'steals': [8, 39, 23, 24,1,42],
#'defRebs': [7, 31, 33, 14,1,31],
#})
 
# ------- PART 1: Define a function that do a plot for one line of the dataset!
 
def make_spider( row, title, color):
    amount = len(df["球員"])
    
    import math
    column_amount = math.sqrt(amount)
    column_amount = int(math.ceil(column_amount))
    # number of variable
    categories=list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(column_amount,column_amount,row+1, polar=True, )

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=5)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([3,5,7,10], ["3","5","7","10"], color="grey", size=6)
    plt.ylim(0,10)

    # Ind1
    values=df.loc[row].drop('球員').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)

    # Add a title
    plt.title(title, size=5, color=color, y=0.9)

    
# ------- PART 2: Apply the function to all individuals
# initialize the figure
my_dpi=150
plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
 
# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df.index))
 
# Loop to plot
for row in range(0, len(df.index)):
    make_spider( row=row, title=' '+df['球員'][row], color=my_palette(row))

plt.show()
