def add(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return None
    return x + y


res = add(1, 3)
print(f"Function returns {res}")
