import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris = pd.read_csv("Iris.csv")

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(15, 6), dpi=200)

species = iris['Species'].unique()
colors = ["blue", "yellow", "pink"]

for specie, color in zip(species, colors):
    sub_df = iris[iris['Species'] == specie]
    
    ax1.scatter(
        sub_df['SepalLengthCm'], 
        sub_df['PetalLengthCm'], 
        label=specie, 
        color=color, 
        alpha=0.5, 
        edgecolor='black'
    )

ax1.legend(title="specie", fontsize=8)
ax1.set_title("Sepal Length vs. Petal Length")
ax1.set_xlabel("Sepal Length (cm)")
ax1.set_ylabel("Petal Length (cm)")

#-----------------------------------------------------

ax2.hist(iris['PetalWidthCm'], bins=10, color="#198f74", edgecolor="black")
ax2.set_title("Petal Width Distribution")
ax2.set_xlabel("Petal Width (cm)")
ax2.set_ylabel("Frecuency")

#-----------------------------------------------------
cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

for col in cols:
    ax3.plot(iris.index, iris[col], label=col)

ax3.set_title("Measurements")
ax3.set_xlabel("Indexes")
ax3.set_ylabel("Centimeters")
ax3.legend(loc="upper left", fontsize=8)
ax3.grid(True, linestyle=":", alpha=0.5)

plt.subplots_adjust(wspace=0.35)
plt.show()
plt.close()

#Part B
loan = pd.read_csv("LoanDataset - LoansDatasest.csv")
fig1, (axi1, axi2, axi3) = plt.subplots(nrows=1, ncols=3, figsize=(17, 6), dpi=200)

intent_counts = loan['loan_intent'].value_counts(ascending=True)  

axi1.barh(intent_counts.index, intent_counts.values, color="#17ec22", edgecolor="black")
axi1.set_title("Loan Intent")
axi1.set_xlabel("N. of Requesters")
axi1.grid(axis='x', linestyle=":", alpha=0.6)

#-----------------------------------------------------

loan['loan_amnt'] = (
    loan['loan_amnt']
    .astype(str)
    .str.replace('£', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)

loan['loan_amnt'] = pd.to_numeric(loan['loan_amnt'], errors='coerce')
loan['customer_income'] = pd.to_numeric(loan['customer_income'], errors='coerce')

df_scatter = loan.dropna(subset=['customer_income', 'loan_amnt'])

p99_income = df_scatter['customer_income'].quantile(0.99)
p99_amnt = df_scatter['loan_amnt'].quantile(0.99)

axi2.scatter(
    df_scatter['customer_income'] / 1000, 
    df_scatter['loan_amnt'] / 1000, 
    alpha=0.2,               
    color="gold", 
    edgecolor="none",
    s=12                     
)
axi2.set_title("Income vs. Loan Amount")
axi2.set_xlabel("Customer Income (thousands)")
axi2.set_ylabel("Loan Amount (thousands)")

axi2.set_xlim(0, p99_income / 1000)
axi2.set_ylim(0, p99_amnt / 1000)
axi2.grid(True, linestyle=":", alpha=0.3)

#------------------------------------------------------

bins3 = [18, 25, 35, 50, np.inf]
labels3 = ['18-25', '25-35', '35-50', '50+']
loan['age_group'] = pd.cut(loan['customer_age'], bins=bins3, labels=labels3, right=False)


min_val = loan['loan_amnt'].min()                       
max_val = float(loan['loan_amnt'].quantile(0.99))       


fixed_bins = np.linspace(min_val, max_val, 15)


colors3 = ['lightcoral', 'lightskyblue', 'limegreen', 'darkorchid']
data_groups = [loan[loan['age_group'] == g]['loan_amnt'].dropna() for g in labels3]


axi3.hist(
    data_groups,
    bins=fixed_bins,
    color=colors3,
    label=labels3,
    edgecolor="black",
    linewidth=0.7
)

axi3.set_title("Amount Distribution among Age")
axi3.set_xlabel("Loan Amount (£)")
axi3.set_ylabel("Frecuency")
axi3.legend(title="Age Groups")
axi3.grid(axis='y', linestyle=":", alpha=0.5)

plt.subplots_adjust(wspace=0.35)
plt.show()