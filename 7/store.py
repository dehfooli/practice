import qrcode
PRODUCTS = []

def read_from_database():
    f = open("database.txt","r")

    for line in f:
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


def show_menu():
    print("1- add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show_List")
    print("6- Buy")
    print("7- Exit")

def add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    new_product={'code':code, 'name':name, 'price':price, 'count': count}
    PRODUCTS.append(new_product)

def Edit():
    code = input("enter code: ")
    for product in PRODUCTS:
        if product['code']==code:
            print("Which feild do you want to edit? ")
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
            
            break
    else:
        print("This code not valid")


def Remove():
    ...
def Search():
    user_input=input("type your keyword: ")
    for product in PRODUCTS:
        if product['code']==user_input or product ['name']==user_input:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])   
            break
    else:
        print("not found")
        

def Show_List():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"])

def Buy():
    ...



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
        Search()
    elif choice ==5:
        Show_List()
    elif choice ==6:
        Buy()
    elif choice ==7:
        write_to_database()
        exit(0)
    else:
        print("Please enter corect number.")

    