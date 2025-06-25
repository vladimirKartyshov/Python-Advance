number_list = [11, 32, 35, 48.32]
print(number_list)

some_list = [66, 67.999, "hello"]
print(some_list)
print(len(some_list))
print(some_list[1])

another_list = some_list[:2]
print(another_list)

some_list[2] = "hi"
print(some_list)

new_list = another_list + some_list
print(new_list)

# Adding items
new_list.append("new item")
new_list.insert(0, "start")
new_list.insert(2, 13)
print(new_list)

# Removing items
new_list.pop()
new_list.pop(0)

deleted_item = new_list.pop()
deleted_item = new_list.remove(66)

print(new_list)
print(deleted_item)

number_list2 = [22, -544, 66, 77]
letter_list = ["a", "r", "w", "z"]

number_list2.sort()
letter_list.sort()

x = number_list2.sort()
y = letter_list.sort()

print(number_list2)
print(letter_list)
print(x)
print(y)

#чтобы сохранить отсортированные данные
letter_list.sort()
new_list2 = letter_list

print(new_list2)

number_list2.reverse()
letter_list.reverse()

print(number_list2)
print(letter_list)

number_list2.append(letter_list)
print(number_list2)




