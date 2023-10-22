# Write a function called "calculate_discounted_price" that takes the original price and discount percentage as arguments and returns the discounted price.
# Write another function called "apply_discount" that takes the original price and a discount percentage as arguments and returns a string that states the discounted price.
# Then, write a third function called "shopping_cart" that calls the "apply_discount" function and prints the message with the discounted price.

# Test the function using:
# shopping_cart(50, 20)

def calculate_discounted_price(original_price, discount_percentage):
    discount = original_price * (discount_percentage/100)
    return original_price - discount

def apply_discount(original_price, discount_percentage):
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    return f"The discounted price is: {discounted_price}"

def shopping_cart(original_price, discount_percentage):
    print(apply_discount(original_price, discount_percentage))

shopping_cart(50,20)
