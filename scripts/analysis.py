import pandas as pd

# Load datasets
porter = pd.read_csv("../data/delivery.csv")
orders = pd.read_csv("../data/olist_orders_dataset.csv")
items = pd.read_csv("../data/olist_order_items_dataset.csv")
customers = pd.read_csv("../data/olist_customers_dataset.csv")

# Print shapes
print("Porter:", porter.shape)
print("Orders:", orders.shape)
print("Items:", items.shape)
print("Customers:", customers.shape)

# Preview sample
print("\nPorter Preview:")
porter.head()

