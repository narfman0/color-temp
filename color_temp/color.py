
import argparse
import numpy as np
import colour


def rgb_to_temperature(rgb):
    """ Convert sRGB to temperature in Kelvin.
    First, we convert to tristimulus values.
    Second, we convert to chromaticity coordinates.
    Third, we convert to color temp in K from Hernandez paper.

    Parameters
    ----------
    rgb : List/tuple of rgb values, e.g. [255.0, 235.0, 12.0]

    Returns
    -------
    numeric : CCT (correlated color temperature) in kelvin
    """
    rgb_array = np.array(rgb)
    xyz = colour.sRGB_to_XYZ(rgb_array / 255)
    xy = colour.XYZ_to_xy(xyz)
    cct = colour.xy_to_CCT_Hernandez1999(xy)
    return cct


def temperature_to_rgb(cct):
    """ Convert temperature in Kelvin to sRGB.
    First, we convert CCT (Kelvin) to chromaticity coordinates.
    Second, we convert to tristimulus values.
    Third, we convert to rgb

    Parameters
    ----------
    cct : Correlated color temperature in kelvin

    Returns
    -------
    array : List/tuple of rgb values, e.g. [255.0, 235.0, 12.0]
    """
    xy = colour.CCT_to_xy(cct)
    xyz = colour.xy_to_XYZ(xy)
    rgb = colour.XYZ_to_sRGB(xyz)
    return rgb
