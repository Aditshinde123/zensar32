def begin_end(fun):
    def inner(x,y):
        fun(x,y)

    return inner





