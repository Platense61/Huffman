"""
This function aims to parse the codeword file. 
It uses the split(" -- ") function to return a list of the character and the code ex. [[!], 01000101010]
within the for loop the list from above gets appended to my_list which eventually is returned

Returns a list of lists
"""
def encode_parse(filePath):
    file = open(filePath, "r")
    lines = file.readlines()

    my_list = []
    for x in lines:
        word = x.split(" -- ")
        my_list.append(word)
    return my_list

"""
The encode function will use a dictionary to map every char to its respectful binary code (00010111)

"""
def encode(filePath):
    codes = encode_parse(filePath)
    my_map = {}
    my_map["\n"] = "0001"
    for x in codes[1:len(codes)]:
        my_map[x[0][1]] = x[1].replace("\n","")

    #Now we must write the encrypted message to the encrypted.txt file
    fileWrite = open("encrypted.txt", 'w')
    with open("hollow.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            fileWrite.write(my_map[c])
    f.close()
    print("Hollow.txt has been encrypted using huffman encoding. Encrypted file is located in encrypted.txt")


"""
This function will decrypt the file we created with the function encode (from above)
similar to encode we parse the codeword file and create a map similar to encode but this time the 
binary strings are the keys and the chars are the values of the map (was flipped in encode)
we then read the encrypted file char by char and append each char to a string with each pass trying to grab an item from the map.
if we cant grab an item from the map we know we havent actually found a valid binary sequence so we continue appending to this string untill we do
"""
def decrypt(filePath):
    codes = encode_parse(filePath)
    my_map = {}
    my_map["0001"] = "\n"

    for x in codes[1:len(codes)]:
        my_map[x[1].replace("\n","")] = x[0][1]
    
    fileWrite = open("decrypt.txt", 'w')
    fileRead = open("encrypted.txt", 'r')
    str = ""
    with open("encrypted.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            str += c
            value = my_map.get(str)
            if value is not None:
                fileWrite.write(value)
                str = ""
    fileWrite.close()
    fileRead.close()
    print("Decrypted message is now located in decrypt.txt")


encode("codewords.txt")
decrypt("codewords.txt")