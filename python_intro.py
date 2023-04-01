# %% [markdown]
# # Python Introduction

# %% [markdown]
# ## Section 1: Variables and Objects

# %%
x = 100                # assign integer object 100 to variable x
y = 100.0              # assign float object 100.0 to variable y
z = '100'              # assign str object 100 to variable z

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

# %% [markdown]
# ## Section 2: Operators
# 

# %% [markdown]
# ### 2.1: Operators on float and int 

# %%
x = 5
y = 10.3

z = x + y    
a = z - 0.3   
b = a / 3    

print(z)
print(a)
print(b)

# %% [markdown]
# ### 2.2: Operators on string 

# %%
aa = 'Happy '
bb = 'Birthday'

cc = aa + bb   
dd = aa * 2

print(cc)
print(dd)

# %% [markdown]
# ### Exercises: 
# Use '+' to concatenate xvar, yvar and zvar together.
# 
# 

# %%
xvar = 'supercali'
yvar = 'fragilistic'
zvar = 'expialidocious'

# %% [markdown]
# Use '*' to repeat the string in greet 3 times to return a new str value yoyoyo.

# %%
greet = 'yo'

# %% [markdown]
# # Section 3: Built-in Python Functions

# %%
aa = 'hello'        
bb = len(aa)        
print(bb) 

cc = '100'
print(type(cc))     
dd = int(cc)        
print(dd)       
print(type(dd))       

# %% [markdown]
# ### Excercises:

# %% [markdown]
# Get the length of strings with len(). Both strings should be length of 11.

# %%
x = 'hello there'

y = 'hi       ok'

# %% [markdown]
# int(), float() and str() functions. Convert the below string to an integer, then double the value (to 106).  Convert this value to a float (106.0) and convert that value to a string.  Retrieve and print the length of this string (should be 5).

# %%
zzy = '53'


# %% [markdown]
# # Section 4: Object Methods

# %%
var = 'Hello, World!'
var2 = var.replace('World', 'Mars')            
print(var2)           

var = 'Hello, World!'
var2 = var.count('l')            
print(var2)            

var = 'hello!'                
var2 = var.upper()                        
print(var2)                        

# %% [markdown]
# # Section 5: Conditions

# %% [markdown]
# ### 5.1: If/elif/else

# %%
zz = input('type an integer and I will tell you its sign:  ')
zyz = int(zz)

print(zyz)

if zyz > 0:
    print('this number is positive')

elif zyz < 0:
    print('this number is negative')

else:
    print('this number is zero')

# %% [markdown]
# ### 5.2: For Loop

# %%
for cc in range(0,5):
    print(cc)
    cc = cc + 1

print('done')

# %% [markdown]
# ### Exercises:

# %% [markdown]
# Use 'if' with 'elif' and 'else'. If variable 'myaa' is greater than variable 'mybb', print 'greater'; otherwise if 'myaa' is less than 'mybb', print 'lesser', otherwise, print 'equal'.  Again, change the values to prove that all 3 conditions are correctly handled.
# 

# %%
myaa = 20               
mybb = 10 

# %% [markdown]
# ## Section 6: User Defined Functions

# %%
def print_hello():
    print('Hello')

print_hello()
print_hello()
print_hello()

# %%
def print_hello(fname):
    greeting = f'Hello, {fname}'
    print(greeting)

print_hello('David')

# %%
def squareit(input):
    squared = input ** 2
    return squared

print(squareit(2))
print(squareit(10))


