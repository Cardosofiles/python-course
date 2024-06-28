import winsound
x = 10
while x >= 0:
    print(x)
    x = x - 1
winsound.Beep(2500, 500)

number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1