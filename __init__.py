import bpy
from . import operators, panel, handlers

bl_info = {
    "name": "LegoIt",
    "blender": (4, 4, 0),
    "category": "Object",
}

classes = (
    operators.OBJECT_OT_import_lego_node_group,
    panel.LegoItPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    handlers.register_handlers()
    bpy.types.Scene.materials_enum = bpy.props.EnumProperty(
        name="Material Name",
        items=operators.get_materials
    )

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    handlers.unregister_handlers()
    del bpy.types.Scene.materials_enum

if __name__ == "__main__":
    register()
