n = int(input())
if n>=18:
    print("You are eligible to vote")
    if n>=21:
        print("You are eligible candidate for president")
    else:
        print("You are not eligible candidate for president")
else:
    print("You are not eligible to vote")
    print("You are not eligible candidate for president")