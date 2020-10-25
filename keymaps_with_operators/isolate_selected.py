import bpy
from zpy import register_keymaps
km = register_keymaps()


class VIEW3D_OT_localview_clickdrag(bpy.types.Operator):
    bl_description = "Toggle display of selected object(s) separately and centered in view"
    bl_idname = 'view3d.localview_clickdrag'
    bl_label = "Local View"
    bl_options = {'UNDO'}

    @classmethod
    def description(cls, context, properties):
        return cls.bl_description

    @classmethod
    def poll(cls, context):
        return bpy.ops.view3d.localview.poll()

    def execute(self, context):
        bpy.ops.view3d.localview(frame_selected=self.frame_selected)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if (event.value == 'PRESS'):
            # Wait until done dragging mouse around
            return {'RUNNING_MODAL'}
        return {'FINISHED'}

    frame_selected: bpy.props.BoolProperty(
        name="Frame Selected",
        description="Move the view to frame the selected objects",
        default=True,
    )


def register():
    # Isolate selected
    args = dict(name='3D View', type='TAB', shift=True)
    km.add('view3d.localview_clickdrag', **args, value='CLICK_DRAG', frame_selected=False)
    km.add('view3d.localview', **args, value='CLICK', frame_selected=True)


def unregister():
    km.remove()
