import bpy
from zpy import Is, Get, is27, is28


class PRESET_PT_lights(bpy.types.Panel):
    """Properties for active Light object"""
    bl_label = "Toggle Light props"
    bl_options = {'DEFAULT_CLOSED', 'HIDE_HEADER'}
    bl_region_type = 'TOOLS'
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(self, context):
        return Is.light(context.object)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout.column(align=True)

        light = context.object.data
        eve = context.scene.eevee

        # if eve.shadow_method == 'ESM':
        #     preset = all((
        #         round(light.shadow_buffer_clip_start, 2) == 0.01,
        #         # round(light.shadow_buffer_exp, 2) == 7.5,
        #         round(light.shadow_buffer_bleed_bias, 2) == 0.95,
        #         light.use_contact_shadow,
        #     ))
        # elif eve.shadow_method == 'VSM':
        #     preset = all((
        #         round(light.shadow_buffer_clip_start, 2) == 0.01,
        #         # round(light.shadow_buffer_exp, 2) == 7.5,
        #         round(light.shadow_buffer_bleed_bias, 2) == 0.95,
        #         light.use_contact_shadow,
        #     ))
        # else:
        #     assert None, ("New/Unknown shadow method", eve.shadow_method)

        light_icon = ('LIGHT', 'LAMP')[is27]
        light_icon += '_' + light.type
        # if preset:
        #     light_icon += '_' + light.type
        #     preset = True
        # else:
        #     preset = False

        args = dict(icon=light_icon, depress=True)
        # args = dict(icon=light_icon, depress=preset)
        if is27: args.pop('depress')

        # # layout.emboss = 'PULLDOWN_MENU'
        # row = layout.row()
        # row.scale_x = 2
        # row.scale_y = 2
        # row.operator(PRESET_OT_lights.bl_idname, text="", **args)
        # # prefs.operator(layout, 'Default Light Setup', text="",
        # #             icon='OUTLINER_OB_LIGHT')

        col = layout.box().column(align=True)
        col.prop(light, 'color', text="")
        col.prop(light, 'energy')  # , text="")
        col.prop(light, 'specular_factor')  # , text="")
        col.prop(light, 'shadow_soft_size')  # , text="")
        col.prop(light, 'shadow_buffer_bias')  # , text="")
        # col.prop(light, 'shadow_buffer_exp')  # , text="")
        # # layout.prop(light, 'use_contact_shadow', toggle=True)  # , text="")
        # if eve.shadow_method == 'ESM':
        #     layout.prop_enum(eve, 'shadow_method', 'VSM')


class PRESET_OT_lights(bpy.types.Operator):
    bl_description = "Set default values for a good lamp, with one click"
    bl_idname = 'zpy.preset_lights'
    bl_label = "Default Light Setup"
    bl_options = {'REGISTER', 'UNDO_GROUPED'}

    @classmethod
    def poll(self, context):
        return Is.light(context.object)

    def execute(self, context):
        eve = context.scene.eevee
        light = context.object.data

        def default():
            light.shadow_buffer_clip_start = 0.05
            light.shadow_buffer_soft = 3.0

            light.shadow_buffer_bias = 1.0
            light.shadow_buffer_exp = 2.5
            light.shadow_buffer_bleed_bias = 0.0

            light.use_contact_shadow = False
            light.contact_shadow_distance = 0.2
            light.contact_shadow_soft_size = 0.2
            light.contact_shadow_bias = 0.03
            light.contact_shadow_thickness = 0.2

        def esm():
            light.shadow_buffer_clip_start = 0.01
            # light.shadow_buffer_soft = 3.0

            # light.shadow_buffer_bias = 1.0
            light.shadow_buffer_exp = 7.5
                # Sometimes looks unnecessary
                # What it does is under certain lighting conditions
                # It will do an additional shadow clipping, like bias
            # light.shadow_buffer_bleed_bias = 0.0

            light.use_contact_shadow = True
            light.contact_shadow_distance = 0.02
            # light.contact_shadow_soft_size = 0.2
            light.shadow_buffer_bleed_bias = 0.95
            # light.contact_shadow_thickness = 0.2

        def vsm():
            light.shadow_buffer_clip_start = 0.01
            # light.shadow_buffer_soft = 3.0

            light.shadow_buffer_bias = 0.01
            # light.shadow_buffer_exp = 2.5
            light.shadow_buffer_bleed_bias = 0.5

            light.use_contact_shadow = True
            # light.contact_shadow_distance = 0.02
            # light.contact_shadow_soft_size = 0.2
            # light.contact_shadow_bias = 0.03
            # light.contact_shadow_thickness = 0.2

        default()

        if eve.shadow_method == 'ESM':
            esm()
        elif eve.shadow_method == 'VSM':
            vsm()
        else:
            assert None, ("New/Unknown shadow method", eve.shadow_method)

        return {'FINISHED'}
