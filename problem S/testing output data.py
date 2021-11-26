with open("input.txt", "r") as inp, open("output.txt", "r") as out:
    input = [i.strip() for i in inp]
    output = [i.strip() for i in out]
    if input == output[::-1]:
        print("Test is OK")
    else:
        print("Test Denied")
