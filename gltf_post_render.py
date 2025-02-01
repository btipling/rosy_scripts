""" Sets the name for images in gltf """
import os
from pathlib import Path
import json
import hou


hou_paths = hou.houdiniPath()
for hou_path in hou_paths:
    print(hou_path)

gltf_path = hou.findFile("exports/Box_002/Box_002.gltf")
print("found gltf path!", gltf_path)
gltf_contents = hou.readFile(gltf_path)
print("read gltf")
gltf_obj = json.loads(gltf_contents)
print("loaded gltf")
print(gltf_obj["images"])
for image in gltf_obj["images"]:
    image_name = Path(image["uri"]).stem
    print(image_name)
    image["name"] = image_name
for image in gltf_obj["images"]:
    print(image)
updated_contents = json.dumps(gltf_obj)

print(updated_contents)

rosy_asset_dir = os.environ.get("ROSY_ASSET_DIR", "nope")
print(rosy_asset_dir)
print("done reading gltf")
try:
    f = open(rosy_asset_dir + "\\houdini\\exports\\Box_002\\Box_022.gltf", 'w', encoding="utf-8")
    print("opened?")
    f.write(updated_contents)
    f.close()
except Exception as e:
    hou.ui.displayMessage(e)
    
print("done updating gltf")