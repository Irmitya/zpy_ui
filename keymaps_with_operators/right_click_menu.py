# from zpy import register_keymaps
# import bpy
# km = register_keymaps()


# class RIGHT_MT_click(bpy.types.Menu):
#     bl_description = ""
#     # bl_idname = 'RIGHT_MT_click'
#     bl_label = ""

#     @classmethod
#     def poll(self, context):
#         return True

#     def draw(self, context):
#         layout = self.layout

#         layout.label(text="hhhhhhh")
#         original = dir(bpy.context)
#         temporary = dir(context)
#         for x in original:
#             if x in temporary:
#                 temporary.remove(x)

#         abs(len(temporary) - len(original))


# def register():
#     km.add('wm.call_menu', name='User Interface',
#         type='RIGHTMOUSE', value='PRESS', ctrl=True).name = 'RIGHT_MT_click'


# def unregister():
#     km.remove()
