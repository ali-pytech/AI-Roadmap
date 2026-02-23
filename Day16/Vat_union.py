"""Customers VAT Union"""
customers_jan = {"Ali","Ahmed","Faisal"}
customers_feb = {"hamza","Umer","Zubair"}
all_customers = customers_jan | customers_feb

print(f"All Customers: {all_customers}")
