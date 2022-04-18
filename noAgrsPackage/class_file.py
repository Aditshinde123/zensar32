class StartStop:
    def _init_(self,function):
        self.function = function
    def _call_(self,*args):
        self.function(*args)