# -*- coding: UTF-8 -*-

from pychemiq import (
    JordanWignerTransform,
    BravyiKitaevTransform,
    ParityTransform,
    MappingType,
    transCC2UCC
)

def jordan_wigner(fermion):
    """
    Jordan-Wigner Transform
    """
    return JordanWignerTransform(fermion)

def bravyi_kitaev(fermion):
    """
    Bravyi-Kitaev Transform
    """
    return BravyiKitaevTransform(fermion)

def parity(fermion):
    """
    Parity Transform
    """
    return ParityTransform(fermion)

def Transform(fermion,mapping_type):
    """
    Docstrings for method Transform
    """
    if mapping_type == MappingType.Bravyi_Kitaev:
        return bravyi_kitaev(fermion)
    elif mapping_type == MappingType.Jordan_Wigner:
        return jordan_wigner(fermion)
    elif mapping_type == MappingType.Parity:
        return parity(fermion)
    else:
        print("Error: invalid mapping type ",mapping_type)      
    return

