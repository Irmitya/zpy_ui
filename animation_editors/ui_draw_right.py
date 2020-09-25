import bpy


def draw(self, context, layout=None):
    if layout is None:
        layout = self.layout

    row = layout.row(align=True)

    st = context.space_data
    row.operator('zpy.toggle_anim_snap', text="",
        icon=('SNAP_ON', 'SNAP_OFF')[st.auto_snap == 'NONE'],
        depress=(st.auto_snap == 'FRAME')
    )

    edit = context.preferences.edit

    # but = row.row(align=True)
    # but.enabled = (edit.keyframe_new_interpolation_type == 'BEZIER')
    row.prop(edit, 'keyframe_new_handle_type', icon_only=True)
    # row.prop(edit, 'keyframe_new_interpolation_type', icon_only=True)
    kt = edit.keyframe_new_interpolation_type

    but = row.box()
    # but.emboss = 'NONE'  # enum in ['NORMAL', 'NONE', 'PULLDOWN_MENU', 'RADIAL_MENU']
    but.menu('GLOBAL_MT_set_interpolation', text="  ", icon='IPO_' + kt)

    # for kt in ('CONSTANT', 'LINEAR', 'BEZIER'):
        # but = row.row(align=True)
        # # but.active = (kt == edit.keyframe_new_interpolation_type)
        # if (kt == edit.keyframe_new_interpolation_type):
        #     but.prop(edit, 'keyframe_new_interpolation_type', icon_only=True)
        # else:
        #     but.active = False
        #     but.operator('zpy.set_anim_interpolations',
        #         text="", icon='IPO_' + kt).type = kt

    if hasattr(context.scene, 'wait'):
        row.operator('zpy.wait_for_input', text="", icon='FRAME_NEXT')
        wait = context.scene.wait

        loop = row.row()
        loop.emboss = 'PULLDOWN_MENU'
        loop.active = wait.stop_loop

        # icon = ('FILE_REFRESH', 'FRAME_NEXT')[loop.active]
        icon = ('FILE_REFRESH', 'PAUSE')[loop.active]
        loop.prop(wait, 'stop_loop', text="", icon=icon)


# for space in ('GRAPH_EDITOR', 'DOPESHEET_EDITOR', 'NLA_EDITOR'):
    # exec(f'''class {space}_HT_draw_right(bpy.types.Header):
        # bl_space_type = '{space}'

        # draw = draw
    # ''')



# editors = (
    # 'DOPESHEET_HT_editor_buttons',
    # 'TIME_HT_editor_buttons',
    # 'GRAPH_HT_header',
    # 'NLA_HT_header',
# )


# def register():
    # for menu in editors:
        # eval('bpy.types.' + menu).append(draw)


# def unregister():
    # for menu in editors:
        # eval('bpy.types.' + menu).remove(draw)
