import bpy
import os

package_dir = os.path.dirname(__file__)
filepath = os.path.join(package_dir, "Lego.blend")
node_group_name = "Lego"
material_name_to_import = "DefaultLegoMaterial"

def import_data(filepath_arg):
    with bpy.data.libraries.load(filepath_arg, link=False) as (data_from, data_to):
        data_to.node_groups = [name for name in data_from.node_groups if name.startswith(node_group_name)]
        data_to.materials = [name for name in data_from.materials if name == material_name_to_import]
        if not data_to.node_groups:
            print(f"Node group '{node_group_name}' not found in file '{filepath_arg}'")
            return False
        if not data_to.materials:
            print(f"Material '{material_name_to_import}' not found in file '{filepath_arg}'")
            return False
        return True

def apply_geo_node_to_active_object(node_group_name_arg, material_name, density):
    if not bpy.context.active_object:
        print("No active object.")
        return
    active_object = bpy.context.active_object
    if active_object.type != 'MESH':
        print("Active object is not a mesh.")
        return
    if node_group_name_arg not in bpy.data.node_groups:
        print(f"Node group '{node_group_name_arg}' not found.")
        return
    node_group = bpy.data.node_groups[node_group_name_arg]
    geo_mod = active_object.modifiers.new(name="GeometryNodes", type='NODES')
    geo_mod.node_group = node_group
    if material_name != 'None' and material_name in bpy.data.materials:
        material = bpy.data.materials[material_name]
        for node in node_group.nodes:
            if "Material" in node.inputs:
                node.inputs["Material"].default_value = material
    for node in node_group.nodes:
        if node.type == 'VALUE' and node.name == 'Density':
            node.outputs[0].default_value = density
    print(f"Node group '{node_group_name_arg}' successfully added and applied to the active object with material '{material_name}' and density '{density}'.")
