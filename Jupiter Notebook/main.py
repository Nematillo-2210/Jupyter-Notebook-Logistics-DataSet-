# %% [markdown]
# # Logistics Shipments Analysis
#
# This notebook analyzes delayed shipments in a logistics dataset.
# It identifies which warehouses and carriers contribute most to delays,
# and examines the impact of delays on average transit days.

# %%
# Load libraries
#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

# %%

df = pd.read_csv("logistics_shipments_dataset.csv")
df = df.dropna(subset=["Delivery_Date", "Cost"])


df["is_delayed"] = df["Status"] == "Delayed"


is_delayed = df[df["is_delayed"]]


delays_by_warehouse = is_delayed["Origin_Warehouse"].value_counts().sort_values(ascending=False)
delays_by_carrier = is_delayed["Carrier"].value_counts().sort_values(ascending=False)


avg_transit = df.groupby("is_delayed")["Transit_Days"].mean()
avg_transit.index = ["On-time", "Delayed"]

fig, axes = plt.subplots(1, 3, figsize=(22,6))

delays_by_warehouse.plot(kind="barh", color="#0eeb5b", edgecolor="black", ax=axes[0])
axes[0].set_xlabel("Number of Delays")
axes[0].set_ylabel("Warehouse")
axes[0].set_title("Delayed Shipments by Warehouse")

for i, v in enumerate(delays_by_warehouse):
    axes[0].text(v + 0.5, i, str(v), va='center')


delays_by_carrier.plot(kind='barh', color='#23b6fa', edgecolor='black', ax=axes[1])
axes[1].set_xlabel("Number of Delays")
axes[1].set_ylabel("Carrier")
axes[1].set_title("Delayed Shipments by Carrier")
for i, v in enumerate(delays_by_carrier):
    axes[1].text(v + 0.5, i, str(v), va='center')


avg_transit.plot(kind="bar", color=["blue","red"], ax=axes[2])
axes[2].set_ylabel("Average Transit Days")
axes[2].set_xlabel("Shipment Status")
axes[2].set_xticklabels(["On-time","Delayed"], rotation=0)
axes[2].set_title("Average Transit Days")

for i, v in enumerate(avg_transit):
    axes[2].text(i, v + 0.1, f"{v:.2f}", ha='center')

plt.tight_layout()
plt.show()

# %% [markdown]
# ### Analysis
#
# **Warehouse delays:**
# The first chart shows which warehouses have the most delayed shipments.
# It is clear that **Warehouse_SF** has the highest number of delays, indicating potential bottlenecks at that location.
#
# **Carrier delays:**
# The second chart shows delayed shipments by carrier. **UPS** and **USPS** have the lowest number of delays, while **Amazon Logistics**, which might have been expected to perform better, had around 30 delays — nearly 5 fewer than **DHL**, which experienced the most delayed shipments.
#
# **Average transit days:**
# The third chart demonstrates that, on average, it takes around **4 days** to deliver a shipment.
# Delayed shipments take only slightly longer, showing that delays do not drastically affect delivery times or customers’ expectations.
# Nevertheless, logistics companies should explore ways to **improve efficiency and speed**.
