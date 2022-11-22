my_str = 'This is not a test'
print(my_str)

split_str = my_str.split()
print(split_str)

reversed_elements = []
for element in split_str:
	reversed_elements.append(element[::-1])
print(reversed_elements)

new_str = ' '.join(reversed_elements)
print(new_str)
