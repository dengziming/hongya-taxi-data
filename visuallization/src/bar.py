
import matplotlib.pyplot as plt

data = [5, 20, 15, 25, 10]
labels = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']

plt.bar(range(len(data)), data, tick_label=labels)
plt.show()