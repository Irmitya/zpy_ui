import bpy


class RENDER_OT_view_playback(bpy.types.Operator):
    bl_description = "Render the viewport for the animation range then start the player"
    bl_idname = 'render.opengl_playback'
    bl_label = "Viewport Render Animation + Playback"

    @classmethod
    def poll(cls, context):
        return bpy.ops.render.opengl.poll(context.copy())

    def invoke(self, context, event):
        bpy.ops.render.opengl('INVOKE_DEFAULT', animation=True)
        self.frame = context.scene.frame_current

        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type in {'ESC'}:
            return {'CANCELLED'}

        frame = context.scene.frame_current

        if frame < self.frame:
            # When frame reaches the end, it should jump back to the start
            self.play(context)
            return {'FINISHED'}
        else:
            # Keep updating frame
            self.frame = frame

        return {'PASS_THROUGH'}
        return {'RUNNING_MODAL'}

    def execute(self, context):
        bpy.ops.render.opengl(animation=True)
        self.play(context)
        return {'FINISHED'}

    def play(self, context):
        # scn = context.scene

        # scn.render.filepath
        # scn.render.image_settings.file_format
        bpy.ops.render.play_rendered_anim_fix()


def draw(self, context):
    layout = self.layout
    layout.operator("render.opengl_playback", text="Viewport Render Playback", icon='RENDER_ANIMATION')


def register():
    bpy.types.VIEW3D_MT_view.append(draw)


def unregister():
    bpy.types.VIEW3D_MT_view.remove(draw)
