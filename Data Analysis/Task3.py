import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load dataset
df = pd.read_csv(r'C:\Users\Mezbah Uddin\Downloads\Compressed\test.csv')

# 1. Check Normal Distribution for `battery_power`
sns.histplot(df['battery_power'], kde=True)
plt.title('Battery Power Distribution')
plt.xlabel('Battery Power')
plt.ylabel('Frequency')
plt.show()

stats.probplot(df['battery_power'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Battery Power')
plt.show()

stat, p = stats.shapiro(df['battery_power'])
print(f'Shapiro-Wilk Test for Normality (battery_power): p-value = {p}')
if p > 0.05:
    print("battery_power follows a normal distribution.")
else:
    print("battery_power does not follow a normal distribution.")

# 2. Check Binomial Distribution for `dual_sim`
dual_sim_counts = df['dual_sim'].value_counts()
expected_freq = [dual_sim_counts.sum() * 0.5] * 2  # Assuming equal probability (0.5) for Binomial
chi2, p = stats.chisquare(f_obs=dual_sim_counts, f_exp=expected_freq)
print(f'Chi-square test for Binomial (dual_sim): p-value = {p}')
if p > 0.05:
    print("dual_sim follows a Binomial distribution.")
else:
    print("dual_sim does not follow a Binomial distribution.")
