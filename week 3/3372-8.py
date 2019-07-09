def f(x):
    if x <= -2:
        result = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        result = -x / 2
    elif 2 < x:
        result = (x - 2) ** 2 + 1
    return(result)