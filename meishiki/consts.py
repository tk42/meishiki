import sys
from enum import Enum
import yaml
from box import Box
import importlib.resources

try:
    f = importlib.resources.read_binary("meishiki", "consts.yaml")
    raw = yaml.safe_load(f)
except Exception as e:
    print("Exception occurred while loading YAML...", file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)

kd = Box(raw)


class TemplateType(Enum):
    TYPE_I = "template.html"
    TYPE_II = "template2.html"
