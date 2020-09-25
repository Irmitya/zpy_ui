import bpy
from zpy import register_keymaps, utils
km = register_keymaps()


class SCREEN_OT_merge_areas(bpy.types.Operator):
    bl_description = "Join selected areas into new window"
    bl_idname = 'zpy.area_join'
    bl_label = "Join Area"
    bl_options = {'BLOCKING', 'INTERNAL'}

    @classmethod
    def poll(self, context):
        return context.area and bpy.ops.screen.area_join.poll(context.copy())

    def invoke(self, context, event):
        area = context.area
        x = event.mouse_x
        y = event.mouse_y
        # try:

        # max_x = x - area.width / 3
        # max_y = y - area.height / 3
        # min_x = x + area.width / 3
        # min_y = y + area.height / 3

        mid_x = (area.width - area.x) / 2
        mid_y = (area.height - area.y) / 2

        if x < mid_x:
            border_x = (area.x)
        else:
            border_x = (area.x + area.width)
        if y < mid_y:
            border_y = (area.y)
        else:
            border_y = (area.y + area.height)

        ran_x = utils.scale_range(x, area.x, area.x + area.width, 0, 1)
        ran_y = utils.scale_range(y, area.y, area.y + area.height, 0, 1)

        if ran_x > ran_y:
            x = border_x
        else:
            y = border_y

        bpy.ops.screen.area_join('INVOKE_DEFAULT', cursor=(x, y))
        # bpy.ops.screen.area_join('INVOKE_DEFAULT', cursor=(x, border_y))
        # bpy.ops.screen.area_join('INVOKE_DEFAULT', cursor=(border_x, y))

        # bpy.ops.screen.area_join(
            # 'INVOKE_DEFAULT',
            # max_x=x - area.width / 3,
            # max_y=y - area.height / 3,
            # min_x=x + area.width / 3,
            # min_y=y + area.height / 3,
            # )

        return {'FINISHED'}


class SCREEN_OT_split_areas(bpy.types.Operator):
    bl_description = "Split selected area into new windows"
    bl_idname = 'zpy.area_split'
    bl_label = "Split Area"
    bl_options = {'BLOCKING', 'INTERNAL'}

    @classmethod
    def poll(self, context):
        return context.area and bpy.ops.screen.area_split.poll(context.copy())

    def invoke(self, context, event):
        area = context.area
        rel_x = event.mouse_x / (area.x + area.width)
        rel_y = event.mouse_y / (area.y + area.height)

        if rel_x > rel_y:
            direction = 'HORIZONTAL'
            factor = rel_x
        else:
            direction = 'VERTICAL'
            factor = rel_y

        bpy.ops.screen.area_split(
            'INVOKE_DEFAULT',
            direction=direction,
            factor=factor,
            cursor=(event.mouse_region_x, event.mouse_region_y),
        )

        return {'FINISHED'}


def register():
    args = dict(name='Screen', type='MIDDLEMOUSE', value='PRESS', alt=True)
    km.add(SCREEN_OT_merge_areas, **args, shift=True)
    km.add(SCREEN_OT_split_areas, **args, ctrl=True)


def unregister():
    km.remove()
