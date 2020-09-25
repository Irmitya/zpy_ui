import bpy
from bpy.types import Operator
from zpy import utils, register_keymaps
km = register_keymaps()


class sample_jitter:
    bl_description = "Add keyframes on every frame between the selected keyframes (as jitter type)"
    bl_label = "Sample Keyframes"
    bl_options = {'UNDO'}

    @classmethod
    def description(cls, context, properties):
        return cls.bl_rna.description

    @classmethod
    def poll(cls, context):
        return cls.op.poll(context.copy())

    def invoke(self, context, event):
        return self.function(context, 'INVOKE_DEFAULT')

    def execute(self, context):
        return self.function(context, 'EXEC_DEFAULT')

    def function(self, context, invoke):
        utils.update_keyframe_points(context)

        curves = dict()

        for fc in context.editable_fcurves:
            curves[fc] = dict()

            for key in fc.keyframe_points:
                if key.select_control_point:
                    curves[fc][tuple(key.co)] = key.type

        exit = self.op(invoke)
        if exit == {'CANCELLED'}:
            return exit

        for fc in context.editable_fcurves:
            for key in fc.keyframe_points:
                if key.select_control_point:
                    if tuple(key.co) not in curves[fc]:
                        key.type = 'JITTER'

        return exit


class GRAPH_OT_sample_jitter(Operator, sample_jitter):
    bl_idname = 'graph.sample_jitter'
    op = bpy.ops.graph.sample


class ACTION_OT_sample_jitter(Operator, sample_jitter):
    bl_idname = 'action.sample_jitter'
    op = bpy.ops.action.sample


def register():
    args = dict(type='O', shift=True, alt=True)
    km.add(GRAPH_OT_sample_jitter, name='Graph Editor', **args)
    km.add(ACTION_OT_sample_jitter, name='Dopesheet', **args)


def unregister():
    km.remove()
