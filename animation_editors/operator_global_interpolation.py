import bpy
from bpy.types import Operator, Menu
from zpy import utils


interpolation_mode_items = [
    # interpolation
    ('', "Interpolation", "Standard transitions between keyframes"),
    ('CONSTANT', "Constant", "No interpolation, value of A gets held until B is encountered", 'IPO_CONSTANT', 1),
    ('LINEAR', "Linear", "Straight-line interpolation between A and B (i.e. no ease in/out)", 'IPO_LINEAR', 2),
    ('BEZIER', "Bezier", "Smooth interpolation between A and B, with some control over curve shape", 'IPO_BEZIER', 3),

    # easing
    ('', "Easing (by strength)", "Predefined inertial transitions, useful for motion graphics (from least to most " "''dramatic'')"),
    ('SINE', "Sinusoidal", "Sinusoidal easing (weakest, almost linear but with a slight curvature)", 'IPO_SINE', 5),
    ('QUAD', "Quadratic", "Quadratic easing", 'IPO_QUAD', 6),
    ('CUBIC', "Cubic", "Cubic easing", 'IPO_CUBIC', 7),
    ('QUART', "Quartic", "Quartic easing", 'IPO_QUART', 8),
    ('QUINT', "Quintic", "Quintic easing", 'IPO_QUINT', 9),
    ('EXPO', "Exponential", "Exponential easing (dramatic)", 'IPO_EXPO', 10),
    ('CIRC', "Circular", "Circular easing (strongest and most dynamic)", 'IPO_CIRC', 11),

    ('', "Dynamic Effects", "Simple physics-inspired easing effects"),
    ('BACK', "Back", "Cubic easing with overshoot and settle", 'IPO_BACK', 13),
    ('BOUNCE', "Bounce", "Exponentially decaying parabolic bounce, like when objects collide", 'IPO_BOUNCE', 14),
    ('ELASTIC', "Elastic", "Exponentially decaying sine wave, like an elastic band", 'IPO_ELASTIC', 15),
]


class GLOBAL_MT_set_interpolation(Menu):
    bl_description = "Interpolation mode used for first keyframe on newly added F-Curves " \
                     "(subsequent keyframes take interpolation from preceding keyframe)"
    bl_label = "New Interpolation Type"

    def draw(self, context):
        layout = self.layout
        layout.label(text="New Interpolation Type")

        row = layout.row()
        for item in interpolation_mode_items:
            (id, label, *desc) = item
            if not id:
                col = row.column()
                col.label(text=label)
            else:
                col.operator('zpy.set_anim_interpolations', text=label, icon=desc[1]).type = id


class GLOBAL_OT_set_interpolation(Operator):
    bl_description = "Set interpolation of all fcurves in all actions" \
        ".\nFor viewing the animation in a specific mode (for example blockout)"\
        ".\nAlt Click to apply interpolation to all existing actions"
    bl_idname = 'zpy.set_anim_interpolations'
    bl_label = "Set Global Interpolation"
    bl_options = {'REGISTER', 'UNDO'}

    # @classmethod
    # def poll(self, context):
        # return bpy.data.actions

    def invoke(self, context, event):
        if event.alt:
            for action in bpy.data.actions:
                # bases = a.base_interpolations.
                for fc in action.fcurves:
                    for key in fc.keyframe_points:
                        key.interpolation = self.type
        utils.prefs().edit.keyframe_new_interpolation_type = self.type

        return {'FINISHED'}

    type: bpy.props.EnumProperty(
        items=interpolation_mode_items,
        name="New Interpolation Type",
        description="Interpolation mode used for first keyframe on newly added F-Curves "
                    "(subsequent keyframes take interpolation from preceding keyframe)",
        default='BEZIER'
    )
