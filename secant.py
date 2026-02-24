import math

allowed_fx = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}

def function(expr: str):
    # Convert string to function
    def f(x):
        allowed = {"x": x, **allowed_fx}
        return eval(expr, {"__builtins__": {}}, allowed)
    return f


def secant(func, x0, x1, accuracy=1e-6, max_iterations=200):
    y0 = func(x0)
    y1 = func(x1)

    iteration = 1

    while iteration <= max_iterations:

        if y1 - y0 == 0:
            raise ZeroDivisionError("Division by zero in secant formula")

        x2 = x1 - y1 * (x1 - x0) / (y1 - y0)
        y2 = func(x2)

        print(
            f"Iteration {iteration}: "
            f"x0={x0:.6f}, x1={x1:.6f}, x2={x2:.6f}, f(x2)={y2:.6f}"
        )

        if abs(y2) < accuracy or abs(x2 - x1) < accuracy:
            print(f"\n root at x = {x2:.6f}")
            return x2

        x0, y0 = x1, y1
        x1, y1 = x2, y2

        iteration += 1

    print("\n max iterations reached, no root found.")
    return x1


if __name__ == "__main__":

    expr = input("f(x) = ")
    func = function(expr)
    
    x0 = float(input("Enter x0: "))
    x1 = float(input("Enter x1: "))

    accuracy_ = float(input("accuracy (default 1e-6): ") or 1e-6)

    try:
        root = secant(func, x0, x1, accuracy=accuracy_)
    except Exception as e:
        print(f"Error: {e}")