class Class(object):
    def __dir__(self):
        attributes = self.__dict__.keys()
        nounderscore = filter(lambda x: not x.startswith("_"), dir(self.__class__))
        methods = filter(lambda x: callable(getattr(self, x)), nounderscore)
        for i,m in enumerate(methods):
            methods[i] = m + "()"
            nounderscore.remove(m)

        # We add the remaining nounderscore's in case they didn't show up in
        # the __dict__. We also group methods and attributes together for
        # readability.
        dirlist = [{"methods":methods}, {"attributes": attributes+nounderscore}]
        return dirlist

class MyClass(Class):
    some_class_variable = True

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

obj = MyClass(5,7)
print(dir(obj))
