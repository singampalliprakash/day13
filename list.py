"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e .
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list."""
if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        command=input().strip().split()
        if command[0]=="insert":
            index=int(command[1])
            value=int(command[2])
            list.insert(index,value)
        elif command[0]=="print":
            print(list)
        elif command[0]=="remove":
            val=int(command[1])
            list.remove(val)
        elif command[0]=="append":
            na=int(command[1])
            list.append(na)
        elif command[0]=="sort":
            list.sort()
        elif command[0]=="pop":
            list.pop()
        elif command[0]=="reverse":
            list.reverse()
        