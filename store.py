class Store:
    def __init__(self, name: str, store_type: str, capacity: int):
        self.name = name
        self.store_type = store_type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def from_size(cls, name: str, store_type: str, size: int):
        # Tạo một instance mới với capacity là 50% của size
        return cls(name, store_type, size // 2)

    def add_item(self, item_name: str):
        total_items = sum(self.items.values())
        if total_items < self.capacity:
            if item_name in self.items:
                self.items[item_name] += 1
            else:
                self.items[item_name] = 1
            return f"{item_name} added to the store"
        else:
            return "Not enough capacity in the store"

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the store"
        else:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.store_type} with capacity {self.capacity}"

    def get_total_items(self):
        return f"{sum(self.items.values())}"

# Tạo các instance của lớp Store
first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store("Second store", "Clothes", 500)

# Thực hiện các thao tác
print(first_store.add_item("potato")) 
print(second_store.add_item("jeans")) 
print(first_store.remove_item("tomatoes", 1)) 
print(second_store.remove_item("jeans", 1)) 
print(first_store)
