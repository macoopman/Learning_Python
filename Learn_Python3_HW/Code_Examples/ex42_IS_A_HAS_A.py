

## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a Object
class Person(object):

    def __init_(self,name):
        ## has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = none;


## Employee is-a Person
class Employee(Person):

    def __init__(self,name,salary):
        ## creating employee object and setting varables
        super(Employee, self).__init__ (name)
        ## A Employee has-a salary
        self.salary = salary
        
