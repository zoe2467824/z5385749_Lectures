d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers"
    }
for key_value_tuple in d.items():
    print(key_value_tuple)


for i in range (5,0):
    print ("This will not execute because start is greater than stop. ")

for i in range (5,0,-1):
    print("This message will self-destruct in {} secs...".format(i))


letters = ["a","b","c","d","e"]
print (f"letters = {letters}")
for i, x in enumerate (letters):
    print (f"letters [{i}]--> {x}")

the_sum = 0
i = 1
while i <= 100:
    the_sum = the_sum + 1
    i = i + 1
print(the_sum)