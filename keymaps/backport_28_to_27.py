# from zpy import register_keymaps
# km = register_keymaps.register()


# # 2.8 hotkeys to 2.7
# def register():
    # # Show toolbox menu (Dynamic Spacebar addon)
    # km.add('wm.call_menu', name='Window', type='SPACE', shift=True, value='PRESS', properties={'name': 'VIEW3D_MT_Space_Dynamic_Menu'})

    # # Search Menu
    # km.add('wm.search_menu', name='Window', type='F3', value='PRESS')

    # # Fullscreen
    # km.add('screen.screen_full_area', name='Screen', type='SPACE', ctrl=True, value='PRESS')
    # km.add('screen.screen_full_area', name='Screen', type='SPACE', ctrl=True, alt=True, value='PRESS', properties={'use_hide_panels': True})
    # km.add('screen.screen_full_area', name='3D View', type='SPACE', ctrl=True, alt=True, value='PRESS', properties={'use_hide_panels': True})
    # km.toggle('wm.context_toggle', name='3D View', type='SPACE', ctrl=True, value='PRESS')

    # # Select
    # km.add('view3d.cursor3d', name='3D View', type='LEFTMOUSE', value='CLICK')
    # km.add('view3d.select_border', name='3D View', type='EVT_TWEAK_L', shift=True, value='ANY', properties={'deselect': False, 'extend': True})
    # km.add('view3d.select_border', name='3D View', type='EVT_TWEAK_L', value='ANY', properties={'extend': False})
    # # km.add(idname='view3d.manipulator', name='3D View', type='LEFTMOUSE', value='RELEASE',
    # #        properties={'release_confirm': True, 'use_accurate': False, 'use_planar_constraint': False})
    # # km.add('view3d.cursor3d', name='3D View', type='LEFTMOUSE', any=True, value='CLICK')
    # km.add('view3d.select_border', name='3D View', type='B', value='PRESS', properties={'extend': True})
    # km.toggle('view3d.select_border', name='3D View', type='B', value='PRESS')  # By default, extend isn't declared
    # km.toggle('view3d.manipulator', name='3D View', type='LEFTMOUSE', value='PRESS', shift=True)
    # km.toggle('view3d.manipulator', name='3D View', type='LEFTMOUSE', value='PRESS', any=True)
    # # km.toggle('view3d.cursor3d_enhanced', name='3D View', type='ACTIONMOUSE', value='PRESS', shift=True, addon=False)

    # km.toggle('view3d.cursor3d', name='3D View', type='ACTIONMOUSE', value='PRESS')
    # # When this is toggled, manipulators don't work with mouse click
    # # km.toggle('view3d.manipulator', name='3D View', type='LEFTMOUSE', any=True, value='PRESS')

    # # Center View
    # km.add('view3d.view_center_pick', name='3D View', type='MIDDLEMOUSE', alt=True, value='PRESS')

    # deselect = [
    #     ('gpencil.select_all', 'Grease Pencil Stroke Edit Mode'),
    #     ('paint.face_select_all', 'Face Mask'),
    #     ('paint.vert_select_all', 'Weight Paint Vertex Selection'),
    #     ('pose.select_all', 'Pose'),
    #     ('object.select_all', 'Object Mode'),
    #     ('curve.select_all', 'Curve'),
    #     ('mesh.select_all', 'Mesh'),
    #     ('armature.select_all', 'Armature'),
    #     ('mball.select_all', 'Metaball'),
    #     ('lattice.select_all', 'Lattice'),
    #     ('particle.select_all', 'Particle'),
    #     ('marker.select_all', 'Markers'),
    #     ('uv.select_all', 'UV Editor'),
    #     ('mask.select_all', 'Mask Editing'),
    #     ('node.select_all', 'Node Editor'),
    #     ('sequencer.select_all', 'Sequencer'),
    #     ('clip.select_all', 'Clip Editor'),
    #     ('clip.graph_select_all_markers', 'Clip Graph Editor'),
    #     ]
    # for id, name in deselect:
    #     km.add(id, name=name, type='A', alt=True, value='PRESS', properties={'action': 'DESELECT'})


# def unregister():
    # km.remove()
