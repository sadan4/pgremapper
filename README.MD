this is a very basic remapper for keys on linux

thanks to xkeysnail for an example of how to do this

```bash
pip install --requirement requirements.txt
```
## in config.py: 
* map keys to remaps
* edit device_numbers to have the numbers of the devices you want to be remapped. the numbers are the final numbers of /dev/input/event
* edit the window class to match with the window you want remapped. you can find this with `$ xprop WM_CLASS` and then click on the window you want the class of