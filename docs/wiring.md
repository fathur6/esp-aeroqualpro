# Draft logical wiring — MKR WiFi 1010

**Not a physical header orientation or fabrication schematic. Not bench-tested.** Verify printed PCB labels and manufacturer's pinout before connecting.

## Draft wiring image
![Draft MKR WiFi 1010 and Grove air-quality sensor wiring](../hardware/draft-wiring.jpg)

[Original supplied JPEG](https://i.postimg.cc/XYM9t36v/draft-wiring.jpg) · [SVG diagram](../hardware/draft-wiring.svg) · [HTML view](../hardware/draft-wiring.html)

The supplied image retains its original “one HM3301 assumed” caption; **one unit is confirmed**. The written net mapping below governs the connections.

## I2C connections
| Net | Connection |
|---|---|
| SDA, low voltage | MKR D11/SDA → shifter LV1 |
| SCL, low voltage | MKR D12/SCL → shifter LV2 |
| SDA, high voltage | Shifter HV1 → all three I2C sensor SDA pins in parallel |
| SCL, high voltage | Shifter HV2 → all three I2C sensor SCL pins in parallel |
| LV reference | MKR 3V3 → shifter LV |
| HV reference | External regulated +5 V → shifter HV |
| Sensor power | External regulated +5 V → each Grove VCC |
| Ground | MKR GND, shifter GND, every sensor GND and external supply negative all common |

Use a bidirectional open-drain I2C-compatible shifter (e.g. BSS138-type), not a unidirectional signal converter. Both sides need suitable pull-ups; many modules already include them. Confirm the effective parallel resistance and actual bus voltages.

I2C addresses: SGP30 0x58, HM3301 0x40, Multichannel Gas v2 0x08. These are unique for one unit each. The project owner confirmed one HM3301 on 11 October 2026, so no I2C multiplexer is required for the current configuration. For future expansion only, two HM3301 modules at 0x40 would require separate multiplexer channels (e.g. TCA9548A); its wiring/pull-up domains must be designed separately before use.

## Analog connection
```text
Air Quality v1.3 SIG ---- 10 kΩ ----+---- MKR A0
                                   |
                                 15 kΩ
                                   |
                               Common GND
```
Use 1% resistors. White/second signal wire is not connected on this analog module. VCC uses the external 5 V rail, GND uses common ground.

Ideal V_A0 = V_SIG × 15/(10+15) = 0.60 × V_SIG. At 5.0 V SIG, A0 is 3.0 V. An illustrative 5.25 V rail with worst-case 1% resistors gives approximately 3.175 V. The 5.25 V rail is a calculation assumption, not a verified supply specification or a guarantee against transients. Measure the node before connection and keep it below 3.3 V throughout operation; assess resistor loading and add buffering/protection as required.

## Grove cables
| Colour | I2C module | Analog module |
|---|---|---|
| Yellow | SCL | SIG |
| White | SDA | NC |
| Red | VCC | VCC |
| Black | GND | GND |

Verify labels, not colour alone. Grove-to-Dupont leads/breadboard are suitable for a prototype. An UNO Grove Base Shield does not directly match the MKR footprint. MKR I2C is D11/D12, not UNO A4/A5.

## Assembly order
1. With power off, check nets and shorts.
2. Verify regulated rails, level shifter voltages, common GND and analog node without connecting vulnerable MKR inputs.
3. Test each sensor separately; run I2C scan for I2C modules.
4. Integrate bus and check combined pull-ups and voltage behaviour.
5. Establish warm-up/baseline, ADC scaling and repeatability before interpreting readings.
