# Reflection questions 1.) I would use .get() when a certain key might not exist and I wanted to avoid any errors. My rule of thumb would be to use bracket notation when the key must exist and .get when there could be missing data.
# Question 2.) This pattern reminds me of SUMIF from excel because it groups values and calculates totals. Python is better for larger sets of data because it is able to automate the process and can handle a lot more data much more efficiently.

print("--- Exercise 1 ---")
customer = {
  "name": "Alice",
  "email": "alice@example.com",
  "tier": "gold", 
  "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


print("--- Exercise 2 ---")
customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print(customer.get("email", "Email not found"))


print("--- Exercise 3 ---")

# New Version
print(customer.get("email", "no email on file"))

# Older Version (Still used in some codebases)
# try:
#     print(customer["email"])
# except KeyError as error:
#     print(f"KeyError Caught: {error}")


print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key} : {value}")

for item in customer:
     print(item)


print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0,
                  "silver": 0.05,
                  "gold": 0.10,
                  "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")


print("--- Exercise 6 ---")
customers = [
     {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
     {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
     {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers: 
     rate = tier_discounts.get(record["tier"], 0)
     discount = 300 * rate
     print(f"{record['name']}  ({record['tier']}): ${discount:.2f} discount on $300 purchase")


print("--- Exercise 7 ---")
catalog = {
     "Widget A": {"price": 9.99, "stock": 150},
     "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
     if details["stock"] < 20:
          print(f"LOW STOCK: {product} - Only {details}")


print("--- Exercise 8 ---")
transactions = [
     {"reigon": "South", "amount": 300},
     {"reigon": "North", "amount": 150},
     {"reigon": "South", "amount": 200},
]
sales_by_reigon = {}
for sale in transactions:
     reigon = sale["reigon"]
     sales_by_reigon[reigon] = sales_by_reigon.get(reigon, 0) + sale["amount"]
print(sales_by_reigon)

for reigon in sorted(sales_by_reigon):
     print(f"{reigon}: {sales_by_reigon[reigon]}")
