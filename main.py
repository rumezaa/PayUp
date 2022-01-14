import random
r = random.Random()
print("Hey! Having trouble deciding  who's gonna pay for food/drinks?\nUse this program to make that decision for you\n\n")

add_names = input("Enter the names of those who might potentially pay\nSeparate each name with a space\n\nNames: ")


#turning strings into lists
our_list = add_names.split()

num_of_names = len(our_list)

choice = r.randint(0,(num_of_names-1))

payUp = our_list[choice]

print(f"\n{payUp} get your wallet out! And maybe a tissue for your tears.")

input("\n\n\nPress enter to exit")
