import component


class Entity(object):

    def __init__(self):
        self._components = {}

    def add_component(self, component):

        assert component.uuid not in self._components
        self._components[component.uuid] = component
        component.entity = self
        component.register()

    def remove_component(self, uuid):

        try:

            component = self._components[uuid]
            component.manager.remove_component(uuid)
            del self._components[uuid]

        except KeyError:
            raise component.NoSuchComponentException(uuid)

    def __getattr__(self, name):

        if name in self.__dict__:
            return self.__dict__[name]

        for component in self._components:
            if component.name == name:
                return component

        raise AttributeError(name)
