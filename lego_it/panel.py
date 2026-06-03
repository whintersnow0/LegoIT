import bpy
from .operators import OBJECT_OT_import_lego_node_group

class LegoItPanel(bpy.types.Panel):
    bl_label = "LegoIt"
    bl_idname = "OBJECT_PT_lego_it"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_import_lego_node_group.bl_idname, text="Import Lego Geometry Nodes", icon='NODETREE')
