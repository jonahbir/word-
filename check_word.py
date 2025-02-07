def word(s):
    count_upper=0
    count_lower=0
    for i in s:
        if i.isupper():
            count_upper+=1
        else:
            count_lower+=1
    if count_upper>count_lower:
        return s.upper()
    else:
        return s.lower()
string=input()
print(word(string))

