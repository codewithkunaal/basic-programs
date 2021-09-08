def rem ( string,word):
    new = string.replace(word,"was")
    return new.strip()
m = "    above is a new string  "
# cm = rem(m,"is")
print(rem(m,"is"))
