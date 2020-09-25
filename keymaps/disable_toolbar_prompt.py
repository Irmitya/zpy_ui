from zpy import register_keymaps
km = register_keymaps()


# https://developer.blender.org/rBde152d072488d1f122b732feaad8b0b4f554f07d
# Tool System: Use tapping Alt as a leader key to switch tools

# This enters a modal when pressing Alt and waits for you to press something.
# It's very inconvenient and I don't even use the toolbar, so disabling.


def register():
    # Insert markers, like inserting keyframes
    km.toggle('wm.toolbar_prompt', name='Window', type='LEFT_ALT', value='CLICK')
    km.toggle('wm.toolbar_prompt', name='Window', type='RIGHT_ALT', value='CLICK')


def unregister():
    km.remove()
