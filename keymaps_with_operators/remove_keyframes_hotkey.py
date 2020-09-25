import bpy
from zpy import register_keymaps
km = register_keymaps()


class ANIM_OT_keyframe_delete_v3d_keyingset(bpy.types.Operator):
    """
    Was originally for preventing False error when removing keyframes from
    one bone while multiple rigs were in pose mode. The warning would tell you
    that it couldn't remove keyframes from the  other objects, despite
    successfully remooving from the active (and intended) object.
    """
    # bl_description = "Keyframe Remove Menu with confirmation"\
    # " (or Remove Keyframe from Keyingset if Autokeyingset is Enabled)"
    bl_description = "Delete keyframes on current frame, based on keyingset"
    # bl_description = "Remove keyframes on current frame for selected "\
        # "objects and bones"
        # ".\n(without calling an error for having multiple objects)"
    bl_idname = 'zpy.keyframe_delete_v3d_keyingset'
    bl_label = "Delete Keyframe"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return (context.scene.tool_settings.use_keyframe_insert_keyingset and
                context.scene.keying_sets_all.active)
        # return bpy.ops.anim.keyframe_delete_v3d.poll(context.copy())

    def invoke(self, context, event):
        # if context.scene.tool_settings.use_keyframe_insert_keyingset and \
        #         context.scene.keying_sets_all.active:
        #     op = bpy.ops.anim.keyframe_delete
        #     # try:
        #         # bpy.ops.anim.keyframe_delete('INVOKE_DEFAULT')
        #         # return {'FINISHED'}
        #     # except:
        #         # pass
        # else:
        #     op = bpy.ops.anim.keyframe_delete_v3d

        try:
            # return op('INVOKE_DEFAULT')
            return bpy.ops.anim.keyframe_delete('INVOKE_DEFAULT')
        except Exception as er:
            self.report({'WARNING'}, repr(er))
            return {'CANCELLED'}


def register():
    args = dict(idname=ANIM_OT_keyframe_delete_v3d_keyingset,
        type='I', value='PRESS', alt=True,
    )
    km.add(**args, name='Object Mode')
    km.add(**args, name='Pose')


def unregister():
    km.remove()
