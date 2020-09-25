from zpy import register_keymaps
km = register_keymaps()


def register():
    km.add('wm.window_fullscreen_toggle', name='Window', type='F10', value='PRESS')


def unregister():
    km.remove()
