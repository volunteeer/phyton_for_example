tvshow_list = ["show1","show2","show3","show4"]
for i in tvshow_list:
    print(tvshow_list.index(i), i)
new_show = input("Add another show: ")
new_position = int(input("Add prevered position in the list"))
tvshow_list.insert(new_position, new_show)
for i in tvshow_list:
    print(tvshow_list.index(i), i)
