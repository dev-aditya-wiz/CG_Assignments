products = 47
products_per_box = 6

complete_boxes = products // products_per_box
remaining_products = products % products_per_box

print("Complete boxes:", complete_boxes)
print("Remaining products:", remaining_products)