import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Store.csv',encoding='latin1',skiprows=[0])
df = df.dropna(axis=1, how='all')
df = df.dropna(how='all')
df = df.fillna(0)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

def calculate(payment_type, name):
    total = payment_type.sum()
    print(f"Total Payment by {name} : {total}")

print("="*50)
print("Payment Type Summary".center(50))
print("="*50)
calculate(df['Card'], "Card")
calculate(df['Cash'], "Cash")
calculate(df['UPI'], "UPI")
calculate(df['CNote'], "CNote")
print("="*50)

daily_total = df.groupby('Date')[['Card', 'Cash', 'UPI', 'CNote']].sum()

daily_total.plot(kind='line', color = ['green','orange','blue','red'],figsize=(10,6))
plt.title("Daily Payment Totals by Method", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Amount")
plt.grid(True, linestyle = "--")
plt.legend(title = "Payment Method")
plt.tight_layout()
plt.show()
