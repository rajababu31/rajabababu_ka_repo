"""def display(pizza_name):
    num = len(pizza_name)
    if num == 0 :
       print("please select a pizza")
       return
 #else:
    for i in pizza_name:
        print(i)


    print(f"ther are {num} pizza")
    print(f"first pizza is {pizza_name[0]}")
    print(f"last pizza is {pizza_name[len(pizza_name) - 1]}")
    """



pizza=["veg","non-veg","margritra","hawaie","boo-boo"]
#display(pizza)
print()
#empty=()    #created an empty collection
#display(empty)
def custom(i) :  # i is considered as element of pizza name
    return len(i)
def add_pizza(pizzas,step=0) :  #step ko o assign karke hamne kar dia hai is parameter ko optional
    step=int(step)
    add=input("please enter the pizza to be added in the menu : ")

    if pizza_exist(add,pizzas):
        print("pleae enter diff pizza name,it is already exist")
    else :
         pizzas.append(add)
         #pizza.sort(reverse=True,key=custom)
         pizza.sort()
         for i in pizza[:step] :
           print(i)
#add_pizza(pizza)
print(pizza)

def pizza_exist(add,pizzas):
    for i in pizzas :
        if add.lower() == i or add.upper() == i :  # in that way it will test taking your input as all lower and upper and then compare with the list element
          return True
    return False

add_pizza(pizza)

