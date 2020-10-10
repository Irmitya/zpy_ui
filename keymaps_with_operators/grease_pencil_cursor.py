import bpy
from zpy import register_keymaps
km = register_keymaps()


# class GPENCIL_OT_set_cursor(bpy.types.Operator):
    # bl_description = ""
    # bl_idname = 'gpencil.cursor3d'
    # bl_label = "Set 3D Cursor (Grease Pencil)"
    # # bl_options = {}
        # # enum set in {'REGISTER', 'UNDO', 'UNDO_GROUPED', 'BLOCKING', 'MACRO', 'GRAB_CURSOR', 'PRESET', 'INTERNAL'}
    # # bl_undo_group = ""

    # @classmethod
    # def description(cls, context, properties):
        # return cls.bl_description

    # @classmethod
    # def poll(cls, context):
        # if bpy.ops.view3d.cursor3d.poll(context.copy()):
            # return context.mode in (
                # 'OBJECT',
                # # 'EDIT_GPENCIL',
                # 'PAINT_GPENCIL',
                # 'SCULPT_GPENCIL',
                # 'VERTEX_GPENCIL',
                # 'WEIGHT_GPENCIL',
            # )

    # def invoke(self, context, event):
        # return bpy.ops.view3d.cursor3d('INVOKE_DEFAULT')

    # def execute(self, context):
        # return bpy.ops.view3d.cursor3d()


def register():
    # km.add(GPENCIL_OT_set_cursor, name='Grease Pencil', type='RIGHTMOUSE')
    km.add('view3d.cursor3d', name='Grease Pencil Stroke Paint (Draw brush)', type='RIGHTMOUSE')


def unregister():
    km.remove()
