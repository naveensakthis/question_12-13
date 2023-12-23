
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("enterprise.csv")

plt.plot(data['year'], data['Industry_value'])
plt.xlabel('Year')
plt.ylabel('Industry Value')
plt.title('Enterprise Trends Over the Years')
plt.yticks('2011')
plt.savefig("Enterprise_plot.png")
plt.show()