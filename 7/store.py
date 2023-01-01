import qrcode

PRODUCTS = []

def read_from_database():
    f = open("database.txt","r")

    for line in f:
        line = line.replace('\n','')
        result= line.split(",")
        my_dict={"code":result[0],"name":result[1],"price":result[2],"count":result[3]}
        PRODUCTS.append(my_dict)

    f.close()

def write_to_database():
    f = open("database.txt","w")
    f.close()
    new_file= open("database.txt","a")
    for product in PRODUCTS:
        new_file.write(str(product["code"])+","+str(product['name'])+','+str(product['price'])+','+str(product['count'])+'\n')
    new_file.close()

def Factor(Product_list,i):
    sum = 0
    j = 1
    print("_____________ Factor _____________")
    for product in Product_list:
        print(j , "- " , product["name"],"     ",product["price"],"    ",product["count"])
        sum += (product["count"] * product["price"])
        j+=1
    print("Sum = ",sum)


def show_menu():
    print("1- add")
    print("2- Edit")
    print("3- Remove")
    print("4- qrcodestore")
    print("5- Search")
    print("6- Show_List")
    print("7- Buy")
    print("8- Exit")

def add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    new_product={'code':code, 'name':name, 'price':price, 'count': count}
    PRODUCTS.append(new_product)

def Edit():
    Show_List()
    code = input("Which code do you want to edit? please enter code: ")
    for product in PRODUCTS:
        if product['code']==code:
            print("1- name:\n2- price:\n3- count: " )
            choice = int (input("enter your choice: "))
            if choice ==1:
                new_name=str(input("please enter new name: "))
                product["name"]=new_name
                print("Information has been updated successfully")
            elif choice == 2:
                new_price=str(input("please enter new price: "))
                product["price"]=new_price
                print("Information has been updated successfully")
            elif choice == 3:
                new_count= int(input("please enter new count: "))
                product["count"]=new_count
                print("Information has been updated successfully")
            
            break
    else:
        print("This code not valid")


def Remove():
    Show_List()
    remove = input("Which code do you want to remove? please enter code: ")
    for product in PRODUCTS:
            if product['code']==remove:
                print("Do you sure? \n 1-yes\t\t2-No")
                choice = int (input("enter your choice: "))
                if choice==1:
                   write_to_database()
                elif choice==2:
                    break
                print("Information has been deleted successfully")
    else:
            print("This code not valid")

def qrcodestore():
    Show_List()
    user_input = input("Which code do you want to have it's QRCODE? please enter code: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            qr = qrcode.QRCode(version = 1,box_size = 10,border = 5)
            qr.make(product)
            qr.make(fit = True)
            img = qr.make_image(fill_color = 'red',back_color = 'white')
            img.save("product.png")
            print("QRCODE generated")
            break
                    
    else:
        print("This code not valid")

def Search():
    user_input=input("type your keyword: ")
    for product in PRODUCTS:
        if product['code']==user_input or product ['name']==user_input:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])   
            break
    else:
        print("not found")
        

def Show_List():
    print("code\t\tname\t\tprice\t\tcount")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"],"\t\t", product["count"])

def Buy():
    i = 0
    PurchaseAmount= 0
    Product_list= []
    user_input = input("Which code do you want to buy ? please enter code: ")
    for product in PRODUCTS:
        while True:
            if product["code"] == user_input:
                print("How many do you need to buy?")
                choice =int(input("please enter the count? "))
                if choice > int(product['count']):
                    print("sorry! This Product not enough in shop. The available  number of this item is",end=" ")
                    print(product['count'])
                    new_choice = input("Do you want to continue??? (y/n) -> ")
                    if new_choice == 'Y' or new_choice == 'y':
                        continue
                    else:
                        return
                else:
                    choice < int(product['count'])
                    product['count'] = int(product['count']) - choice
                    PurchaseAmount = (choice * int(product['price']))
                    i+=1
                    Factor_dict = {"name":product['name'],"price":PurchaseAmount,"count":choice}
                    str(product['count'])
                    str(product['price'])
                    Product_list.append(Factor_dict)
                    break
    else:
        print("This Code is Not valid!")
print("Welcome to Gashtook Store")
print("Loding...")
read_from_database()
print("Data loaded.")

while True:

    show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        add()
    elif choice ==2:
        Edit()
    elif choice ==3:
        Remove()
    elif choice ==4:
        qrcodestore()
    elif choice ==5:
        Search()
    elif choice ==6:
        Show_List()
    elif choice ==7:
        Buy()
    elif choice ==8:
        write_to_database()
        exit(0)
    else:
        print("Please enter corect number.")