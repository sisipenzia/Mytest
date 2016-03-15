class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)


     def pop(self):
         if self.isEmpty():
            print('Stack is empty')

         else:
            return self.items.pop()

     def peek(self):
         if self.isEmpty(self):
            print('Stack is empty')

         else:
            return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


open_file = open("index.html",'r')
contents = open_file.read()
open_file.close()
#print(len(contents))
tag_stack = Stack()
index = 0
for i in contents:
    index = index + 1
    if i == '<':
        x = index - 1
        pass
    if i == '>':
        y = index
        tag = contents[x:y]

        if tag[1] != '/':
            if len(tag) < 10:
                opening_tag = tag
                tag_stack.push(opening_tag)
                print("Tag added to stack : {}".format(opening_tag))
                pass
        else:
            closing_tag = tag
            tag_stack.pop()
            print("Tag removed from stack")
            pass
#if len(tag) > 0:
#    print("Some tags are not properly closed")
#else:
#    print("All tags are properly closed")






