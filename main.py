import os
import shutil

# Coolest art entry: copy the artwork entry.png beside this file to /output/entry.png.
# The art is a lone astronaut silhouetted before a vast neon nebula and a ringed planet.
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dst_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(dst_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(dst_dir, "entry.png"))
