import datatypes


class ComponentManager(object):

    __metaclass__ = datatypes.Singleton

    _components = {}

    def set_task_manager(self, task_manager):
        task_manager.add(self._update_task, 'component manager task')

    def add_component(self, component):

        assert self._components.get(component.uuid) is None
        self._components[component.uuid] = component
        component.init(self)

    def remove_component(self, uuid):

        try:

            component = self._components[uuid]
            del self._components[uuid]
            component.destroy()

        except KeyError:
            raise NoSuchComponentException(uuid)

    def _update_task(self, task):

        for component in self._components.itervalues():
            self._update_component(component)

        return task.cont

    def _update_component(self, component):
        pass


class Component(object):

    manager = None
    _entity = None

    def init(self):
        raise NotImplementedError

    def destroy(self):
        pass

    def register(self):

        assert self.manager is not None
        self.manager().add_component(self)

    @datatypes.nested_property
    def entity():

        def get(self):
            return self._entity

        def set(self, entity):
            self._entity = entity

        return locals()


class ComponentException(Exception):
    pass


class NoSuchComponentException(ComponentException):
    pass
