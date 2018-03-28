def _init():
    global _global_ch
    _global_ch = {}


def set_value(name, value):
    _global_ch[name] = value


def get_value(name, value=None):
    try:
        return _global_ch[name]
    except KeyError:
        return value
