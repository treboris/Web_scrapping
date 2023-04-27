import plotly.express as px
import pandas as pd
import seaborn as sns
import numpy as np




df = pd.read_csv('diagram_data/programing.csv')



# create data


x = df['count']
y = df['languages']
z = x+np.random.rand(15)
z=z*z

# Change color with c and transparency with alpha.
# I map the color to the X axis value.
plt.scatter(x, y, s=z*2000, c=x, cmap="Blues", alpha=0.4, edgecolors="grey", linewidth=2)

# Add titles (main and on axis)
plt.xlabel("the X axis")
plt.ylabel("the Y axis")
plt.title("A colored bubble plot")

# Show the graph
plt.show()
