import json
import os.path
from pathlib import Path

def gen(d, fpath):
  dirname, base = os.path.dirname(fpath), os.path.splitext(os.path.basename(fpath))[0]
  with open(Path(dirname) / (base + '.json'), 'w') as w:
    json.dump(d, w)
