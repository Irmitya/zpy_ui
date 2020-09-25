import bpy


class GRAPH_OT_remove_unused_bones(bpy.types.Operator):
    bl_description = "Remove selected fcurves of bones without any changes (like clean channels but check multiple fcurves, not just the fcurve itself)"
    bl_idname = 'graph.remove_unused_bones'
    bl_label = "Remove Unused Bone Fcurves"
    bl_options = {'UNDO'}

    @classmethod
    def description(cls, context, properties):
        return cls.bl_rna.description

    # @classmethod
    # def poll(cls, context):
        # return context.selected_editable_fcurves

    # def invoke(self, context, event):
        # utils.update_keyframe_points(context)
        # return self.execute(context)

    def execute(self, context):
        bones = dict()

        def scan(fc, bone):
            # Initial check in list
            id = (bone, fc.id_data)
            if (id not in bones):
                bones[id] = list()
            elif not bones[id]:
                # one of the bone's fcurves was found to be used, so skip
                return

            # Scan modifiers for animation being generated
            for mod in fc.modifiers:
                if mod.type != 'CYCLES':
                    # modifier likely adds something, so bone is used
                    return bones[id].clear()

            last_value = None
            for key in fc.keyframe_points:
                if (last_value is None):
                    last_value = key.co.y
                elif (last_value != key.co.y):
                    # there's a change in this fcurve
                    # Note: It's possible to be an unnoticable change like 0.000000025 / 1
                    #       but ignore that and just consider it changed
                    return bones[id].clear()

            # Fcurve was found to not have any changes, so add it to queue for deletion
            bones[id].append((fc.data_path, fc.array_index))

        for fc in context.selected_editable_fcurves:
            if not fc.data_path.startswith('pose.bones'):
                continue

            # Get bone name from fcurve
            bone = fc.data_path.split('["', 1)[1].split('"]', 1)[0]

            scan(fc, bone)

        # Go through all the cache and delete unused fcurves
        for ((bone, action), fcurves) in bones.items():
            while fcurves:
                (path, index) = fcurves.pop()
                action.fcurves.remove(action.fcurves.find(path, index=index))

        return {'FINISHED'}


# def register():
    # bpy.types.GRAPH_MT_channel.append(draw)


# def unregister():
    # bpy.types.GRAPH_MT_channel.remove(draw)
