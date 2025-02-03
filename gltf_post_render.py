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
for image in gltf_obj["images"]:
    image_name = Path(image["uri"]).stem
    image["name"] = image_name
  
print("done adding names to images")  
    
updated_contents = json.dumps(gltf_obj)

rosy_asset_dir = os.environ.get("ROSY_ASSET_DIR", "nope")
print("done updating gltf")

print("writing to asset dir:", rosy_asset_dir)
try:
    f = open(rosy_asset_dir + "\\houdini\\exports\\Box_002\\Box_002.gltf", 'w', encoding="utf-8")
    print("opened?")
    f.write(updated_contents)
    f.close()
except Exception as e:
    hou.ui.displayMessage(e)
    
print("done writing gltf")