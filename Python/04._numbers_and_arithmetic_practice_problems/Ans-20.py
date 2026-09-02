number_of_products = 4
price_per_product = 75

total_cost = number_of_products * price_per_product

complete_groups = total_cost // 100
remaining_amount = total_cost % 100

print("Total cost: ₹", total_cost)
print("Complete groups of ₹100:", complete_groups)
print("Remaining amount: ₹", remaining_amount)