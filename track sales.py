print("Welcome to Sunny Jean world")
jeans_sold=int(input("amount of jeans sold?"))
target_sale=int(input("target sale"))
if jeans_sold >= target_sale:
    print("target sale has been reached")
else:
    print("target sale has not been reached")
jeans_in_stock=int(input("original amount of jeans"))
deduction=(jeans_in_stock)-(jeans_sold)
print( "amount of jeans remaining" , deduction)