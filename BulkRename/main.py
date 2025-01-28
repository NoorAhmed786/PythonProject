import os # Import the os module

def main():
    i = 0
    path = "D:/python/"  # Path to the directory containing the files to be renamed
    for filename in os.listdir(path): # Loop through all the files in the directory 
        # Construct source and destination paths
        my_dest = "img" + str(i) + ".jpg"
        my_source = os.path.join(path, filename)
        my_dest = os.path.join(path, my_dest)

        # Rename the file
        os.rename(my_source, my_dest)
        i += 1

if __name__ == "__main__":# Call the main function
    main()














# # Additional code for testing loops
# list1 = ['I am ', 'You are ']
# list2 = ['healthy', 'fine', 'geek']
# list2_size = len(list2)

# for item in list1:
#     print("start outer for loop")
#     i = 0
#     while i < list2_size:
#         print(item, list2[i])
#         i += 1
#     print("end for loop")

# for i in range(2, 4):
#     for j in range(1, 11):
#         print(i, "*", j, "=", i * j)
#     print()
