import bpy
from zpy import register_keymaps, Get, Is, Set, popup
km = register_keymaps()


class VIEW3D_MT_object_mode_pie_armature_mesh(bpy.types.Menu):
    bl_label = "Mode"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator_enum("object.mode_set", "mode")

        def op(text, icon, mode):
            pie.operator('zpy.mode_set_armature_mesh', text=text, icon=icon).mode = mode

        pie.operator_context = 'EXEC_DEFAULT'

        if Is.mesh(context.object):
            op("Pose", 'POSE_HLT', 'POSE')
            op("Edit Armature", 'EDITMODE_HLT', 'EDIT_ARMATURE')
        elif Is.armature(context.object):
            pie.separator()
            op("Weight Paint", 'WPAINT_HLT', 'WEIGHT_PAINT')
            pie.separator()
            op("Sculpt", 'SCULPTMODE_HLT', 'SCULPT')
            op("Edit Mesh", 'EDITMODE_HLT', 'EDIT_MESH')


class OBJECT_OT_set_mode_armature_mesh(bpy.types.Operator):
    bl_description = "Sets the object interaction mode"
    bl_idname = 'zpy.mode_set_armature_mesh'
    bl_label = "Toggle Mode"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        (rig, mesh) = cls.get_rig_mesh(context)
        return (rig and mesh)

    def invoke(self, context, event):
        return bpy.ops.wm.call_menu_pie(name='VIEW3D_MT_object_mode_pie_armature_mesh')

    def execute(self, context):
        (rig, mesh) = self.get_rig_mesh(context)

        # Switch to object mode first, to prevent sending rig to empty mode
        # happens when switching from Armature Edit to Weight Paint (warning but no error)
        # from there, trying to change the armature mode gives error after fixing the mode
        bpy.ops.object.mode_set(mode='OBJECT')

        if self.mode == 'POSE':
            Set.active(context, rig)
            return bpy.ops.object.mode_set(mode='POSE')
        elif self.mode == 'EDIT_ARMATURE':
            Set.active(context, rig)
            return bpy.ops.object.mode_set(mode='EDIT')
        elif self.mode == 'WEIGHT_PAINT':
            Set.active(context, mesh)
            return bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
        elif self.mode == 'EDIT_MESH':
            Set.active(context, mesh)
            return bpy.ops.object.mode_set(mode='EDIT')
        elif self.mode == 'SCULPT':
            Set.active(context, mesh)
            return bpy.ops.object.mode_set(mode='SCULPT')

        return {'PASS_THROUGH'}

    @staticmethod
    def get_rig_mesh(context):
        ob = context.object

        if Is.armature(ob):
            for ob in context.selected_objects:
                if Is.mesh(ob):
                    for mod in ob.modifiers:
                        if (mod.type == 'ARMATURE') and (mod.object == context.object):
                            return (context.object, ob)
        elif Is.mesh(ob):
            for mod in ob.modifiers:
                if (mod.type == 'ARMATURE') and (mod.object in context.selected_objects):
                    return (mod.object, ob)

        return (None, None)

    mode: bpy.props.EnumProperty(
        items=[
            # ('identifier', "Name", "Description", 'NONE', 1),
            ('POSE', "Pose", ""),
            ('EDIT_ARMATURE', "Edit Armature", ""),
            ('WEIGHT_PAINT', "Weight Paint", ""),
            ('EDIT_MESH', "Edit Mesh", ""),
            ('SCULPT', "Sculpt", ""),
        ],
        name="",
        description="",
    )


def register():
    # km.add('wm.call_menu_pie', name='Object Non-modal', type='TAB', value='CLICK_DRAG').name = "VIEW3D_MT_object_mode_pie_armature_mesh"
    km.add(OBJECT_OT_set_mode_armature_mesh, name='Object Non-modal', type='TAB', value='CLICK_DRAG')


def unregister():
    km.remove()
