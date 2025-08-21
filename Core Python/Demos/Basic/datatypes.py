####numeric
#1.  int
x=10


#2.  class
x=3.14
print(type(x))

#3. comples
x=10+5j   #real + imaginary


####Text
#4. string
x='First string'
x="this isn't an example"
x='''First line
Second line
Third line'''
x="""This is for multiline statement.
First
Second"""

print(type(x))


####Sequentials
#1. List
x=[1,2,3,'xyz',3.14]

#2. Tuple
x=(1,2,3,'abc',3.14)

#3. Range
x=range(1,11)
print(type(x))

####Settype
#1. Set
x={1,2,'xyz',3.14}

#2. FrozenSet
x=frozenset({1,2,'abc',3.14})


####Mapping
#1. Dictionary
x={'name':'Rahul Patil', 'dept':'student'}


####BooleanType
#1. True
x= True

#2. False
x= False


####NoneType
x=None
print(x)
print(type(x))