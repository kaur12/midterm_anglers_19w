import matplotlib.pyplot as plt


years = [2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018]
membership_number = [52, 67, 45, 55, 65, 60, 55, 65, 80]

plt.plot(years, membership_number, color='blue')
plt.xlabel('years')
plt.ylabel('membership_number')
plt.title('MEMBERSHIP NUMBERS PER YEAR')

plt.show();
