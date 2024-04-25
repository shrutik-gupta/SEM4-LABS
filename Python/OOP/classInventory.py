class Inventory:
    def __init__(self):
        self.item_details = {}

    def add_item(self, item_id, item_name, stock_count, price):
        if item_id not in self.item_details:
            self.item_details[item_id] = {'item_name': item_name, 'stock_count': stock_count, 'price': price} #nested dictionary - item_id key ke value mai ek new dictioanry store karo
            print(f"Item '{item_name}' added to inventory.")
        else:
            print(f"Item with ID {item_id} already exists in inventory.")

    def update_item(self, item_id, new_details):
        if item_id in self.item_details:
            self.item_details[item_id].update(new_details) #nwe deatils mai we are passing exact format -> {id: {key:value}}
            print(f"Item details updated for ID {item_id}.")
        else:
            print(f"Item with ID {item_id} not found in inventory.")

    def check_item_details(self, item_id):
        if item_id in self.item_details:
            print(f"Item details for ID {item_id}:")
            for key, value in self.item_details[item_id].items(): #printing key:values of inner dictioanry
                print(f"{key}: {value}")
        else:
            print(f"Item with ID {item_id} not found in inventory.")

# Test the class
inventory = Inventory()

# Add items
inventory.add_item(1, "Apple", 10, 1.5)
inventory.add_item(2, "Banana", 20, 0.75)

# Update item details
inventory.update_item(1, {'stock_count': 15, 'price': 2.0})

# Check item details
inventory.check_item_details(1)
inventory.check_item_details(2)
inventory.check_item_details(3)  # Non-existent item
