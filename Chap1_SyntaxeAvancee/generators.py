def fibonacci():
    a, b  = 0, 1
    while True:
        yield b
        c = a + b
        a = b
        b = c
    
for i in fibonacci():
    print(i)