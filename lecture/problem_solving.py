#Write a function to remove duplicated character from a string

# def rem_dup_char(words):
#     for word in words:
#         if words.count(word)>2:
#             continue
#         else:
#             print(word)

# word ="chaccal is well"

# rem_dup_char(word)


#write a function to return the first occurence in a string of 3 of the same charactere
#consecutive, or None if there are no 3 consecutive character

def count_triples(string):
    # list_string = string.split()
    # # print(list_string)
    # for chars in list_string:
    #     if len(chars)==3:
    #         for char in chars:
    #             if chars.count(char) == 3:
    #                 print(char, end='')

    for i in range(0, len(string)-2):
        if string[i]==string[i+1] and string[i]==string[i+2]:
            return string[i:i+3]
            

string1 ="I am a member of the AAA"
string2 = "the fat cat sat om the mat"
string4 = "you will count 666"
string3 = "aardvark"
string5 = "help!!!!"
print(count_triples(string3))
print(count_triples(string1))
print(count_triples(string2))
print(count_triples(string4))
print(count_triples(string5))