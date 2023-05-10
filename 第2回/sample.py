input_line = int(input())

value = int(1)

for i in range(2, input_line + 1):
    value *= i
    while value % 10 == 0:
        value //= 10
    value %= 100000000000

value = str(value)

# valueの一番最後から10文字目までを表示する
value = value[-9:]

print(int(value))
