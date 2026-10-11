"""Software-only checks. No hardware measurement is performed."""
from pathlib import Path
import json
import xml.etree.ElementTree as ET

r_top = 10_000
r_bottom = 15_000
ratio = r_bottom / (r_top + r_bottom)
nominal = 5.0 * ratio
worst_case = 5.25 * (r_bottom * 1.01) / (r_top * 0.99 + r_bottom * 1.01)
addresses = {"SGP30": 0x58, "HM3301": 0x40, "Gas_v2": 0x08}
assert len(set(addresses.values())) == len(addresses)
assert nominal < 3.3 and worst_case < 3.3
root = Path(__file__).resolve().parents[1]
ET.parse(root / "hardware/draft-wiring.svg")
print(json.dumps({"divider_ratio": ratio, "A0_at_SIG_5V": nominal,
                  "A0_at_SIG_5_25V_worst_1pct": worst_case,
                  "i2c_addresses": {k: hex(v) for k, v in addresses.items()},
                  "svg_xml_valid": True, "hardware_tested": False}, indent=2))
