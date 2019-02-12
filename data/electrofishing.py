import matplotlib.pyplot as plt

labels = "2016", "2017", "2018"
sizes = [38, 47, 49]
colors = ['lightskyblue', 'lightgreen', 'lightpink']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Number of fishes caught")
plt.xlabel("Electrofishing in 2016, 2017 & 2018")
plt.show()