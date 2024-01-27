def word_count(string):
    # Here we are removing the spaces from start and end,
    # and breaking every word whenever we encounter a space
    # and storing them in a list. The len of the list is the
    # total count of words.
    return(len(string.strip().split(" ")))
#taking user input using input() method
string = input("Enter your sentence: ")
print(string)
#print the string and measure the no. of words using word_count() method
print(format(string),"has total words:",word_count(string))
