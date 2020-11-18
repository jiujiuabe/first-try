class Dog():
    def __init__(self, name, age):
        # 创建Dog()实例时，通过实参向其传递名字和年龄，self会自动传递
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')


my_dog = Dog('willie', 1)
print("My dig's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + ' years old.')
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 2)
print("Your dog's name is " + your_dog.name.title() + '.')
print("Your dog is " + str(your_dog.age) + ' years old.')
your_dog.sit()
your_dog.roll_over()
