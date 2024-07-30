inpList: list[str] = []
while True:
    num: str = input("Enter a value: ")
    if num == "":
        break
    else:
       inpList.append(num)
print(f"Here's the list: {inpList}")