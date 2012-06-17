import panda3d.core

import component
import datatypes


class TransformComponent(component.Component):

    manager = TransformManager

    def __init__(self):

        self._position_vector = panda3d.core.Vec3()
        self._positional_velocity = panda3d.core.Vec3()

        self._rotation_vector = panda3d.core.Vec3()
        self._rotational_velocity = panda3d.core.Vec3()

        self._scale_vector = panda3d.core.Vec3()

    @datatypes.nested_property
    def position():

        def get(self):
            return self._position_vector

        def set(self, position):

            if isinstance(position, tuple):

                assert len(position) == 3
                self._position_vector.setPos(*position)

            else:
                self._position_vector.setPos(position)

        return locals()

    @datatypes.nested_property
    def rotation():

        def get(self):
            return self._rotation_vector

        def set(self, rotation):

            if isinstance(rotation, tuple):

                assert len(rotation) == 3
                self._position_vector.setPos(*rotation)

            else:
                self._position_vector.setPos(rotation)

        return locals()

    @datatypes.nested_property
    def scale():

        def get(self):
            return self._scale_vector

        def set(self, scale):

            if isinstance(scale, tuple):

                assert len(scale) == 3
                self._scale_vector.setPos(*scale)

            else:
                self._scale_vector.setPos(scale)

        return locals()

    @datatypes.nested_property
    def positional_velocity():

        def get(self):
            return self._positional_velocity

        def set(self, velocity):

            if isinstance(velocity, tuple):

                assert len(velocity) == 3
                self._positional_velocity.setPos(*velocity)

            else:
                self._positional_velocity.setPos(velocity)

        return locals()

    @datatypes.nested_property
    def rotational_velocity():

        def get(self):
            return self._rotational_velocity

        def set(self, velocity):

            if isinstance(velocity, tuple):

                assert len(velocity) == 3
                self._rotational_velocity.setPos(*velocity)

            else:
                self._rotational_velocity.setPos(velocity)

        return locals()


class TransformManager(component.ComponentManager):

    def _update_component(self, transform):

        transform.position += transform.positional_velocity
        transform.rotation += transform.rotational_velocity
