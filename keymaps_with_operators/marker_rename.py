import bpy
from zpy import register_keymaps
km = register_keymaps()


class MARKER_OT_rename_multiple(bpy.types.Operator):
    bl_description = "Rename selected time markers"
    bl_idname = 'zpy.rename_markers'
    bl_label = "Rename Marker(s)"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        markers = context.scene.timeline_markers
        count = len([m for m in markers if m.select])

        return (count > 1)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'name')

    def invoke(self, context, event):
        # This is essentially what the builtin marker renamer does
        # for m in context.scene.timeline_markers:
            # if m.select:
                # self.name = m.name
                # break
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        name = self.name
        for d in range((len(name))):
            name = name.replace(f"{{{'#' * d}}}", f"←┤m.frame:0{d}┤►")
        name = name.replace(
            "{", "{{").replace(
            "}", "}}").replace(
            '←┤', '{').replace(
            "┤►", '}')

        for m in context.scene.timeline_markers:
            if not m.select:
                continue
            m.name = name.format(m=m)
        return {'FINISHED'}

    name: bpy.props.StringProperty(
        name="Name",
        description="New name for markers"
        ".\nWrap a number sign (#) in brackets {##} to insert the marker's frame number",
        default="F_{##}",
        options=set({'SKIP_SAVE'}),
    )


def register():
    km.add('zpy.rename_markers', name='Markers', type='F2', value='PRESS')
    km.add('zpy.rename_markers', name='Markers', type='RIGHTMOUSE', value='DOUBLE_CLICK', any=True)
    km.add('marker.rename', name='Markers', type='F2', value='PRESS')
    km.add('marker.rename', name='Markers', type='RIGHTMOUSE', value='DOUBLE_CLICK', any=True)
