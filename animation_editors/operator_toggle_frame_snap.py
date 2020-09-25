import bpy


class TOGGLE_OT_animation_snap(bpy.types.Operator):
    bl_description = "Toggle auto frame snapping for active area"
    bl_idname = 'zpy.toggle_anim_snap'
    bl_label = "Toggle Auto Snap"

    @classmethod
    def poll(self, context):
        return context.space_data

    def execute(self, context):
        st = context.space_data
        st.auto_snap = ('NONE', 'FRAME')[st.auto_snap == 'NONE']

        return {'FINISHED'}
