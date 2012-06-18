import datatypes


class ComponentManager(object):

    __metaclass__ = datatypes.Singleton

    _components = {}
    task_manager = None
    running = False

    @classmethod
    def set_task_manager(cls, task_manager):
        cls.task_manager = task_manager

    def start_update_loop(self):

        assert self.task_manager is not None

        if self.running is False:

            self.running = True
            self.task_manager.add(self._update_task, 'component manager task')

    def add_component(self, component):

        assert self._components.get(component.uuid) is None

        if self.running is False:
            self.start_update_loop()

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

    name = None
    required_components = []

    def init(self, manager):
        self.manager = manager

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


class ComponentFactory(object):

    registered_components = {}

    @classmethod
    def make(cls, component_name, *args, **kwargs):

        try:

            component_cls = cls.registered_components[component_name]
            return component_cls(*args, **kwargs)

        except KeyError:
            raise NoSuchComponentException(component_name)

    @classmethod
    def register_component(cls, component_cls):

        assert component_cls.name not in cls.registered_components
        cls.registered_components[component_cls.name] = component_cls


class ComponentException(Exception):
    pass


class NoSuchComponentException(ComponentException):
    pass
