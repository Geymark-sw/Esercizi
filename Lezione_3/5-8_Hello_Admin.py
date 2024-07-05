users: list[str] = ["pippo","pluto","admin","topolino","jhon cena"]


if len(users) == 0:
    print(f"We need to find some users!!!")


for i in users:

    if i == "admin":

        print(f"Hello {i}, would you like to see a status report?")

    else:

        print(f"Hello {i}, thank you for logging in")