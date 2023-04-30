class SingletonObject(object):
    class __singeletonObject():
        
        
        def __init__(self) -> None:
            self.val = None

        def __str__(self) -> str:
            return f"{self, self.val}"
        
        # write your function here

    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__singeletonObject

        return SingletonObject.instance
        
    def __getattribute__(self, name):
        return getattr(self.instance, name)
    
    def __setattr__(self, name):
        return setattr(self.instance, name)