import tcod

movement_settings = {
    'up': {'move': (0, -1)}, 
    'down': {'move': (0, 1)},
    'right': {'move': (1, 0)},
    'left': {'move': (-1, 0)},
    'u': {'move': (1, -1)},
    'y': {'move': (-1, -1)},
    'b': {'move': (-1, 1)},
    'n': {'move': (1, 1)},
    '.': {'pass': (0, 0)},
    'enter_lalt': {'fullscreen': True},
    'escape': {'exit': True},
    's': {'save': True}
    }

title_screen_settings = {
    
    'up': 'up',
    'down': 'down',
    'enter': 'enter'
}

def handle_keys(key, settings):
    # settings is dict
    key_char = chr(key.c)

    try:
        if key.vk == tcod.KEY_UP or key_char == 'k':
            return settings['up']

        elif key.vk == tcod.KEY_DOWN or key_char == 'j':
            return settings['down']

        elif key.vk == tcod.KEY_RIGHT or key_char == 'l':
            return settings['right']

        elif key.vk == tcod.KEY_LEFT or key_char == 'h':
            return settings['left']

        elif key_char == 'u':
            return settings['u']

        elif key_char == 'y':
            return settings['y']

        elif key_char == 'b':
            return settings['b']

        elif key_char == 'n':
            return settings['n']

        elif key_char == '.':
            return settings['.']

        elif key.vk == tcod.KEY_ENTER:
            return settings['enter']

        elif key_char == 's':
            return settings['s']

        if key.vk == tcod.KEY_ENTER and key.lalt:
            return settings['enter_lalt']

        elif key.vk == tcod.KEY_ESCAPE:
            return settings['escape']

    except KeyError:
        return {}

    # this is deprecated

    return {}
