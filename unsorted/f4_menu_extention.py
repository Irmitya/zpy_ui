import bpy
from zpy import utils


def draw_menu(self, context):
    layout = self.layout

    layout.operator_context = 'INVOKE_DEFAULT'
    if utils.find_op('iv.icons_show'):
        layout.operator('iv.icons_show', icon='QUESTION')
    layout.separator()
    layout.operator_context = 'INVOKE_AREA'

    space = context.space_data
    if hasattr(space, 'show_region_header'):
        if hasattr(space, 'show_region_tool_header'):
            layout.context_pointer_set('space', space)

            icon = ('CHECKBOX_DEHLT', 'CHECKBOX_HLT')[space.show_region_header]
            layout.operator('zpy.region_header', text="Header", icon=icon)
            layout.prop(space, 'show_region_tool_header', text="Tool Settings")
        else:
            layout.prop(space, 'show_region_header')

    if hasattr(space, 'show_region_hud'):
        layout.prop(space, 'show_region_hud')

    layout.operator('wm.window_fullscreen_toggle', icon='FULLSCREEN_ENTER')

    # Draw_Console_Stuff
    layout.separator()
    layout.operator_context = 'INVOKE_DEFAULT'
    layout.operator('wm.console_toggle', icon='CONSOLE')
    layout.operator('zpy.clear_console', icon='CANCEL')


class OPERATOR_OT_name(bpy.types.Operator):
    bl_description = "Disable topbar header without disabling Tool Settings"
    bl_idname = 'zpy.region_header'
    bl_label = "Show Header"

    @classmethod
    def description(cls, context, properties):
        return cls.bl_rna.description

    @classmethod
    def poll(cls, context):
        return hasattr(context, 'space')

    def execute(self, context):
        space = context.space
        toolbar = space.show_region_tool_header

        space.show_region_header = not space.show_region_header
        space.show_region_tool_header = toolbar

        # prefs.remove(context.space_data, 'show_region_header')

        return {'FINISHED'}


def register():
    bpy.types.TOPBAR_MT_file_context_menu.append(draw_menu)


def unregister():
    bpy.types.TOPBAR_MT_file_context_menu.remove(draw_menu)
