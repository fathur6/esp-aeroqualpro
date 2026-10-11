# Research notes — draft

## Scope and terminology
- TVOC: total volatile organic compounds; SGP30 reports a broad estimated VOC response, not selective identification of individual compounds.
- eCO2: equivalent carbon dioxide estimate from SGP30; not a direct CO2 sensor.
- PM1 / PM2.5 / PM10: particulate mass-concentration channels associated with nominal particle-size fractions. The HM-3300/3600 family datasheet identifies HM3301 as a mass-concentration model and HM3302 as a counting plus mass-concentration model (selection guide, page 13). Do not assume the family protocol's particle-count fields are supported on HM3301. Preserve the manufacturer's distinction between standard and atmospheric concentration fields when implementing its parser.
- Qualitative gas response: change in sensor response consistent with exposure; not a validated selective gas concentration.
- Air Decarbonation: project name, not an experimentally demonstrated outcome.

## Candidate hardware
| Module | Interface / default 7-bit address | Intended role | Important limitation |
|---|---|---|---|
| Grove VOC and eCO2 SGP30 | I2C / 0x58 | TVOC and eCO2 trend | Not direct CO2 measurement |
| Grove laser dust HM3301 | I2C / 0x40 | Particulate monitoring | One unit confirmed by the project owner; mass-concentration outputs |
| Grove Multichannel Gas Sensor v2 | I2C / 0x08 | Multiple qualitative gas responses | Cross-sensitivity; not calibrated selective gas analysis |
| Grove Air Quality Sensor v1.3 | Analog | Broad indoor air-quality response | Thresholds need validation with divider and MKR ADC |
| Arduino MKR WiFi 1010 | SAMD21, 3.3 V logic | Controller / WiFi | Not ESP32; GPIO not 5 V tolerant |

Product links were supplied by the project owner. Some supplier listings in the supplied context mark the gas v2 module, Air Quality v1.3 and MKR as discontinued. Stock and replacement availability require a fresh purchasing check; no current availability is asserted.

## Proposed power architecture
Use a regulated external 5 V rail for Grove module VCC and the I2C shifter HV reference; MKR is powered through Micro-USB. Share GND only between the power domains. Do not connect the external sensor +5 V rail to MKR USB/5V, 3V3 or GPIO in this draft. This is a conservative prototype architecture, not a claim that every module requires 5 V.

Total steady-state and startup current have not been reconciled. Account for HM3301 fan startup, gas-sensor heaters and supply margin before selecting a supply. Power rails together or isolate signals to avoid back-powering unpowered devices. Verify module revisions, onboard translation and combined pull-ups before assembly.

## Warm-up and interpretation
Supplier guidance for Multichannel Gas Sensor v2 recommends at least 24 hours after storage under one month, 48 hours after 1–6 months, and 72 hours after over six months. Confirm against the actual module documentation. This storage/preconditioning guidance is not a universal runtime stabilization period for all sensors.

SGP30 measurement cadence, initial stabilization, baseline management and humidity compensation must follow manufacturer/library requirements during firmware development. No baseline is measured or saved yet. Analog library thresholds designed around another supply/ADC cannot be reused without checking divider scaling, ADC resolution and sensor loading.

## Validation backlog
- [x] Confirm HM3301 quantity: one unit, confirmed by the project owner on 11 October 2026.
- [ ] Confirm exact PCB revisions and connector labels.
- [ ] Reconcile operating/startup currents and choose final supply rating.
- [ ] Verify I2C shifter/pull-ups and effective bus resistance.
- [ ] Measure analog node under expected/worst-case conditions before attaching A0.
- [ ] Assess analog source loading; buffer if required.
- [ ] Scan each I2C sensor individually, then scan integrated bus.
- [ ] Implement and validate vendor libraries on MKR SAMD21.
- [ ] Validate warm-up, baselines, sampling cadence and ADC thresholds.
- [ ] Record reference comparisons, uncertainty and reproducibility.
- [ ] Add dedicated CO2 sensing if actual CO2 concentration or carbon removal is an objective.

## Evidence status
Documentation review and software-only electrical calculations have been performed. There is no bench test, measured dataset, integrated firmware, calibrated alarm or demonstrated carbon-removal performance in this snapshot. Diagram crossings are not junctions unless identified; written net mapping governs.
