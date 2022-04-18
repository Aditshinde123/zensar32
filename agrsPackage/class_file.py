def StartStopwitharguement(name1,name2,name3):
    print(name1,name2,name3)
    def function(func):
        def inner(*args):
            print("Welcome.....")
            func(*args)
            print("End.....")

        return inner
    return function