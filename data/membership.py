import matplotlib.pyplot as plt

Years = ('2014', '2015', '2016', '2017', '2018')
y_pos = ('0', '50,000', '1,00,000', '1,50,000')
performance = ['1,00,000', '1,50,000', '1,00,00', '50,000', '1,50,000']

plt.bar(y_pos, performance, align='center', alpha=0.5, color='purple')
plt.xticks(y_pos, Years)
plt.xlabel('Years')
plt.ylabel('Number of eggs received')
plt.title('Species received number of eggs')

plt.show()