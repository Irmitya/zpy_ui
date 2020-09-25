# from zpy import register_keymaps
# km = register_keymaps.register()

# new_key = 'W'
# # Switch Quick Favorites (Q) to (W-slide)


# class POSE_OT_wm_call(Operator):
    # bl_description = ""
    # bl_idname = myops + '.call_menu_pose'
    # bl_label = ""
    # bl_options = {'INTERNAL'}

    # @classmethod
    # def poll(self, context):
    #     return (context.mode == 'POSE')

    # def execute(self, context):
    #     bpy.ops.wm.call_menu('INVOKE_DEFAULT', name='VIEW3D_MT_pose_context_menu')
    #     return {'FINISHED'}


# class wm:
    # call_menu = [
    #     ('Dopesheet', 'DOPESHEET_MT_context_menu'),
    #     ('Grease Pencil Stroke Edit Mode', 'VIEW3D_MT_gpencil_edit_context_menu'),
    #     # ('Grease Pencil Stroke Sculpt Mode', 'VIEW3D_MT_gpencil_sculpt_context_menu'),
    #     # ('Pose', 'VIEW3D_MT_pose_context_menu'),
    #     ('Object Mode', 'VIEW3D_MT_object_context_menu'),
    #     ('Curve', 'VIEW3D_MT_edit_curve_context_menu'),
    #     ('Mesh', 'VIEW3D_MT_edit_mesh_context_menu'),
    #     ('Armature', 'VIEW3D_MT_armature_context_menu'),
    #     ('Particle', 'VIEW3D_MT_particle_context_menu'),
    #     ('Animation Channels', 'DOPESHEET_MT_channel_context_menu'),
    #     ('UV Editor', 'IMAGE_MT_uvs_context_menu'),
    #     ('Graph Editor', 'GRAPH_MT_context_menu'),
    #     ('Node Editor', 'NODE_MT_context_menu'),
    #     ('Clip Editor', 'CLIP_MT_tracking_context_menu'),
    #     ]
    # call_panel = [
    #     ('Image Paint', 'VIEW3D_PT_paint_texture_context_menu'),
    #     ('Vertex Paint', 'VIEW3D_PT_paint_vertex_context_menu'),
    #     ('Weight Paint', 'VIEW3D_PT_paint_weight_context_menu'),
    #     ('Sculpt', 'VIEW3D_PT_sculpt_context_menu'),
    #     ('Grease Pencil Stroke Sculpt Mode', 'VIEW3D_MT_gpencil_sculpt_context_menu'),
    #     ]


# def register():
    # km.toggle('wm.call_menu', name='Window', type='Q', value='PRESS')
    # km.add('wm.call_menu', name='Window', type=new_key, value='CLICK_DRAG',
    #        properties={'name': 'SCREEN_MT_user_menu'})

    # for call in ['wm.call_menu', 'wm.call_panel']:
    #     for (id, name) in eval(call):
    #         if id == 'Pose': continue
    #         args = dict(idname=call, name=id, type=new_key, value='RELEASE')
    #         km.add(**args, properties={'name': name})
    #         km.toggle(**args)

    # # Pose (Release) is overriding Weight Paint (Release)
    # km.toggle('wm.call_menu', name='Pose', type=new_key, value='PRESS')
    # km.add(POSE_OT_wm_call, name='Pose', type=new_key, value='RELEASE')


# def unregister():
    # km.remove()
