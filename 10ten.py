# 10. Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
cost_price=int(input("enter the cost:"))
sell_price=int(input("enter the selling price:"))

profit=sell_price-cost_price
if sell_price>cost_price:
    print("shopkeeper have profit of",profit,"Rupees")
elif sell_price==cost_price:
    print("shopkeeper has no profit and no loss")
elif sell_price<cost_price:
    print("shopkeeper has in",profit,"loss")