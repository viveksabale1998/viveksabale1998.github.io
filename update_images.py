from PIL import Image
import os

source_path = "/Users/viveksabale/GitHub/sites/static/V_new.png"
dest_png_path = "/Users/viveksabale/GitHub/sites/static/V_new.png"
dest_ico_path = "/Users/viveksabale/GitHub/sites/static/favicon.ico"

try:
    img = Image.open(source_path)
    img.save(dest_png_path, format='PNG')
    print(f"Saved PNG to {dest_png_path}")
    
    img.save(dest_ico_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print(f"Saved ICO to {dest_ico_path}")
except Exception as e:
    print(f"Error processing images: {e}")
