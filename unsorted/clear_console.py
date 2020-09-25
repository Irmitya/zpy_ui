import bpy
import os


class UI_OT_console_clear(bpy.types.Operator):
    bl_description = "Clear System Console"
    bl_idname = 'zpy.clear_console'
    bl_label = "Clear System Console"

    def execute(self, context):
        os.system("cls")
        return {'FINISHED'}
