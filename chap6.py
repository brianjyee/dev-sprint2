# Enter your answrs for chapter 6 here
# Name: Brian Yee


# Ex. 6.6
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif first(s) == last(s):
        return is_palindrome(middle(s))
    else:
        return False

#print is_palindrome('abba')

# Ex 6.8
def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)

#print gcd(20,8)
