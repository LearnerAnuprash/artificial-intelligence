#Implementing the concept of tree 

print("\nEnter the tree as in the example below:\n")

print("Root node: 1")
print("Create node: 1,2,L")
print("Create node: 1,3,R")
print("Create node: 2,4,L")
print("Create node: 2,5,R")
print("Create node: 3,6,R")
print("Create node: 6,7,R")
print("Create node: 7,8,L")
print("Create node: 7,9,R\n")


print("     1         ")
print("    / \        ")
print("   2   3       ")
print("  / \   \      ")
print(" 4   5   6     ")
print("          \    ")
print("           7   ")
print("          / \  ")
print("         8   9 ")

#List of node
treeData=[]

#Asking user for entering root node 
rootNode=input("Enter root node:")

#Loop until user types 'done'
while True:
    data=input("(Type 'done' to mark complete anytime ) Create node =>").lower()
    if(data=="done"):
        break
    parent, child, direction=data.split(",")
    treeData.append({
        "parent":parent.strip(),
        "child":child.strip(),
        "dir":direction.strip().upper()
    })

#Displaying the dictionary of tree in tabular form 
print("Displaying the dictionary of tree in tabular form ")
print("Parent\tChild\tDirection")
for node in treeData:
    print("\n"+node['parent']+"\t"+node['child']+"\t"+node['dir'])

print("\n")

#Displaying the nodes in tree-like form 




