#!/usr/bin/env python3

import Xlib.display as dis
import evdev as ev
from evdev import uinput, ecodes as ec, InputEvent

from config import keymap, DEVICE_NUMBERS, PG_WINDOW_CLASS

_codes = ec.keys.keys() - ec.BTN
mouse_btns = {256: ['BTN_0', 'BTN_MISC'],
              257: 'BTN_1',
              258: 'BTN_2',
              259: 'BTN_3',
              260: 'BTN_4',
              261: 'BTN_5',
              262: 'BTN_6',
              263: 'BTN_7',
              264: 'BTN_8',
              265: 'BTN_9',
              272: ['BTN_LEFT', 'BTN_MOUSE'],
              274: 'BTN_MIDDLE',
              273: 'BTN_RIGHT'
              }
_codes.update(mouse_btns)
_ui = uinput.UInput(events={
    ec.EV_KEY: _codes,
    ec.EV_REL: set([0, 1, 6, 8, 9])
})


def getWindowClass(d=dis.Display()) -> str:
    cw = d.get_input_focus().focus
    p = _get_class_name(cw)
    return p[1] if p else ""


def _get_class_name(window):
    try:
        wmname = window.get_wm_name()
        wmclass = window.get_wm_class()
        # workaround for Java app
        # https://github.com/JetBrains/jdk8u_jdk/blob/master/src/solaris/classes/sun/awt/X11/XFocusProxyWindow.java#L35
        if (wmclass is None and wmname is None) or "FocusProxy" in wmclass:
            parent_window = window.query_tree().parent
            if parent_window:
                return _get_class_name(parent_window)
            return None
        return wmclass
    except:
        return None


# generate device handles
print([f"/dev/input/event{x}" for x in DEVICE_NUMBERS])
devices = [ev.InputDevice(f"/dev/input/event{x}") for x in DEVICE_NUMBERS]
for device in devices:
    device.grab()


def handle_map(event: InputEvent):
    if getWindowClass() == PG_WINDOW_CLASS:
        print("remapping")
        event.code = keymap[event.code]
    _ui.write_event(event)
    _ui.syn()


try:
    while True:
        for device in devices:
            try:
                for e in device.read():
                    if e.code in keymap:
                        handle_map(e)
                    else:
                        _ui.write_event(e)
                        _ui.syn()
            except BlockingIOError:
                pass
except KeyboardInterrupt:
    for device in devices:
        device.ungrab()
    exit(0)
