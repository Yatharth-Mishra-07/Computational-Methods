import math

allowed_fx = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}

def function(expr: str):
    # Convert string to function
    def f(x):
        allowed = {"x": x, **allowed_fx}
        return eval(expr, {"__builtins__": {}}, allowed)
    return f


def newton_raphson(func, Dfunc, x0, accuracy=1e-6, max_iterations=200):
    iteration = 1

    while iteration <= max_iterations:

        y = func(x0)
        Dy = Dfunc(x0)

        if Dy == 0:
            raise ZeroDivisionError("Derivative became zero")

        x1 = x0 - y / Dy
        y1 = func(x1)

        print(
            f"Iteration {iteration}: "
            f"x0={x0:.6f}, x1={x1:.6f}, f(x1)={y1:.6f}"
        )

        if abs(y1) < accuracy or abs(x1 - x0) < accuracy:
            print(f"\n root at x = {x1:.6f}")
            return x1

        x0 = x1
        iteration += 1

    print("\n max iterations reached, no root found.")
    return x0


if __name__ == "__main__":

    expr = input("f(x) = ")
    expr = expr.replace("^", "**")

    Dexpr = input("f'(x) = ")
    Dexpr = Dexpr.replace("^", "**")

    func = function(expr)
    Dfunc = function(Dexpr)

    x0 = float(input("Enter initial guess x0: "))

    accuracy_ = float(input("accuracy (default 1e-6): ") or 1e-6)

    try:
        root = newton_raphson(func, Dfunc, x0, accuracy=accuracy_)
    except Exception as e:
        print(f"Error: {e}")