def outer(a):
    b = 2
    def inner():
        c = a + b
        print("c =", c)
    return inner

func = outer(3)
func()
