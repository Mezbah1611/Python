import pandas as pd
import scipy.stats as stats

# Load dataset
df = pd.read_csv(r'C:\Users\Mezbah Uddin\Downloads\Compressed\test.csv')

# One-sample t-test for `battery_power`
battery_power_mean = 1200  # Hypothesized population mean
t_stat, p_value = stats.ttest_1samp(df['battery_power'], battery_power_mean)
print(f"One-sample t-test for battery_power:\n t-statistic = {t_stat}, p-value = {p_value}")
if p_value < 0.05:
    print("Conclusion: Reject H0. The mean battery power is significantly different from 1200 mAh.")
else:
    print("Conclusion: Fail to reject H0. The mean battery power is not significantly different from 1200 mAh.")


