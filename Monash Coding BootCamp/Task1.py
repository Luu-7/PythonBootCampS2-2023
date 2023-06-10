# BootCamp Q1 - List to 
def number(myNumber:list[int]):
    final = 0
    multiply = 1
    for i in reversed(myNumber):
        add = i * multiply 
        final += add
        multiply *= 10

    print(final)

if __name__ == "__main__":
	number([8, 3, 5, 1])

