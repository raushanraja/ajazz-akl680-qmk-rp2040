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

## Refereneces:
- https://config.qmk.fm
- https://switchandclick.com/ansi-vs-iso-layout/
- http://www.keyboard-layout-editor.com
- https://usevia.app
- https://www.caniusevia.com/docs/configuring_qmk 
- https://www.caniusevia.com/docs/download_firmware
- https://www.youtube.com/watch?v=7d5yzBOup9U
- https://learn.adafruit.com/using-qmk-on-rp2040-microcontrollers/overview
- https://learn.adafruit.com/using-qmk-on-rp2040-microcontrollers/rp2040-one-key-keyboard
- https://cdn-learn.adafruit.com/downloads/pdf/using-qmk-on-rp2040-microcontrollers.pdf
- https://www.vikasraj.dev/blog/qmk-pi-pico-rp2040
- https://www.masterzen.fr/2020/05/03/designing-a-keyboard-part-1/
- https://www.masterzen.fr/2020/05/25/designing-a-keyboard-part2/
- https://www.masterzen.fr/2020/10/20/designing-a-keyboard-part3/

## FAQS:
- Invalid protocol error on usevia.app
    - Give user the permisson for device
```bash
# Check the device id
 sudo dmesg -w

# (replace hidraw__ with id shown in dmesg)
sudo chown $USER:$USER /dev/hidraw11
sudo chown $USER:$USER /dev/hidraw12
sudo chown $USER:$USER /dev/hidraw13

```
- https://github.com/qmk/qmk_firmware/issues/22291

