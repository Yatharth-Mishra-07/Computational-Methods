def function(expr: str):
    #converts a string to a function
    def f(x):
        return eval(expr)
    return f

def bisxn(func, a, b, accuracy = 1e-6, max_iterations = 200):

    if func(a) * func(b) >= 0:
        raise ValueError("f(a) and f(b) have the same sign")
    
    iteration = 1
    while iteration <= max_iterations:
        c = (a + b) / 2.0
        fc = func(c)
        print(f"Iteration {iteration}: a={a:.6f}, b={b:.6f}, c={c:.6f}, f(c)={fc:.6f}")

        if abs(fc) < accuracy or (b - a) / 2.0 < accuracy:
            print(f"\n root at x = {c:.6f}")
            return c

        if func(a) * fc > 0:

            a = c
        else:

            b = c

        iteration += 1

    print("\n max iterations reached, no root found.")

    return (a + b) / 2.0

if __name__ == "__main__":

    expr = input("f(x) = ")
    func = function(expr)

    a = float(input("Enter interval start 'a': "))

    b = float(input("Enter interval end 'b': "))

    accuracy_ = float(input("accuracy (default 1e-6): ") or 1e-6)



    try:
        root = bisxn(func, a, b, accuracy = accuracy_)

    except Exception as e:
        print(f"Error: {e}")