# Source register

Research snapshot based on the documentation review in this project conversation. Links are references, not redistributed manufacturer files. Specifications must be checked against the purchased module revision.

## Primary sources
- Arduino MKR WiFi 1010: https://docs.arduino.cc/hardware/mkr-wifi-1010/
- Arduino ABX00023 pinout: https://docs.arduino.cc/resources/pinouts/ABX00023-full-pinout.pdf
- Arduino ABX00023 datasheet: https://docs.arduino.cc/resources/datasheets/ABX00023-datasheet.pdf
- SGP30 Grove wiki: https://wiki.seeedstudio.com/Grove-VOC_and_eCO2_Gas_Sensor-SGP30/
- HM3301 Grove wiki: https://wiki.seeedstudio.com/Grove-Laser_PM2.5_Sensor-HM3301/
- HM-3300/3600 family datasheet (HM3301/HM3302 model distinction, selection guide page 13): https://files.seeedstudio.com/wiki/Grove-Laser_PM2.5_Sensor-HM3301/res/HM-3300%263600_V2.1.pdf
- Multichannel Gas v2 wiki: https://wiki.seeedstudio.com/Grove-Multichannel-Gas-Sensor-V2/
- Air Quality v1.3 wiki: https://wiki.seeedstudio.com/Grove-Air_Quality_Sensor_v1.3/
- Multichannel Gas v2 default-address implementation: https://raw.githubusercontent.com/Seeed-Studio/Seeed_Multichannel_Gas_Sensor/master/src/Multichannel_Gas_GMXXX.h
- Multichannel Gas example: https://raw.githubusercontent.com/Seeed-Studio/Seeed_Multichannel_Gas_Sensor/master/examples/basic_demo/basic_demo.ino

## Supplied product references
- https://my.cytron.io/p-grove-voc-and-eco2-sgp30-gas-sensor
- https://my.cytron.io/p-grove-laser-pm2p5-dust-sensor-hm3301
- https://my.cytron.io/p-grove-multichannel-gas-sensor-v2
- https://my.cytron.io/p-grove-air-quality-sensor-v1.3
- https://my.cytron.io/p-arduino-mkr-wiFi-1010

The HM3301 link appeared twice in the supplied list; the project owner confirmed on 11 October 2026 that there is only one HM3301 module. Prices/stock are deliberately omitted because supplied snapshots differ and are time-sensitive.

## Traceability
MKR voltage limits/pins → Arduino pinout/datasheet. Sensor roles/interface limits → Seeed wikis. Gas v2 address 0x08 → Seeed library header/example. Storage preheat guidance → supplied Cytron v2 product text. Divider resistor values and 5 V architecture → proposed engineering design, not vendor certification.
