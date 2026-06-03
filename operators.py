import bpy
import os
from . import utils

def get_materials(self, context):
    materials = [(mat.name, mat.name, "") for mat in bpy.data.materials]
    if not materials:
        materials.append(('None', 'None', ''))
    return materials

class OBJECT_OT_import_lego_node_group(bpy.types.Operator):
    bl_idname = "object.import_lego_node_group"
    bl_label = "Import Lego Geometry Nodes"
    bl_options = {'REGISTER', 'UNDO'}

    material_name = bpy.props.EnumProperty(
        name="Material Name",
        items=get_materials
    )

    density = bpy.props.FloatProperty(
        name="Density",
        default=0.1,
        min=0.000,
        max=1.000
    )

    def execute(self, context):
        if not os.path.exists(utils.filepath):
            self.report({'ERROR'}, f"File '{utils.filepath}' does not exist.")
            return {'CANCELLED'}
        if utils.import_data(utils.filepath):
            utils.apply_geo_node_to_active_object(utils.node_group_name, self.material_name, self.density)
            self.report({'INFO'}, f"Lego node group '{utils.node_group_name}' successfully imported and applied with material '{self.material_name}' and density '{self.density}'.")
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, f"Failed to import Lego node group '{utils.node_group_name}'.")
            return {'CANCELLED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "material_name")
        layout.prop(self, "density")
