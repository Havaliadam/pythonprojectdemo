class Inventory:
    def __init__(self,max_capacity):
        self.max_capacity=max_capacity
        self.item={}
        self.item_count=0


    def add_itemm(self,name,price,quantity):
        if name in self.item:
            return f"^{name} ögesi envater de var\n"
        if self.item_count+quantity>self.max_capacity:
            return f"{quantity} adet {name} eklendi\n"

        self.item[name]={"name":name,"price":price,"quantity":quantity}
        self.item_count+=quantity
        return f"{name} ögesi basari ile eklendi\n"
    def delete_item(self,name):
        if name not in self.item:
            return f"{name} ögesinde var\n"
        self.item_count-=self.item[name]["quantity"]
        del self.item[name]
        return  f"{name} silindi\n"


