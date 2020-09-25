import bpy
from bpy.props import StringProperty
from zpy import register_keymaps
km = register_keymaps()


class WINDOW_OT_toggle_area(bpy.types.Operator):
    bl_description = "Toggle active area type"
    bl_idname = 'zpy.toggle_area'
    bl_label = "Toggle Area"

    def execute(self, context):
        area = context.area
        space = self.space_type

        if space in self.enum_ui_type:
            if area.ui_type != space:
                area.ui_type = space
            else:
                return {'PASS_THROUGH'}
        elif space in self.enum_type:
            if area.type != space:
                area.type = space
            else:
                return {'PASS_THROUGH'}
        else:
            self.report({'INFO'}, f"[{area!r}] Invalid area type")

        return {'FINISHED'}

    space_type: StringProperty()

    base = bpy.types.Area.bl_rna.properties['type']
    enum = base.enum_items
    # space_type = EnumProperty(
        # items=[
            # ('EMPTY', 'Empty', '', 'NONE', 0),
            # ('VIEW_3D', '3D Viewport', 'Manipulate objects in a 3D environment', 'VIEW3D', 1),
            # ('IMAGE_EDITOR', 'UV/Image Editor', 'View and edit images and UV Maps', 'IMAGE', 6),
            # ('NODE_EDITOR', 'Node Editor', 'Editor for node-based shading and compositing tools', 'NODETREE', 16),
            # ('SEQUENCE_EDITOR', 'Video Sequencer', 'Video editing tools', 'SEQUENCE', 8),
            # ('CLIP_EDITOR', 'Movie Clip Editor', 'Motion tracking tools', 'TRACKER', 20),
            # ('DOPESHEET_EDITOR', 'Dope Sheet', 'Adjust timing of keyframes', 'ACTION', 12),
            # ('TIMELINE', 'Timeline', 'Adjust timing of keyframes', 'TIME', 120),
            # ('GRAPH_EDITOR', 'Graph Editor', 'Edit drivers and keyframe interpolation', 'GRAPH', 2),
            # ('NLA_EDITOR', 'Nonlinear Animation', 'Combine and layer Actions', 'NLA', 13),
            # ('TEXT_EDITOR', 'Text Editor', 'Edit scripts and in-file documentation', 'TEXT', 9),
            # ('CONSOLE', 'Python Console', 'Interactive programmatic console for advanced editing and script development', 'CONSOLE', 18),
            # ('INFO', 'Info', 'Main menu bar and list of error messages (drag down to expand and display)', 'INFO', 7),
            # ('OUTLINER', 'Outliner', 'Overview of scene graph and all available data-blocks', 'OUTLINER', 3),
            # ('PROPERTIES', 'Properties', 'Edit properties of active object and related data-blocks', 'PROPERTIES', 4),
            # ('FILE_BROWSER', 'File Browser', 'Browse for files and assets', 'FILEBROWSER', 5),
            # ('PREFERENCES', 'Preferences', 'Edit persistent configuration settings', 'PREFERENCES', 19)
            # ],
        # name='Editor Type',
        # description='Current editor type for this area',
        # default=None,  # ('string' or {'set'})  from items
        # options={'SKIP_SAVE'},
        # )
    enum_type = (
        'VIEW_3D',
        'IMAGE_EDITOR',
        'NODE_EDITOR',
        'SEQUENCE_EDITOR',
        'CLIP_EDITOR',
        'DOPESHEET_EDITOR',
        'GRAPH_EDITOR',
        'NLA_EDITOR',
        'TEXT_EDITOR',
        'CONSOLE',
        'INFO',
        'OUTLINER',
        'PROPERTIES',
        'FILE_BROWSER',
        'PREFERENCES',
    )
    enum_ui_type = (
        'VIEW_3D',
        'VIEW',
        'UV',
        'ShaderNodeTree',
        'CompositorNodeTree',
        'TextureNodeTree',
        'SEQUENCE_EDITOR',
        'CLIP_EDITOR',
        'DOPESHEET',
        'TIMELINE',
        'FCURVES',
        'DRIVERS',
        'NLA_EDITOR',
        'TEXT_EDITOR',
        'CONSOLE',
        'INFO',
        'OUTLINER',
        'PROPERTIES',
        'FILE_BROWSER',
        'PREFERENCES',
    )


def register():
    args = dict(idname=WINDOW_OT_toggle_area, value='PRESS')

    args['type'] = 'F13'
    # Outliner
    km.add(**args, name='Property Editor', space_type='OUTLINER')
    km.add(**args, name='Outliner', space_type='PROPERTIES')
    # Console
    km.add(**args, name='Text', space_type='CONSOLE')
    km.add(**args, name='Console', space_type='TEXT_EDITOR')
    # Animation
    km.add(**args, name='Dopesheet', space_type='DOPESHEET')
    km.add(**args, name='Dopesheet', space_type='FCURVES')
    km.add(**args, name='Graph Editor', space_type='NLA_EDITOR')
    km.add(**args, name='NLA Editor', space_type='TIMELINE')

    args['type'] = 'F14'
    # Outliner
    km.add(**args, name='Property Editor', space_type='OUTLINER')
    km.add(**args, name='Outliner', space_type='PROPERTIES')
    # Console
    km.add(**args, name='Text', space_type='CONSOLE')
    km.add(**args, name='Console', space_type='TEXT_EDITOR')
    # Animation
    km.add(**args, name='Dopesheet', space_type='TIMELINE')
    km.add(**args, name='Graph Editor', space_type='DOPESHEET')
    km.add(**args, name='NLA Editor', space_type='FCURVES')
    km.add(**args, name='Dopesheet', space_type='NLA_EDITOR')


def unregister():
    km.remove()
