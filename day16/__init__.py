def decorator(*args, **kwargs):
    def wrapper(func):
        def inner(*args, **kwargs):
            # 在核心函数之前添加额外的功能
            result = func()
            #             在核心函数之后添加额外的功能
            return result

        return inner

    return wrapper
