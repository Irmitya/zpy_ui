import bpy


def draw_playback(self, context):
    layout = self.layout
    horizontal = (layout.direction == 'VERTICAL')
    if horizontal:
        row = layout.row()
        sub = row.row(align=True)
    else:
        sub = layout

    sub.popover(
        panel="TIME_PT_playback",
        text="Playback",
    )


menus = (
    bpy.types.DOPESHEET_MT_editor_menus,
    bpy.types.GRAPH_MT_editor_menus,
    bpy.types.NLA_MT_editor_menus,
    bpy.types.SEQUENCER_MT_editor_menus,
)


def register():
    for menu in menus:
        menu.prepend(draw_playback)


def unregister():
    for menu in menus:
        menu.remove(draw_playback)
