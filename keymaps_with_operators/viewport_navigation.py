import bpy
from bpy.types import Operator
from zpy import register_keymaps, utils
km = register_keymaps()


class NAVIGATE_OT_rotate_view(Operator):
    bl_description = ""
    bl_idname = 'zpy.rotate_view'
    bl_label = ""

    def execute(self, context):
        prefs = utils.prefs().inputs

        old = prefs.use_mouse_depth_navigate
        prefs.use_mouse_depth_navigate = True

        bpy.ops.view3d.rotate('INVOKE_DEFAULT')
        prefs.use_mouse_depth_navigate = old

        return {'FINISHED'}


class NAVIGATE_OT_zoom_to_selection(Operator):
    bl_description = ""
    bl_idname = 'zpy.zoom_to_selection'
    bl_label = ""

    def execute(self, context):
        prefs = utils.prefs().inputs

        old = prefs.use_zoom_to_mouse
        prefs.use_zoom_to_mouse = True

        prefs2 = utils.prefs().inputs

        old2 = prefs2.use_mouse_depth_navigate
        prefs2.use_mouse_depth_navigate = True

        bpy.ops.view3d.dolly('INVOKE_DEFAULT')
        prefs.use_zoom_to_mouse = old
        prefs2.use_mouse_depth_navigate = old2

        return {'FINISHED'}


class SNAP_OT_view_focus(Operator):
    bl_description = ""
    bl_idname = 'zpy.focus_to_mouse'
    bl_label = "View Center Pick"

    @classmethod
    def description(cls, context, properties):
        return cls.bl_rna.description

    @classmethod
    def poll(cls, context):
        if context.mode not in ('PAINT_GPENCIL', 'SCULPT'):
            return bpy.ops.view3d.view_center_pick.poll(context.copy())

    def invoke(self, context, event):
        return bpy.ops.view3d.view_center_pick('INVOKE_DEFAULT')

    def execute(self, context):
        return bpy.ops.view3d.view_center_pick()


def register():
    args = dict(name='3D View', type='LEFTMOUSE', alt=True)
    km.add('view3d.move', **args, shift=True)
        # Shift View
    km.add(NAVIGATE_OT_rotate_view, **args)
        # Rotate
    km.add('view3d.zoom', **args, shift=True, ctrl=True)
        # Zoom to Selection  (does not work with saved depth preference)
    km.add(NAVIGATE_OT_zoom_to_selection, **args, ctrl=True)
        # Zoom in Direction

    # 2D Editors
    args = dict(name='SequencerPreview', type='LEFTMOUSE', alt=True)
    km.add('view2d.pan', **args, shift=True)
    km.add('view2d.zoom', **args, ctrl=True)

    # From without operators

    args = dict(name='3D View', type='WHEELUPMOUSE')
    km.add('view3d.view_pan', **args, shift=True).type = 'PANUP'
    km.add('view3d.view_pan', **args, ctrl=True).type = 'PANRIGHT'
    km.add('view3d.view_roll', **args, shift=True, ctrl=True).type = 'RIGHT'
    km.add('view3d.view_orbit', **args, ctrl=True, alt=True).type = 'ORBITRIGHT'
    km.add('view3d.view_orbit', **args, shift=True, alt=True).type = 'ORBITUP'

    args = dict(name='3D View', type='WHEELDOWNMOUSE')
    km.add('view3d.view_pan', **args, shift=True).type = 'PANDOWN'
    km.add('view3d.view_pan', **args, ctrl=True).type = 'PANLEFT'
    km.add('view3d.view_roll', **args, shift=True, ctrl=True).type = 'LEFT'
    km.add('view3d.view_orbit', **args, ctrl=True, alt=True).type = 'ORBITLEFT'
    km.add('view3d.view_orbit', **args, shift=True, alt=True).type = 'ORBITDOWN'

    # Snap View to Cursor/Selected
    km.add(SNAP_OT_view_focus, name='3D View', type='LEFTMOUSE', any=True, value='DOUBLE_CLICK')
        # Use custom op to disable in Grease Pencil Draw mode
    # km.add('view3d.view_center_pick', name='3D View', type='LEFTMOUSE', any=True, value='DOUBLE_CLICK')
        # km.add('view3d.view_center_cursor', name='3D View', type='C', value='PRESS')
        # km.add('view3d.select_circle', name='3D View', type='C', value='DOUBLE_CLICK')

    km.add('view3d.view_selected', name='3D View', type='C', shift=True)
    # km.add('view3d.view_all', value='DOUBLE_CLICK', center=False)


def unregister():
    km.remove()
