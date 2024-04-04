from evdev import ecodes as ec

keymap = {
    ec.BTN_EXTRA: ec.KEY_1,
    ec.BTN_SIDE: ec.KEY_6,
    ec.KEY_Q: ec.KEY_2,
    ec.KEY_E: ec.KEY_5,
    ec.KEY_F: ec.KEY_4,
    # for turret
    ec.KEY_2: ec.KEY_E,
}
DEVICE_NUMBERS = [11, 7, 6]
PG_WINDOW_CLASS = "steam_app_2524890"
