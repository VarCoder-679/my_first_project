##--->SHOPPING CART IN PYTHON
foods = []
prices =[]
total=0

name=input("Enter the name of the customer: ")
while True:
    food = input("Enter the food(q or Q for quit): ")
    if food.lower()=="q": #automatically quit even if the letter is capitalize "Q"
        break
    else:
        price = float(input(f"Enter the price of {food}: Rs. "))
        foods.append(food)
        prices.append(price)

print(f" ------{name}'s FOOD CART------- ")

for i in range(len(foods)):
    print(f"{foods[i]} : Rs. {prices[i]}")

for price in prices:
    total += price
print(f"Your total is: Rs.{total}")
