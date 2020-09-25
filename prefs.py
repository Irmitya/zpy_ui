import bpy
from zpy import utils


class User_Interface(bpy.types.AddonPreferences, utils.Preferences):
    bl_idname = __package__  # __name__

    def draw(self, context):
        layout = self.layout
        self.draw_keymaps(context)

    camera_dof_target_type: bpy.props.BoolProperty(
        name="Camera: DoF Target type",
        default=True,
    )
