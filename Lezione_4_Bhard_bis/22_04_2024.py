def is_palindrome(x: int) -> bool:

    
    s: str = str(x)
    i: int = 0

    for i in range(len(s)//2):

        if s[i]!= s[len(s) - (i+1)]:

            return False
        i += 1
    return True

print(is_palindrome("amoroma"))
