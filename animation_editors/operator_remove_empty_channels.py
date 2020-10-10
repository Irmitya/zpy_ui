import bpy


class ANIM_OT_remove_empty(bpy.types.Operator):
    bl_description = "Clean F-Curve Channels, without also cleaning the keyframes"
    bl_idname = 'graph.cull_channels'
    bl_label = "Remove Unused F-Curves"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def description(cls, context, properties):
        return cls.bl_description

    @classmethod
    def poll(cls, context):
        return context.selected_editable_fcurves

    def execute(self, context):
        count = 0

        for fc in context.selected_editable_fcurves:
            remove = True
            for kp in fc.keyframe_points:
                if fc.data_path.endswith('rotation_quaternion') and fc.array_index == 0:
                    cull = 1
                elif fc.data_path.endswith('scale'):
                    cull = 1
                else:
                    cull = 0
                if round(kp.co[1], self.cull) != cull:
                    remove = False
                    break
            if remove:
                fc.id_data.fcurves.remove(fc)
                count += 1

        self.report({'INFO'}, f"Removed {count} fcurves")

        return {'FINISHED'}

    cull: bpy.props.IntProperty(
        name="Cull Ratio",
        description="Amount of decimal points to consider before rounding value",
        default=6,
    )
