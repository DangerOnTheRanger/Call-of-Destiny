import component


class Entity(object):

    def __init__(self):
        self._components = {}

    def add_component(self, new_component):

        assert new_component.uuid not in self._components

        for required_component in new_component.required_components:
            self.add_component(component.ComponentFactory.make(required_component))

        self._components[new_component.uuid] = component
        new_component.entity = self
        new_component.register()

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
