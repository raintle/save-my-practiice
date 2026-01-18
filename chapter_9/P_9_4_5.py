class Restaurant:
    """餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化类"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆基本信息"""
        print(f"{self.restaurant_name} is {self.cuisine_type} style")

    def open_restaurant(self):
        """表示正在营业"""
        print(f"{self.restaurant_name} is open")

    def all_print(self):
        self.describe_restaurant()
        self.open_restaurant()

    def number_served_print(self):
        print(f"now have {self.number_served} people served")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increase_number_served(self, number_served):
        self.number_served += number_served

old_people_chicken = Restaurant("Chicken", "north")
#创建实例
old_people_chicken.all_print()
#使用方法
old_people_chicken.set_number_served(12)
old_people_chicken.number_served_print()
old_people_chicken.increase_number_served(12)
old_people_chicken.number_served_print()

