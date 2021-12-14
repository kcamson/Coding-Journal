class MapPractice:

    def __init__(self):
        print('hi!')

    animals = {
        'hippo': 'hp',
        'kangaroo': 'kg'
    }


print(MapPractice().animals.__contains__('hippo'))
print(MapPractice().animals['hippo'])

