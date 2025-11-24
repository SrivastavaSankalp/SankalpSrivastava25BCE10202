import qrcode

d=0
def show_menu(menu_dict, title):
    print(f"\n--- {title} ---")
    for key, item in menu_dict.items():
        print(f"{key}. {item['name']} - Rs{item['price']}")
def calculate_bill():
    print("-----------Hotel Management System----------")
    print("---------------------------------------------")
    rooms = {
        1: {"name": "Standard Room", "price": 7500},
        2: {"name": "Business Room", "price": 11000},
        3: {"name": "Family room", "price": 15000},
        4: {"name": "Deluxe Room", "price": 21000},
        5: {"name": "Suite", "price": 35000}
    }
    food_menu = {
        1: {"name": "Breakfast Combo", "price": 999},
        2: {"name": "Lunch Meal Combo", "price": 2099},
        3: {"name": "Dinner Buffet", "price": 2199},
        4: {"name": "Full Meal Combo(Breakfast+Lunch+Dinner+Beverages)", "price": 4499},
        5: {"name": "Snack Combo","price":399},
        6: {"name": "Beverages+Sides","price":199},
        7: {"name": "IceCream","price":99},
        8: {"name": "Beverages", "price": 99}
    }
    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    show_menu(rooms, "ROOM TYPES")    
    room_choice = int(input("Select a Room Type (1-5): "))
    nights = int(input("How many nights ?: "))
    selected_room = rooms[room_choice]
    room_total = selected_room['price'] * nights
    print(f"Selected: {selected_room['name']} for {nights} nights.")
    food_total = 0
    orders = [] 
    print("\nDo you want to order food?")
    ordering = True
    while ordering:
        global d
        user_response = input("Type 'yes' to order, or 'no' to finish: ") 
        if user_response == 'no':
            ordering = False
        if user_response == 'yes':
            show_menu(food_menu, "RESTAURANT MENU")
            food_choice = int(input("Enter Item Number: "))
            if food_choice in food_menu:
                quantity = int(input("Quantity: "))
                item = food_menu[food_choice]
                cost = item['price'] * quantity
                food_total += cost
                orders.append(f"{item['name']} x{quantity} (Rs{cost})")
                print(f"Added {quantity} {item['name']}(s) to bill.")
            else:
                print("Item not found.")
        else:
            print("Please type 'yes' or 'no'.")
    grand_total = room_total + food_total
    d+=grand_total
    print("\n" + "="*30)
    print(f" HOTEL BILL: {name.upper()}")
    print("="*30)
    print(f"Phone: {phone}")
    print(f"Room: {selected_room['name']} (Rs{selected_room['price']}/night)")
    print(f"Duration: {nights} nights")
    print(f"Room Charges: Rs{room_total}")
    print("-" * 30)
    if len(orders) > 0:
        print("Restaurant Charges:")
        for order in orders:
            print(f"  - {order}")
        print(f"Food Total: Rs{food_total}")
    else:
        print("No food ordered.")
    print("-" * 30)
    print(f"GRAND TOTAL: Rs{grand_total}")
    print("="*30)
    print("Thank you for staying with us!")
calculate_bill()
print('-----SCAN QR FOR PAYMENT----- ')
qr = qrcode.make(d)
qr.save('qrcode.png')