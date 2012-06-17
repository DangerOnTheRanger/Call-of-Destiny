

def nested_property(func):

    property_args = {}
    property_args['doc'] = func.__doc__

    func_locals = func()
    property_args['fget'] = func_locals['get']
    property_args['fset'] = func_locals.get('set')
    property_args['fdel'] = func_locals.get('del_')

    return locals()


class Event(object):

    def __init__(self):
        self._listeners = set()

    def add_listener(self, listener):
        self._listeners.add(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

    def __contains__(self, listener):
        return listener in self._listeners

    def __add__(self, listener):

        self.add_listener(listener)
        return self

    def __sub__(self, listener):

        self.remove_listener(listener)
        return self


class Singleton(type):

    def __init__(cls, name, bases, dict):

        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kw):

        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)

        return cls.instance
