# Ajazz alk680 QMK RP2040
The AKL680 is a mechanical low profile, low cost 68-key Keyboard.
The DIY Project usages Ajazz AKL680, where the original microcontroller, which only supports Bluetooth and lacks wired functionality, has been replaced with an RP2040 microcontroller. 
This modification transforms the keyboard into a wired-only device. Wires has been soldered on PCB and RP2040 to connect the RP2040 to the keyboard's PCB, which features 5 rows and 16 columns. 
The original internal MCU is bypassed entirely, allowing the keyboard to operate solely in wired mode.



* Keyboard Maintainer: [raushanraja](https://github.com/raushanraja)

Make example for this keyboard (after setting up your build environment):

- clone this repo into ~/qmk_firmware/keyboards/alk680
- ` qmk compile -kb akl680 -km via `

Flashing example for this keyboard:
- ` qmk compile -kb akl680 -km via `

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

**Bootmagic reset**: To enter the bootloader, hold down the key at (0,0) in the matrix (the top left key or Escape) and plug in the keyboard.

## Reload the Pervious config:
- Open https://usevia.app
- select save icon, use ./akl-qmk-saved-conf.json to load the saved config
