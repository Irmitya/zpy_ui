import bpy
from zpy import Get


def basic_pre(self, context):
    layout = self.layout
    layout.operator('anim.start_frame_set')
    layout.operator('anim.end_frame_set')


def basic_post(self, context):
    layout = self.layout
    scn = context.scene
    layout.prop(scn.tool_settings, 'use_record_with_nla', text="Layered Recording")
    layout.prop(scn, 'lock_frame_selection_to_range', text="Limit Playhead to Frame Range")


def dope_w_pre(self, context):
    layout = self.layout
    basic_pre(self, context)
    layout.separator()

    layout.operator('action.sample_jitter')
    layout.separator()


def dope_w_post(self, context):
    layout = self.layout
    basic_post(self, context)


def dope_x(self, context):
    layout = self.layout.column(align=True)
    layout.operator('graph.cull_channels', text="Cull Channels")


def graph_w_pre(self, context):
    layout = self.layout
    basic_pre(self, context)
    layout.separator()

    layout.operator('graph.smooth')
    layout.operator_context = 'INVOKE_DEFAULT'
    layout.operator('graph.smooth_blend')
    layout.operator('graph.sample_jitter')
    layout.separator()

    row = layout.row()
    row.active = bpy.ops.graph.keyframe_type.poll()
    row.operator_menu_enum('graph.keyframe_type', 'type', text="Keyframe Type")
    layout.separator()


def graph_w_post(self, context):
    layout = self.layout
    basic_post(self, context)
    layout.separator()

    sp = context.space_data
    layout.prop(sp, 'use_only_selected_keyframe_handles')
    layout.prop(sp, 'use_only_selected_curves_handles')
    layout.prop(sp, 'show_handles')


def graph_x(self, context):
    layout = self.layout
    layout.operator("graph.delete")

    layout.separator()

    layout.operator('graph.clean_tweak').channels = False
    layout.operator('graph.clean_tweak', text="Clean Channels").channels = True
    layout.operator('graph.remove_unused_bones', text="Clean Channels (Bones)")

    # layout = self.layout.column(align=True)
    layout.operator_context = 'INVOKE_DEFAULT'
    layout.operator('graph.cull_channels', text="Cull Channels")
    layout.operator('graph.decimate', text="Decimate (Error)").mode = 'ERROR'
    layout.operator('graph.decimate', text="Decimate (Ratio)").mode = 'RATIO'


class GRAPH_OT_clean_tweak(bpy.types.Operator):
    bl_description = "Simplify F-Curves by removing closely spaced keyframes (lower threshold)"
    bl_idname = 'graph.clean_tweak'
    bl_label = "Clean Keyframes"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def description(cls, context, properties):
        return cls.bl_description

    @classmethod
    def poll(cls, context):
        return bpy.ops.graph.clean.poll(context.copy())

    def execute(self, context):
        return bpy.ops.graph.clean(threshold=0.0001 * self.threshold, channels=self.channels)
        # return {'FINISHED'}

    threshold: bpy.props.FloatProperty(
        name="Threshold",
        default=10.0,
        min=0.0,
        soft_min=0.0,
        soft_max=10000000.0,
    )
    channels: bpy.props.BoolProperty(
        name="Channels",
        description="",
        default=False,
    )


def nla_w_pre(self, context):
    layout = self.layout
    basic_pre(self, context)
    layout.separator()

    layout.operator('zpy.select_from_strips')
    layout.separator()

    layout.operator('anim.channels_clean_empty')
    layout.operator('nla.action_sync_length', text='Sync Action length Now', icon='FILE_REFRESH').active = False

    for (ob, strips) in Get.strips_nla(context):
        for item in strips:
            icon = ['CHECKBOX_DEHLT', 'CHECKBOX_HLT'][item.strip.use_sync_length]
            break
        else:
            continue
        break
    else:
        icon = 'NONE'
    layout.operator('nla.toggle_action_sync', icon=icon)

    layout.separator()


class NLA_OT_toggle_sync(bpy.types.Operator):
    bl_description = "Toggle auto syncing on selected strips"
    bl_idname = 'nla.toggle_action_sync'
    bl_label = "Sync Action Length"
    bl_options = {'UNDO'}

    @classmethod
    def description(cls, context, properties):
        return cls.bl_description

    @classmethod
    def poll(cls, context):
        return Get.strips_nla(context)

    def execute(self, context):
        value = None

        for (ob, strips) in Get.strips_nla(context):
            for item in strips:
                if value is None:
                    value = not item.strip.use_sync_length
                item.strip.use_sync_length = value

        return {'FINISHED'}


def nla_w_post(self, context):
    layout = self.layout
    basic_post(self, context)


def register():
    bpy.types.DOPESHEET_MT_context_menu.prepend(dope_w_pre)
    bpy.types.DOPESHEET_MT_context_menu.append(dope_w_post)
    bpy.types.DOPESHEET_MT_delete.append(dope_x)

    bpy.types.GRAPH_MT_context_menu.prepend(graph_w_pre)
    bpy.types.GRAPH_MT_context_menu.append(graph_w_post)
    # bpy.types.GRAPH_MT_delete.append(graph_x)
    bpy.types.GRAPH_MT_delete.draw_backup = bpy.types.GRAPH_MT_delete.draw
    bpy.types.GRAPH_MT_delete.draw = graph_x

    bpy.types.NLA_MT_context_menu.prepend(nla_w_pre)
    bpy.types.NLA_MT_context_menu.append(nla_w_post)


def unregister():
    bpy.types.DOPESHEET_MT_context_menu.remove(dope_w_pre)
    bpy.types.DOPESHEET_MT_context_menu.remove(dope_w_post)
    bpy.types.DOPESHEET_MT_delete.remove(dope_x)

    bpy.types.GRAPH_MT_context_menu.remove(graph_w_pre)
    bpy.types.GRAPH_MT_context_menu.remove(graph_w_post)
    # bpy.types.GRAPH_MT_delete.remove(graph_x)
    bpy.types.GRAPH_MT_delete.draw = bpy.types.GRAPH_MT_delete.draw_backup
    del bpy.types.GRAPH_MT_delete.draw_backup

    bpy.types.NLA_MT_context_menu.remove(nla_w_pre)
    bpy.types.NLA_MT_context_menu.remove(nla_w_post)
