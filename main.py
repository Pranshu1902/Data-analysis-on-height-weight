import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('weight-height.csv')
df.head()

df['Height(m)'] = (df['Height']*2.5)/100
df['Weight(Kg)'] = df['Weight']/2.2046
df["BMI"] = df['Weight(Kg)']/(df['Height(m)'])**2
df.head()

health = np.ones(10000, dtype="U6")

for i in range(10000):
  if df.iloc[i]["BMI"]<18.5:
    health[i]="Under"
  elif df.iloc[i]["BMI"]<25.0:
    health[i]="Good"
  else:
    health[i]="Over"

df['Health']=health
df[df['Weight(Kg)']>=100.0].head()


male_mean = df[df['Gender']=="Male"]['Weight(Kg)'].mean()
female_mean = df[df['Gender']=="Female"]['Weight(Kg)'].mean()

above_mean = np.zeros(10000, dtype=bool)
for i in range(10000):
  if df.iloc[i]['Gender']=="Male":
    if df.iloc[i]['Weight(Kg)']>male_mean:
      above_mean[i]=True
    else:
      above_mean[i]=False
  else:
    if df.iloc[i]['Weight(Kg)']>female_mean:
      above_mean[i]=True
    else:
      above_mean[i]=False
df["Above Mean"] = above_mean
df.head()



# plot 1

x = df[df['Gender']=="Male"]['Weight(Kg)'].head(10)
y = df[df['Gender']=="Male"]['Height(m)'].head(10)
plt.bar(x,y, color="r", label="Male")

x = df[df['Gender']=="Female"]['Weight(Kg)'].head(10)
y = df[df['Gender']=="Female"]['Height(m)'].head(10)
plt.bar(x,y, color="b", label="Female")

plt.legend()


# plot 2

plt.bar([1], male_mean, width=0.1, color="r", label="male")
plt.bar([1.4], female_mean, width=0.1, label="female")
plt.legend()
plt.title("Mean Weight (in Kg)");


# plot 3

arr = np.arange(1,11)
man = df[df['Gender']=="Male"]["BMI"].head(10)
man_mean = man.mean()
woman = df[df['Gender']=="Female"]["BMI"].head(10)
woman_mean = woman.mean()

mean_m = np.full((10,1), man_mean)
mean_w = np.full((10,1), woman_mean)

fig, ax = plt.subplots()

ax.scatter(arr, man, color="r", label="Male");
ax.scatter(arr, woman, label="Female");
ax.plot(arr, mean_m, color="r")
ax.plot(arr, mean_w)
ax.legend()
ax.annotate('Female Mean BMI', xy=(6.28, woman_mean), xytext=(8, 21.8),arrowprops=dict(facecolor='green', shrink=0.05))
ax.annotate('Male Mean BMI', xy=(6.28, man_mean), xytext=(1, 30),arrowprops=dict(facecolor='green', shrink=0.05));
ax.set(title="BMI Comparision");

