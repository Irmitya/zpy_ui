import bpy
from zpy import utils


rna_enum_beztriple_keyframe_type_items = [
    ("KEYFRAME", "Keyframe", "Normal keyframe - e.g. for key poses", 'KEYTYPE_KEYFRAME_VEC', 0),
    ("BREAKDOWN", "Breakdown", "A breakdown pose - e.g. for transitions between key poses", 'KEYTYPE_BREAKDOWN_VEC', 1),
    ("MOVING_HOLD", "Moving Hold", "A keyframe that is part of a moving hold", 'KEYTYPE_MOVING_HOLD_VEC', 2),
    ("EXTREME", "Extreme", "An 'extreme' pose, or some other purpose as needed", 'KEYTYPE_EXTREME_VEC', 3),
    ("JITTER", "Jitter", "A filler or baked keyframe for keying on ones, or some other purpose as needed", 'KEYTYPE_JITTER_VEC', 4),
]


class GRAPH_OT_keyframe_type(bpy.types.Operator):
    bl_description = "Set type of keyframe for the selected keyframes"
    bl_idname = 'graph.keyframe_type'
    bl_label = "Set Keyframe Type"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def description(cls, context, properties):
        return cls.bl_rna.description

    @classmethod
    def poll(cls, context):
        # return ed_spacetype_test(C, SPACE_ACTION);
        # return context.space_data.type == 'GRAPH_EDITOR'
        return context.editable_fcurves

    def invoke(self, context, event):
        # ot->invoke = WM_menu_invoke;
        return self.execute(context)

    def execute(self, context):
        utils.update_keyframe_points(context)

        for fc in context.editable_fcurves:
            for key in fc.keyframe_points:
                if key.select_control_point:
                    key.type = self.type

        return {'FINISHED'}

    type: bpy.props.EnumProperty(
        items=rna_enum_beztriple_keyframe_type_items,
        name="Type",
        description="",
        # options={'SKIP_SAVE'},
    )
