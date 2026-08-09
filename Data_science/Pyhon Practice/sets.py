# A set is an unordered collection of items . Every set element is unique (no duplicates) and must be  immutable(cannot be changed).
# Sets  can also he used to perform mathematical set operations like Union , Intersection , Symmetric ,Difference , etc.
#Characterstics:-
#Unordered
#Mutable
#No Duplicates
#Cant contain mutable data types
# ---------------------------------------------------------------------------------------------------------
# Creating Sets

# empty set
# s = set()
# print(s)
# print(type(s))
#1D and 2D set
# s1 = {1,2,3}
# print(s1)
#2D set
# s2 = {1,2,3,{4,5}} -----> this 2D set is not possible 
# print(s2)

#Homo and Hetro
# s1 = {1,'hello',4.5,True,(1,2,3,4)} # duplicate nhi ho sakte hai kyu ki python true ko 1 samjta hai aur 1 set main nhi ho sakte,
#Hum set ke andar immutable mtlb set dal sakte hai
# print(s1)

#Using type conversion
# s4 = set([1,2,3])
# print(s4)
#Duplicates are not allowed
# s5 = {1,1,2,2,3,3,4,5}
# print(s5)
# set can't have mutable items
# s6 = {1,2,[3,4]} #set ke andar mutable datatype store nhi ho sakta hai mtlb list jo hai wo mutable hai
# print(s6)

# ------------------------------------------------------------------------------------------------
#set ke andar order matter nhi karta hai agar contain same hai toh order matter nhi karta hai
# s1 = {1,2,3}
# s2 = {3,2,1}
# print(s1 == s2)

# ------------------------------------------------------------------------------------------------------------
# Accessing items
# set main hum indexing nhi kar sakte hai kyu ki set unordered hota hai
# Set mai hum slicing bhi nhi kar sakte
# Set main agar koi element khus gya toh naa hum index ka use kar ke usse dekh sakte hai aur na nikal sakte hai

# --------------------------------------------------------------------------------------------------------------
# Editing items
# Editing kaam nhi karta hai set ke andar
# ----------------------------------------------------------------------------------
# Adding items --> hum set main add kar sakte hai aur update kar sakte hai item ko
#Hashing control the index positions
# s = {1,2,3,4}
#add --> add ek baar main ek item ko add karga set ke andar
# s.add(5)
# print(s)
#update --> update multiple items ko dalega set ke andar aur wo sab item ko hame list ke andar dalkar bhajna padega
# s.update([5,6,7])
# print(s)

# -----------------------------------------------------------------------------------------------------------
# deleting items :-

#del ---> yhape bhi sem tuple jaisa logic hai particlar index per rakha element ko delete nhi kar sakte 
# s = {1,2,3,4,5}
# print(s)
# del s
# print(s)
# ---------------------
#discard --> discard jo hai element na milne per error through nhi karta hai
# s.discard(5)
# print(s)
# -----------------------------
#remove ---> remove nhi same kaam karta hai discard ki tarah per remove element na milne per error through karta hai
# s.remove(4)
# print(s)
# ----------------------------------------------
#pop --> pop function randomly items ko delete karta hai set ke andar
# s.pop()
# print(s)
# ---------------------------------------------
#clear --> set ko empty bna deta hai
# s.clear()
# print(s)

# -------------------------------------------------------------------------------------------------------

# Set Operations:-

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
#Union(|)
# print(s1 | s2)
#Intersection(&)
# print(s1 & s2)
#Difference(-)
# print(s1 - s2)
# print(s2 - s1)
#Symmetric Difference(^)
# print(s1 ^ s2)
#Membership Test
# print( 1 in s1 )
# print(1 not in s1)
# print(1 not in s2)
#Iteration
# for i in s1:
#     print(i)
# ------------------------------------------------------------------------------------------------
# set functions
# len/sum/min/max/sorted
# s = [1,2,3,4,5,6,7]
# print(len(s))
# print(sum(s))
# print(min(s))
# print(max(s))
# print(sorted(s,reverse= True)) # sorted result always  in list
# ------------------------------------------------------------------------------------------
#Union/update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print(s1.union(s2))
# s1.update(s2)
# print(s1)
# print(s2)
# -------------------------------------------------------------------------------------------
#intersection/intersection_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1.intersection(s2)
# print(s1)
# s1.intersection_update(s2)
# print(s1)
# print(s2)

# --------------------------------------------------------------------------------------------------------
#difference/difference_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1.difference(s2)
# print(s1)
# s1.difference_update(s2)
# print(s1)
# print(s2)

# -----------------------------------------------------------------------------------------------------
# summetric_difference/summetric_difference_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1.symmetric_difference(s2)
# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)
# print(s2)

# -----------------------------------------------------------------------------------------------------
#isdisjoint / issubset / issuperset


# s1 = {1,2,3,4}
# s2 = {7,8,5,6}
# mathematically -> disjoint set aise sets hote jinme ek bhi item comman nhi hota
# print(s1.isdisjoint(s2))

# s1 = {1,2,3,4,5}
# s2 = {3,4,5}
# issubset --> koi part agar dusre set main exist karta hai toh usse subset kehta hai mtlb sub part of the set
# print(s2.issubset(s1))

# issuperset
# s1 = {1,2,3,4,5}
# s2 = {3,4,5}
# print(s1.issuperset(s2))

# --------------------------------------------------------------------------------------------------

#copy
# s1 = {1,2,3}
# s2 = s1.copy()
# print(s2)

# ----------------------------------------------------------------------------------
# frozenset
# frozen set is just an immutable version of a python set object
# Create a frozenset
# fs = frozenset([1,2,3])
# print(fs)
# what works and what does not
# works -->  all read functions
# does not work ---> write operations

# #2D set
# fs = frozenset([1,2,frozenset([2,3,5])])
# print(fs)
# -----------------------------------------------------------------------------
# set comprehension
# example
# s1 = set()
# s1 = {i ** 2  for i in range(1,11) if i > 5}
# print(s1)
