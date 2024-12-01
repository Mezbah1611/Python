class InvalidVoteExcepiton(Exception):
    
    pass

try:
    age = int(input("Ënter your Age : "))
    if age < 18 :
        raise InvalidVoteExcepiton
    
except InvalidVoteExcepiton:
    print("You are not eligibe for vote")

else:
    print("You are eligible for vote ")