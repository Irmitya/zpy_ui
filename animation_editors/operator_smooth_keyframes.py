import bpy
from zpy import utils, register_keymaps
km = register_keymaps()


class GRAPH_OT_smooth_blend(bpy.types.Operator):
    bl_description = "Smooth keyframes then transition to the result"
    bl_idname = 'graph.smooth_blend'
    bl_label = "Smooth Keyframes (Soft)"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def description(cls, context, properties):
        return cls.bl_description

    @classmethod
    def poll(cls, context):
        return bpy.ops.graph.smooth.poll(context.copy())

    def __init__(self):
        self.fcurves = dict()
        self.fcurves_sample = dict()
        self.last_iter = self.iterations
        self.last_sample = self.samples

    def invoke(self, context, event):
        utils.update_keyframe_points(context)

        for fc in context.editable_fcurves:
            fcu = self.fcurves[fc.id_data.name, fc.data_path, fc.array_index] = dict()

            for (index, key) in enumerate(fc.keyframe_points):
                if key.select_control_point:
                    fcu[index] = dict(base=[key.co.y, key.handle_left.y, key.handle_right.y])

        self.smooth(context)

        return self.execute(context)

    def smooth(self, context):
        fcurves = dict()
        if self.samples:
            for fc in context.editable_fcurves:
                keys = list()
                for key in reversed(fc.keyframe_points):
                    key.co.x *= self.samples
                    key.handle_left.x *= self.samples
                    key.handle_right.x *= self.samples
                    keys.append(key.co.x)
                fcurves[fc] = keys

            bpy.ops.graph.sample()

        for index in range(self.iterations):
            bpy.ops.graph.smooth()

        for (fc, keys) in fcurves.items():
            delete = list()
            for (index, key) in fc.keyframe_points.items():
                if key.co.x in keys:
                    key.co.x /= self.samples
                    key.handle_left.x /= self.samples
                    key.handle_right.x /= self.samples
                    pass
                else:
                    delete.append(index)
            for index in reversed(delete):
                fc.keyframe_points.remove(fc.keyframe_points[index])

        for fc in context.editable_fcurves:
            fcu = self.fcurves.get((fc.id_data.name, fc.data_path, fc.array_index))
            if not fcu:
                continue
            for (index, key) in enumerate(fc.keyframe_points):
                base = fcu.get(index)
                if base and key.select_control_point:
                    base['smooth'] = [key.co.y, key.handle_left.y, key.handle_right.y]
                    key.co.y = base['base'][0]
                    key.handle_left.y = base['base'][1]
                    key.handle_right.y = base['base'][2]

    def execute(self, context):
        if (self.last_iter != self.iterations) or (self.last_sample != self.samples):
            for fc in context.editable_fcurves:
                fcu = self.fcurves.get((fc.id_data.name, fc.data_path, fc.array_index))
                if not fcu:
                    continue
                for (index, key) in enumerate(fc.keyframe_points):
                    base = fcu.get(index)
                    if base and key.select_control_point:
                        key.co.y = base['base'][0]
                        key.handle_left.y = base['base'][1]
                        key.handle_right.y = base['base'][2]
            self.smooth(context)
            self.last_iter = self.iterations
            self.last_sample = self.samples

        for fc in context.editable_fcurves:
            fcu = self.fcurves.get((fc.id_data.name, fc.data_path, fc.array_index))
            if not fcu:
                continue
            for (index, key) in enumerate(fc.keyframe_points):
                if fcu.get(index) and key.select_control_point:
                    base = fcu[index]['base']
                    smooth = fcu[index]['smooth']
                    key.co.y = utils.lerp(base[0], smooth[0], factor=self.factor / 100)
                    key.handle_left.y = utils.lerp(base[1], smooth[1], factor=self.factor / 100)
                    key.handle_right.y = utils.lerp(base[2], smooth[2], factor=self.factor / 100)
            fc.update()

        return {'FINISHED'}

    factor: bpy.props.FloatProperty(
        name="Factor",
        description="Amount to transition between the original vs smoothed curve",
        default=50,
        soft_min=-0,
        soft_max=100,
        step=3,
        precision=2,
        # options={'SKIP_SAVE'},
        subtype='PERCENTAGE',
    )
    samples: bpy.props.IntProperty(
        name="Samples",
        description="Number of levels to sample keyframe density"
                    ".\nThis helps maintain the existing curve in the smoothed version",
        default=1,
        min=0,
        soft_max=9,
        # options={'SKIP_SAVE'},
    )
    iterations: bpy.props.IntProperty(
        name="Iterations",
        description="Number of times to repeat the smooth operator",
        default=1,
        min=1,
        soft_max=9,
        # options={'SKIP_SAVE'},
    )


def register():
    km.add(GRAPH_OT_smooth_blend, name='Graph Editor', type='S', alt=True)


def unregister():
    km.remove()
