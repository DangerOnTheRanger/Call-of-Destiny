import panda3d.core
import direct.actor.Actor

import component
import datatypes


class TransformManager(component.ComponentManager):

    def _update_component(self, transform):

        transform.position += transform.positional_velocity
        transform.rotation += transform.rotational_velocity


class TransformComponent(component.Component):

    manager = TransformManager
    name = 'transform'

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
                self._position_vector.setPos(position[0], position[1], position[2])

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
                self._position_vector.setPos(rotation[0], rotation[1], rotation[2])

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
                self._scale_vector.setPos(scale[0], scale[1], scale[2])

            else:
                self._scale_vector.setPos(scale[0], scale[1], scale[2])

        return locals()

    @datatypes.nested_property
    def positional_velocity():

        def get(self):
            return self._positional_velocity

        def set(self, velocity):

            if isinstance(velocity, tuple):

                assert len(velocity) == 3
                self._positional_velocity.setPos(velocity[0], velocity[1], velocity[2])

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
                self._rotational_velocity.setPos(velocity[0], velocity[1], velocity[2])

            else:
                self._rotational_velocity.setPos(velocity)

        return locals()


component.ComponentFactory.register_component(TransformComponent)


class MeshManager(component.ComponentManager):

    def _update_component(self, mesh):

        mesh.model.setPos(mesh.entity.transform.position)
        mesh.model.setHpr(mesh.entity.transform.rotation)
        mesh.model.setScale(mesh.entity.transform.scale)


class MeshComponent(component.Component):

    manager = MeshManager
    name = 'mesh'
    required_components = ['transform']

    def __init__(self, render_node, model_path):

        self._model = direct.actor.Actor.Actor(model_path)
        self._model.reparentTo(render_node)

    @datatypes.nested_property
    def model():

        def get(self):
            return self._model

        return locals()


component.ComponentFactory.register_component(MeshComponent)
