def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    total_time = time.time() - start
    print(f'Function {func.__name__} execution took: {total_time}')
    return result