import pandas as pd
import matplotlib.pyplot as plt

class SalesDataProcessor:
    def __init__(self, file_path):
        self.df = None
        self.load_data(file_path)
        
    def load_data(self, file_path):
        """Loads the dataset into a Pandas DataFrame."""
        self.df = pd.read_csv(file_path)
        print("Dataset Loaded Successfully!")
    
    def clean_data(self):
        """Handles missing values and ensures correct data types."""
        self.df.fillna(0, inplace=True)  # Replace missing values with 0
        self.df["Date"] = pd.to_datetime(self.df["Date"])  # Convert Date column to datetime
        print("Data Cleaned Successfully!")
    
    def get_total_sales(self):
        """Returns the total sales amount."""
        return self.df["TotalPrice"].sum()
    
    def get_unique_products(self):
        """Returns a list of unique products."""
        return self.df["Product"].unique().tolist()
    
    def get_sales_by_category(self):
        """Returns total sales per product category."""
        return self.df.groupby("Category")["TotalPrice"].sum()
    
    def get_top_selling_product(self):
        """Returns the product with the highest total sales."""
        return self.df.groupby("Product")["TotalPrice"].sum().idxmax()

class CustomerSalesProcessor(SalesDataProcessor):
    def get_total_sales_by_customer(self, customer_id):
        """Returns total sales made by a specific customer."""
        return self.df[self.df["CustomerID"] == customer_id]["TotalPrice"].sum()
    
    def get_frequent_customers(self, n=5):
        """Returns the top n customers who made the most purchases."""
        return self.df["CustomerID"].value_counts().head(n)
    
    def get_sales_by_city(self):
        """Returns total sales per city."""
        return self.df.groupby("City")["TotalPrice"].sum()

def visualize_data(processor):
    """Generates plots for sales analysis."""
    # Bar chart for sales by category
    processor.get_sales_by_category().plot(kind='bar', title='Total Sales by Category')
    plt.show()
    
    # Line graph for daily sales trend
    daily_sales = processor.df.groupby("Date")["TotalPrice"].sum()
    daily_sales.plot(kind='line', title='Daily Sales Trend')
    plt.show()
    
    # Pie chart for sales by city
    processor.get_sales_by_city().plot(kind='pie', title='Sales Distribution by City', autopct='%1.1f%%')
    plt.show()

# Main Execution
file_path = "sales_data_india.csv"
processor = CustomerSalesProcessor(file_path)
processor.clean_data()

# Display Results
print("Total Sales:", processor.get_total_sales())
print("Unique Products:", processor.get_unique_products())
print("Sales by Category:\n", processor.get_sales_by_category())
print("Top Selling Product:", processor.get_top_selling_product())

# Visualize Data
visualize_data(processor)
