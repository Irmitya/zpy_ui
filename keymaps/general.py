from zpy import register_keymaps
km = register_keymaps()


def register():
    # Insert markers, like inserting keyframes
    km.add('marker.add', name='Markers', type='I', value='PRESS')

    # # Disable Render
    # # https://developer.blender.org/T60847
    # # Until this is fixed, avoid rendering with Eevee
    # km.toggle('render.render', name='Screen', type='F12', value='PRESS')
    # km.toggle('render.render', name='Screen', type='F12', value='PRESS', ctrl=True)

    # General Hotkeys

    # Show Undo/Redo Panel
    km.add('ed.undo_history', name='Window', type='Z', ctrl=True, alt=True, value='PRESS')
    km.add('screen.redo_last', name='Screen', type='SPACE', alt=True, value='PRESS')

    # Repeat Operator
    km.add('screen.repeat_history', name='Screen', type='R', shift=True, alt=True, value='PRESS')
    # km.add('screen.repeat_history', name='Screen', type='R', shift=True, value='CLICK_DRAG')
    # km.add('screen.repeat_last', name='Screen', type='R', shift=True, value='CLICK')
    # km.toggle('screen.repeat_last', name='Screen', type='R', shift=True, value='PRESS')

    # Disable Mode Toggle, Enable Snap Toggling (from 2.7)
    args = dict(type='TAB', ctrl=True)
    km.toggle('wm.context_toggle', name='3D View', type='TAB', shift=True)  # Disable shift+tab snap toggle
    km.add('wm.context_toggle', name='3D View', **args, data_path='tool_settings.use_snap')
    km.toggle('view3d.object_mode_pie_or_toggle', name='Object Non-modal', **args)

    # Pivot Menu
    args = dict(idname='wm.call_menu_pie', name='3D View', value='PRESS')
    km.add(**args, type='F13').name = 'VIEW3D_MT_pivot_pie'
    km.add(**args, type='F14').name = 'VIEW3D_MT_orientations_pie'

    # # Snap Menu (not pie)
    # km.add('wm.call_menu', name='3D View', type='S', value='PRESS', shift=True, properties={'name': 'VIEW3D_MT_snap'})

    # Fullscreen
    # km.add('screen.screen_full_area', name='Screen', type='SPACE', ctrl=True, value='CLICK')
    # km.add('screen.screen_full_area', name='Screen', type='SPACE', ctrl=True, value='DOUBLE_CLICK', properties={'use_hide_panels': True})
    # # km.add('screen.screen_full_area', name='3D View', type='SPACE', ctrl=True, value='PRESS', properties={'use_hide_panels': True})
    # km.toggle('screen.screen_full_area', name='Screen', type='SPACE', ctrl=True, value='PRESS')

    # Switch the controls for copying a data path
    args = dict(idname='ui.copy_data_path_button', name='User Interface',
        type='C', ctrl=True, shift=True)
    km.toggle(**args, alt=True)
    km.toggle(**args, alt=False)
    km.add(**args, alt=True, full_path=False)
    km.add(**args, alt=False, full_path=True)
    km.add('ui.copy_as_driver_button', type='GRLESS')
    km.add('anim.paste_driver_button', type='GRLESS')

    km.add('transform.transform', name='Pose', type='S', ctrl=True, alt=True).mode = 'BONE_SIZE'

    # Sequencer cut
    args = dict(idname='sequencer.split', name='Sequencer', type='V')
    km.add(**args).type = 'SOFT'
    km.add(**args, shift=True).type = 'HARD'

    # Keep operator search and the new menu search
    km.toggle('wm.search_menu', name='Window', type='F3', value='PRESS')
    km.add('wm.search_menu', name='Window', type='F3', value='CLICK_DRAG')
    km.add('wm.search_operator', name='Window', type='F3', value='CLICK')


def unregister():
    km.remove()
