import bpy


def draw(self, context):
    obj = context.active_object
    if not obj:
        return
    layout = self.layout

    layout.prop(obj, 'show_in_front', toggle=True)
    layout.prop(obj, 'display_type', text="")
    # if context.mode in ('EDIT_ARMATURE', 'POSE'):
    if obj.type == 'ARMATURE':
        layout.prop(obj.data, 'display_type', text="")


def register():
    bpy.types.VIEW3D_HT_tool_header.append(draw)


def unregister():
    bpy.types.VIEW3D_HT_tool_header.remove(draw)
