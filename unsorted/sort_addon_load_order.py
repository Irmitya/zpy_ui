import bpy

class WORKSPACE_OT_sort_addons(bpy.types.Operator):
    bl_description = ""
    bl_idname = 'zpy.sort_addons'
    bl_label = ""
    # bl_options = {'REGISTER'}

    @classmethod
    def description(cls, context, properties):
        return cls.bl_description

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        from .. import __name__ as main

        workspace = context.workspace
        prefs = context.preferences

        import addon_utils
        addon_map = {mod.__name__: mod for mod in addon_utils.modules()}
        owner_ids = {owner_id.name for owner_id in workspace.owner_ids}

        addons = list()

        for addon in prefs.addons:
            module_name = addon.module
            module = addon_map.get(module_name)
            if module is None:
                continue
            info = addon_utils.module_bl_info(module)
            if not info["use_owner"]:
                continue
            is_enabled = module_name in owner_ids

            if module_name == main:
                continue
            elif is_enabled:
                if self.down:
                    addons.append(module_name)
            else:
                if not self.down:
                    addons.append(module_name)

        for add in addons[::-1]:
            bpy.ops.preferences.addon_disable('INVOKE_DEFAULT', module=add)
        for add in addons:
            bpy.ops.preferences.addon_enable('INVOKE_DEFAULT', module=add)

        workspace.owner_ids.clear()

        return {'FINISHED'}

    down: bpy.props.BoolProperty(default=True, options={'HIDDEN'})


def draw_down(self, context):
    row = self.layout.row(align=True)
    row.alignment = 'CENTER'
    row.operator('zpy.sort_addons', text="", icon='TRIA_UP').down = False
    row.operator('zpy.sort_addons', text="", icon='TRIA_DOWN').down = True


def register():
    bpy.types.WORKSPACE_PT_addons.append(draw_down)
    # bpy.types.WORKSPACE_PT_addons.prepend(draw_down)


def unregister():
    bpy.types.WORKSPACE_PT_addons.remove(draw_down)
