VERSION = (0, 0, 1)
SUB_VERSION = "ALPHA"
VERSION_S = '.'.join(map(str, VERSION)) + f"-{SUB_VERSION}" if SUB_VERSION else ""
