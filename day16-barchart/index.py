import matplotlib.pyplot as plt

# Sample data
months = ['January', 'February', 'March', 'April', 'May', 'June']
sales = [15000, 12000, 18000, 9000, 20000, 14000]

# Plotting the bar chart
plt.bar(months, sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales')

# Display the chart
plt.show()
