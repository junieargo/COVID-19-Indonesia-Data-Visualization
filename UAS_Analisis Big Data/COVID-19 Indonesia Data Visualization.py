import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

death = pd.read_csv("C:\Users\kasinas\PycharmProjects\SEMESTER 4\Analisis Big Data\Jumlah_Kematian.csv")
patient = pd.read_csv("C:\Users\kasinas\PycharmProjects\SEMESTER 4\Analisis Big Data\patient.csv")

death.head()
death.tail()

plt.figure(figsize=(15,5))
plt.title('10 Provinsi di Indonesia Dengan Jumlah Kematian COVID-19 Terdikit ')
class Jumlah_Kematian(object):
    pass
Jumlah_Kematian.provinsi.value_counts().plot.bar()

sns.set_style("darkgrid")
sns.FacetGrid(patient, hue='nationality', height = 10)\
.map(plt.scatter, 'current_state', 'province')\
.add_legend()
plt.title('State by province and nationality')
plt.show()