class Descriptor:

    def __set_name__(self, owner, name):
        print('calling class prop: ', name)
        self.priv_name = '_' + name

    def __get__(self, obj, objtype=None):
        print('getting value:')
        return getattr(obj, self.priv_name)


    def __set__(self, obj, value):
        print('setting to:', value)
        setattr(obj, self.priv_name, value)


class SomeClass:

    var = Descriptor()


class Obj:

    @property            # first decorate the getter method
    def attribute(self): # This getter method name is *the* name
        return self._attribute

    @attribute.setter    # the property decorates with `.setter` now
    def attribute(self, value):   # name, e.g. "attribute", is the same
        self._attribute = value   # the "value" name isn't special


class Count(object):

    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax
        self.current=None

    def __getattr__(self, item):
        print('calling __getattr__')
        self.__dict__[item]=0
        return 0

    def __getattribute__(self, item):
        print('calling getattribute')
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self,item)

class Contact(object):

    def __init__(self, first_name=None, last_name=None, 
                 display_name=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = display_name
        self.email = email


    def set_email(self, value):
        if '@' not in value:
            raise Exception("This doesn't look like an email address.")
        self._email = value

    def get_email(self):
        return self._email

    email = property(get_email, set_email)
