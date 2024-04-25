class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price

    def book_table(self, table_number):
        self.booked_tables.append(table_number)

    def customer_order(self, table_number, order):
        self.customer_orders.append((table_number, order))
        print(f"Order '{order}' taken for table {table_number}.")

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_booked_tables(self):
        print("Booked Tables:", self.booked_tables)

    def print_customer_orders(self):
        print("Customer Orders:")
        for table, order in self.customer_orders:
            print(f"Table {table}: {order}")

restaurant = Restaurant()

restaurant.add_item_to_menu("Pizza", 10)
restaurant.add_item_to_menu("Burger", 8)
restaurant.add_item_to_menu("Salad", 6)

restaurant.book_table(1)
restaurant.book_table(2)

restaurant.customer_order(1, "Pizza")
restaurant.customer_order(2, "Burger")
restaurant.customer_order(1, "Salad")

restaurant.print_menu()
restaurant.print_booked_tables()
restaurant.print_customer_orders()
