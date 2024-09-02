
list_of_cloud=["aws", "azure", "gcp", "OVH", "digital ocean"] # list -> data structure which can hold multiple values of different types

print(list_of_cloud)

#Add a new item in list
list_of_cloud.append("Oracle")  # append() -> add to end of list
print(list_of_cloud)

#Add a new item in list at specified location
list_of_cloud.insert(2, "alibaba")  #list index starts from 0,1,....
print(list_of_cloud)

# Find length of list
print(len(list_of_cloud))      

#Iterate list using for loop
for cloud in list_of_cloud:
    print(cloud)

# Print numbers in range of 1(n) to 11(n-1).
for i in range(1,11):
    print(i)