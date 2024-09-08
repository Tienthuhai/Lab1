class Store:
    def __init__(self,name:str,store_type:str,capacity:int):
        self.name=name
        self.store_type=store_type
        self.capacity=capacity
        self.items={}
    def from_size(self):
        return f"{self.name} {self.store_type} {self.capacity//2}"
    def add_item(self,item_name:str):
        total_items=sum(self.items.values())
        if total_items < self.capacity:
            if item_name in self.capacity:
                self.items[item_name]+=1
            else:
                self.items[item_name]=1
            return f"{item_name} added to the store"
        else:
            return "Not enough capacity in the store"
    def remove_item(self,item_name:str,amount:int):
        if item_name in self.items and self.item[item_name] >= ammount:
            self.items[item_name]-=amount
            if self.items[item_name]==0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the store"
        else:
            return f"Cannot remove {amount} {item_name}"
    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
    def get_totel_items(self):
        total_items=sum(self.items.values())
        return  f"{total_items}" 



    
first_store = Store("First store", "Fruit and Veg", 20) 
second_store = Store("Second store", "Clothes", 500) 

print(first_store.add_item("potato")) 
print(second_store.add_item("jeans")) 
print(first_store.remove_item("tomatoes", 1)) 
print(second_store.remove_item("jeans", 1)) 


