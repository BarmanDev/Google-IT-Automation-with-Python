"""
Pregunta 2
Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. 
The values of these attributes can be easily changed at the object level.
The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. 
Fill in the blanks to make the code satisfy the behavior described in the quote. 

"""

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw


class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
    # Switching values of variables using a temporary variable.
    temp = you.apples
    you.apples = me.apples
    me.apples = temp
    return you.apples, me.apples


def exchange_ideas(you, me):
    # Assigning the total number of ideas to each idea attribute.
    you.ideas = you.ideas + me.ideas
    me.ideas = you.ideas
    return you.ideas, me.ideas


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(
    johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(
    johanna.ideas, martin.ideas))
