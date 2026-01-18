class Restaurant:
    """餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化类"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        #设置默认属性值

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
        #将属性变化调用到类方法中
        self.number_served = number_served

    def increase_number_served(self, number_served):
        self.number_served += number_served

old_people_chicken = Restaurant("Chicken", "north")
#创建实例
old_people_chicken.all_print()
#使用方法
old_people_chicken.set_number_served(12)
#使用方法
old_people_chicken.number_served_print()
old_people_chicken.increase_number_served(12)
old_people_chicken.number_served_print()
print('\n')


class User:
    """user的类"""
    def __init__(self, first_name, last_name, age, email):
        """初始化user信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def greet_user(self):
        """向user打招呼"""
        print(f"hello! {self.first_name} {self.last_name}.")

    def describe_user(self):
        """描述user"""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")
        print('ur email is', self.email)

    def increase_login_attempts(self):
        self.login_attempts += 1
        print('now login attempts is', self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print('now login attempts is', self.login_attempts)

user_1 = User("Chicken", "Chicken", "17", "2162951845@qq.com")
#创建实例
user_1.greet_user()
user_1.describe_user()
#使用方法
user_1.increase_login_attempts()
user_1.increase_login_attempts()
user_1.increase_login_attempts()
#使用方法添加值
user_1.reset_login_attempts()