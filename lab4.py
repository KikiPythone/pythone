
def limit_calls(max_calls):
    def decorator(func):
        #  счетчик 
        func.calls = 0

        # вызов ориг ф
        def wrapper(*args, **kwargs):
            if func.calls >= max_calls: 
                raise ValueError(f"Функция {func.__name__} была вызвана больше {max_calls} раз.")
            func.calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
@limit_calls(2)
def unique_values():
    seen = set()
    @limit_calls(4)
    def inner(values):
        return [value for value in values if value not in seen and not seen.add(value)]
    return inner

unique_values_limited = unique_values()
print(unique_values_limited([1, 2, 2, 3]))  
print(unique_values_limited([4, 5, 5, 6])) 
print(unique_values_limited([7, 8, 9]))     
print(unique_values_limited([1, 2, 3]))    
#print(unique_values_limited([1, 2, 3]))     
unique_values_limited = unique_values() 
unique_values_limited = unique_values()
unique_values_limited = unique_values()