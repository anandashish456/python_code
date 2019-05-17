def new_decorator(func):

    def wrap_func():
        print("Code before real func()")
        func()
        print("Code after real func()")

    return wrap_func




@new_decorator
def function_need_decorator():
    print("I need decorator")


function_need_decorator()
