import bpy
from zpy import Is, Get, is27, is28, utils


class PROPS_PT_camera(bpy.types.Panel):
    bl_label = "Toggle Camera props"
    bl_options = {'DEFAULT_CLOSED', 'HIDE_HEADER'}
    bl_region_type = 'TOOLS'
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(self, context):
        if is27: return
        return Is.camera(context.object)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout.column(align=True)

        camera = context.object.data
        prefs = utils.prefs(__package__)

        # col = layout.row(align=True)
        # display_camera = prefs.get("Toggle Camera props")
        # if display_camera:
        #     draw_camera(context, col.row(), obj)
        # col = col.row()
        # col.emboss = 'PULLDOWN_MENU'
        # prefs.prop(
        #     col, "Toggle Camera props", icon='CAMERA_DATA',
        # )

        # dof_obj = camera.dof.focus_object
        args = dict(text="", toggle=False)
        cdtt = prefs.camera_dof_target_type

        if not camera.dof.focus_object:
            layout.operator(PROPS_OT_toggle_camera.bl_idname,
                text=("Value", "Target")[cdtt],
                icon=('EMPTY_AXIS', 'OBJECT_DATA')[cdtt],
            )

        # row = layout.grid_flow(row_major=False, columns=0, even_columns=False, even_rows=False, align=True)
        row = layout.row(align=True)
        if cdtt or camera.dof.focus_object:
            row.prop(camera.dof, 'focus_object', icon='OBJECT_ORIGIN', **args)
        else:
            row.prop(camera, 'show_limits', icon='OBJECT_ORIGIN', **args)
            row.prop(camera.dof, 'focus_distance', icon='NONE', **args)

        layout.prop(camera.dof, 'aperture_fstop', icon='NONE', **args)

        row = layout.row(align=True)
        row.prop(camera, 'display_size', icon='NONE', **args)


class PROPS_OT_toggle_camera(bpy.types.Operator):
    bl_description = "Toggle Camera DoF Target type"
    bl_idname = 'zpy.toggle_camera_dof_target_type'
    bl_label = ""
    bl_options = {'INTERNAL'}

    def execute(self, context):
        prefs = utils.prefs(__package__)
        prefs.camera_dof_target_type = not prefs.camera_dof_target_type

        return {'INTERFACE'}
