import pandas
import matplotlib.pyplot as plt

#Read the data from the csv file
df = pandas.read_csv("eggholder_data.csv")
df.pop('Unnamed: 0')

print("Eggholder:")

#Average the results of the 20 runs
df_avg = df.mean(axis=0)
print("Average:")
print(df_avg)

#Standard Deviation of the data
std_dev = df.std()
print("Standard Deviation:")
print(std_dev)

#Plot the data
plt.title("Eggholder Function")
plt.plot(df['PSO'], label='PSO')
plt.plot(df['GA'], label='GA')
plt.plot(df['DE'], label='DE')
plt.legend(['PSO', 'GA', 'DE'])
plt.savefig('eggholder_plot.png')
plt.show()

print("-----------------------------------------------------")

df = pandas.read_csv("ackley_data.csv")
df.pop('Unnamed: 0')

print("Ackley:")

df_avg = df.mean(axis=0)
print("Average:")
print(df_avg)

std_dev = df.std()
print("Standard Deviation:")
print(std_dev)

plt.title("Ackley Function")
plt.plot(df['PSO'], label='PSO')
plt.plot(df['GA'], label='GA')
plt.plot(df['DE'], label='DE')
plt.legend(['PSO', 'GA', 'DE'])
plt.savefig('ackley_plot.png')
plt.show()