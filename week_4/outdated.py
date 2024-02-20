month, day, year = input("Date: ").split("/")
monthli = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
if month.isalpha():
    for i in monthli:
        if i == str(month).capitalize():
            month = (monthli.index(i)+1)
            # print(i)
elif month.isnumeric():
    if 0>month>12:
        ...
print(f"{year}-{month}-{day}")