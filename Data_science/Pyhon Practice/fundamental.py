# n = int(input("Enter a number :"))
# for i in range(0,n):
#     for j in range(n ,n):
#         print(j,end ="")
#     print()


text = "apple banana mango orange"
words = text.split()
key = "mango"
found = False
for i in range(len(words)):
    if words[i] == key:
        print("Word found at index:", i)
        found = True
        break

if not found:
    print("Word not found")


