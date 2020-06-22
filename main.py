counter = 1
willbuy = 1
maintotal = 0
products = [
    'spiderman',
    'batman'
]

normal_price = [
    180,
    190
]

discounted_price  = [
    180 - (180*.20),
    190 - (190*.20)
]
def normal_order(product_to_order):
    global maintotal
    if product_to_order == 1:
        print("You chose", products[0],normal_price[0])
        quantity = int(input("How many? [numbers only]"))
        total = (normal_price[0]*quantity)
        print(total)
        maintotal = total+maintotal
    elif product_to_order ==2:
        print("You chose", products[1], normal_price[1])
        quantity = int(input("How many? [numbers only]"))
        total = (normal_price[1]*quantity)
        print(total)
        maintotal = total+maintotal
    else:
        print("You chose an invalid number!")
        

def discounted_method(product_to_order):
    global maintotal
    if product_to_order == 1:
        print("You chose", products[0], discounted_price[0])
        quantity = int(input("How many? [numbers only]"))
        total = (discounted_price[0]*quantity)
        print(total)
        maintotal = total+maintotal
    elif product_to_order ==2:
        print("You chose", products[1], discounted_price[1])
        quantity = int(input("How many? [numbers only]"))
        total = (discounted_price[1]*quantity)
        print(total)
        maintotal = total+maintotal
    else:
        print("You chose an invalid number!")

while True:
    if (counter==1):
        print("What do you want to buy? \n [1]Spiderman \n [2]Batman")
        chosen_product = input()
        if willbuy==1:
            print('Are you a regular or senior citizen? \n [1]Regular \n [2]Senior Citizen')
            chosenMode = input()
            if int(chosenMode) == 1:
                normal_order(int(chosen_product))
            elif int(chosenMode) == 2:
                discounted_method(int(chosen_product))
                
            isBuying = input("Do you want to buy again? (Y if yes and any to end)")
            if isBuying=='Y' or isBuying=='y':
                willbuy = 1
            else:
                willbuy = 0
                break
            counter = counter+1
        else:
            print('please buy stuff again')
    elif counter>1:
        print("What do you want to buy? \n [1]Spiderman \n [2]Batman")
        chosen_product = input()
        if willbuy==1:
                normal_order(int(chosen_product))
                isBuying = input("Do you want to buy again? (Y if yes and any to end)")
                if isBuying=='Y' or isBuying=='y':
                    willbuy = 1
                else:
                    willbuy = 0
                    break
                counter = counter+1
        else:
            print('please buy stuff again')

print(f'Number of transactions:{counter}\ntotal:{maintotal}')
    
