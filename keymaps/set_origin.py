from zpy import register_keymaps
km = register_keymaps()


def register():
    km.add(idname='object.origin_set', name='3D View', type='C', value='PRESS',
    ctrl=True, shift=True, alt=True)


def unregister():
    km.remove()
