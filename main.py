# working with lists

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.remove('apple')
fruits.remove('pear')

fruits.append('dragon fruit')
print(fruits)


# working with classes
class MyClass:
    vegetables = ['tomato', 'corn', 'cucumber', 'lettuce']
    vegetables.remove('corn')

    print(vegetables)

    def __init__(self):
        i = 12345

    @staticmethod
    def f():
        return 'whats up??'


print(MyClass.vegetables)
