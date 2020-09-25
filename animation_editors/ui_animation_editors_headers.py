import bpy
from . ui_draw_right import draw as draw_right


def draw(self, context):
    draw_right(self, context)


def register():
    bpy.types.GRAPH_HT_header.append(draw)
    bpy.types.NLA_HT_header.append(draw)
    bpy.types.DOPESHEET_HT_header.append(draw)


def unregister():
    bpy.types.DOPESHEET_HT_header.remove(draw)
    bpy.types.GRAPH_HT_header.remove(draw)
    bpy.types.NLA_HT_header.remove(draw)
