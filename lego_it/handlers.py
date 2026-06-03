import bpy
from . import utils, operators

def update_materials(scene=None, depsgraph=None):
    bpy.types.Scene.materials_enum = bpy.props.EnumProperty(
        name="Material Name",
        items=operators.get_materials
    )

def on_startup(scene):
    if not utils.import_data(utils.filepath):
        print(f"Failed to import data from {utils.filepath}")

def register_handlers():
    bpy.app.handlers.load_post.append(update_materials)
    bpy.app.handlers.depsgraph_update_post.append(update_materials)
    bpy.app.handlers.load_post.append(on_startup)

def unregister_handlers():
    bpy.app.handlers.load_post.remove(update_materials)
    bpy.app.handlers.depsgraph_update_post.remove(update_materials)
    bpy.app.handlers.load_post.remove(on_startup)
