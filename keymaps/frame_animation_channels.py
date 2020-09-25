from zpy import register_keymaps
km = register_keymaps()


def register():
    for (op, editor) in [
    ('action', 'Dopesheet'), ('graph', 'Graph Editor'),
    ('nla', 'NLA Editor'), ('sequencer', 'Sequencer'),
    ]:
        args = dict(name=editor, type='F')
        km.add(f'{op}.view_all', **args, value='CLICK_DRAG')
        km.add(f'{op}.view_selected', **args, value='CLICK')
        km.add(f'{op}.view_frame', **args, value='DOUBLE_CLICK')


def unregister():
    km.remove()
