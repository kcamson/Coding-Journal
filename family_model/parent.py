class Parent:
    def __init__(self, first_name, parent_type, age=None):
        print('hhii!!')
        # self is a hook into the object created. It's how you add attributes
        self.first_name = first_name
        self.parent_type = parent_type
        # the `_` signifies that the attribute should be treated as private
        self._age = age

    # these are functions that are hooked into the object but their strucure is a plain old function
    def age(self):
        return self._age

    def which_parent(self, first_name, parent_type):
        if parent_type == 'mom':
            print('{}, is the {}'.format(first_name, parent_type))

    def full_name(self):
        return self.first_name