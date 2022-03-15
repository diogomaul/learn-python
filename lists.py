my_list = ["January", "February", "March"]
print (my_list)
print (f"The second month ofthe year is {my_list[1]}")

my_list.append("April")
print (my_list)

#remove one that you specify
my_list.remove("February")
print (my_list)

#remove the last
my_list.pop()
print (my_list.pop())
print (my_list)

