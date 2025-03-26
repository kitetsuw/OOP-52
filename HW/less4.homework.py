def uppercase(func):
    def wrapper():
        result = func()
        if result:
            return result.upper()
        return result
    return wrapper

@uppercase
def say_hello():
    return "Привет!"

print(say_hello())
