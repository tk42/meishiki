import sys
from enum import Enum
import os
import yaml
from box import Box

try:
    here = os.path.dirname(__file__)
    with open(os.path.join(here, "consts.yaml"), "rb") as f:
        raw = yaml.safe_load(f)
except Exception as e:
    print("Exception occurred while loading YAML...", file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)

kd = Box(raw)


class Sex(Enum):
    """性別を示すEnumクラス"""
    MALE = 0  # 男性
    FEMALE = 1  # 女性


class TemplateType(Enum):
    TYPE_I = "template.html"
    TYPE_II = "template2.html"
