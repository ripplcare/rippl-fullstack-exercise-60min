import sys
from pathlib import Path

# Repo root = tests -> api -> problem -> <root>
ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
