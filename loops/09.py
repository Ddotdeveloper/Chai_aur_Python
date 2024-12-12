items = ["apple", "banana", "orange", "mango"]
unique_items = set()
for item in items :
    if item in unique_items : 
        print("Duplicate")
        break
    else : 
        unique_items.add(item)
