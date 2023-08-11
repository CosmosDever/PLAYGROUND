def group_fruits_and_vegetables(items_list):

    fruits = []
    vegetables = []
    for item in items_list:
        if is_fruit(item):
            fruits.append(item)
        elif is_vegetable(item):
            vegetables.append(item)
        else:
            print(f"Warning: '{item}' is neither a fruit nor a vegetable!")


    grouped_dict = {
        'fruits': fruits,
        'vegetables': vegetables
    }

    return grouped_dict

def is_fruit(item):
    fruits_list = ['apple','banana','orange','mango','strawberry']
    return item.lower() in fruits_list

def is_vegetable(item):
    vegetables_list = ['carrot','broccoli','tomato','spinach','cucumber']
    return item.lower() in vegetables_list

items_list=['Apple','Banana','Orange','Mango','shoes','Carrot','Broccoli','Tomato','Spinach']
print(group_fruits_and_vegetables(items_list))