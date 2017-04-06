"""
A Python wrapper for osu!next Signature Generator,
original url here: https://lemmmy.pw/osusig/
"""
from enum import Enum


class Mode(Enum):
    """
    A class for available osu game modes
    """
    osu = 0
    taiko = 1
    ctb = 2
    mania = 3


def generate(name: str, colour: str, mode: Mode = Mode.osu, pp_dis: int = None,
             **advanced):
    """
    Generate the signature for a given osu player name.
    :param name: the name of the osu player
    :type name: str
    
    :param colour: the colour of the signature, in hex
    :type colour: str
    
    :param mode: the game mode for the signature, default is osu
    :type mode: osu_sig.Mode
    
    :param pp_dis: Performance Points Display options, default is None
    :type: int
    None: don't show,
    0: replace level,
    1: after accuracy,
    2: above rank
    
    :param advanced: advanced options, see below.
    
    :param removemargin: Remove extra margin from avatar if True.
    :type removemargin: bool
    
    :param flagshadow: Add a shadow behind the flag if True.
    :type flagshadow: bool
    
    :param flagstroke:  Add a white outline to the flag if True.
    :type flagstroke: bool
    
    :param opaqueavatar: Add a background behind the avatar if True.
    :type opaqueavatar: bool
    
    :param darktriangles: Darken the triangles on the header if True.
    :type darktriangles: bool
    
    :param darkheader: Use dark text on the header if True.
    :type darkheader: bool
    
    :param avatarrounding: Set a custom rounding for the avatar.
    The larger the number is the more of the avatar is rounded away.
    :type avatarrounding: int
    
    :param rankedscore: Show your ranked score (replaces playcount) if True.
    :type rankedscore: bool
    
    :param xpbar: Show an XP bar at the bottom if True.
    :type xpbar: bool
    
    :param xpbarhex: Use signature colour for XP bar if True.
    To use this parameter, you must also set xpbar to True.
    :type xpbarhex: bool
    
    :param onlineindicator: Show an online indicator (slows down signature)
    :type onlineindicator: int
    1: Glow around the signature
    2: Green triangle in avatar
    3: Glow and triangle
    :return: The osu signature link for that player
    """
    name = name.replace(' ', '%20')
    mode = str(mode.value)
    url = 'http://lemmmy.pw/osusig/sig.php?colour=hex{}&uname={}&mode={}'\
        .format(colour, name, mode)
    if pp_dis in [0, 1, 2]:
        url += '&pp={}'.format(pp_dis)
    if advanced == {}:
        return url
    else:
        return url + __format_param(advanced)


def __format_param(param):
    """
    Clean up the advanced parameter from generate()
    :param param: the advanced parameter from generate()
    :return: string of formatted parameters
    """
    bool_list = ['removemargin', 'flagshadow', 'flagstroke', 'opaqueavatar',
                 'darktriangles', 'darkheader', 'rankedscore']
    xp = ['xpbar', 'xpbarhex']
    int_list = ['avatarrounding', 'onlineindicator']
    res = ''
    if xp[0] in param and xp[1] in param \
            and param[xp[0]] is True and param[xp[1]] is True:
        res += "&{}&{}".format(xp[0], xp[1])
    elif xp[0] in param and xp[1] not in param and xp[0] is True:
        res += '&{}'.format(xp[0])
    for key, val in param.items():
        if key in bool_list and val is True:
            res += '&{}'.format(key)
        if key in int_list and isinstance(val, int):
            res += '&{}={}'.format(key, str(val))
    return res
