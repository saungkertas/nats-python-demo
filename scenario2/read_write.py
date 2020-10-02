import todolist_pb2 as TodoList

my_list = TodoList.TodoList()
my_list.owner_id = 1234

# ...

with open("./serializedFile", "wb") as fd:
    fd.write(my_list.SerializeToString())


my_list = TodoList.TodoList()
with open("./serializedFile", "rb") as fd:
    my_list.ParseFromString(fd.read())

print(my_list)