data = [1, 2, 2, 3, 4, 4, 4, 5]

counts = {}
max_item = None
max_count = 0

for item in data:
    # 1. Update the count for this item
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
    
    # 2. Check if this item is now the most frequent
    if counts[item] > max_count:
        max_count = counts[item]
        max_item = item

print(f"Highest occurrence: {max_item} (found {max_count} times)")
