# https://developer.blender.org/T72611
# Fixed but leaving in with alternate hotkey (alt + x)
import bpy
from zpy import register_keymaps
km = register_keymaps()


class OP_OT_tmp_xray_toggle(bpy.types.Operator):
    bl_description = ""
    bl_idname = 'zpy.toggle_xray'
    bl_label = "Toggle In Front"
    # bl_options = {'UNDO'}

    @classmethod
    def description(cls, context, properties):
        return cls.bl_description

    @classmethod
    def poll(cls, context):
        return context.object

    def execute(self, context):
        # Alt+Z does bone x-ray toggle, in Weight Paint

        # if context.mode == 'PAINT_WEIGHT':
            # for ob in context.selected_objects:
                # if ob.mode == 'POSE':
                    # ob.show_in_front = not(ob.show_in_front)
        # else:
        context.object.show_in_front = not(context.object.show_in_front)

        return {'FINISHED'}


def register():
    km.add(OP_OT_tmp_xray_toggle, name='3D View', type='X', value='PRESS', alt=True)


def unregister():
    km.remove()
