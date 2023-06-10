# BootCamp Q1 - Combining all index of list to create a whole number
def number(myNumber:list[int]):
    total = 0
    multiply = 1
    for i in reversed(myNumber):
        value = i * multiply 
        total += value
        multiply *= 10

    print(total)

if __name__ == "__main__":
	number([8, 3, 5, 1])

