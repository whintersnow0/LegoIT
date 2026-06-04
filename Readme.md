# LegoIt

Blender addon that turns any mesh into a LEGO-style model using Geometry Nodes.

## Demo
(preview/preview.gif)

## Usage

1. Select a mesh object in the viewport
2. Open the **Tools** panel on the right side (`N` key)
3. Find the **LegoIt** tab and click **Import Lego Geometry Nodes**
4. In the dialog, choose a material and set the density
5. Click **OK**

The Geometry Nodes modifier will be applied to the active object.

---

## Parameters

| Parameter | Description | Range |
|-----------|-------------|-------|
| Material  | Material applied to the LEGO bricks | Any material in the scene |
| Density   | Controls how densely bricks fill the mesh | 0.0 – 1.0 |
