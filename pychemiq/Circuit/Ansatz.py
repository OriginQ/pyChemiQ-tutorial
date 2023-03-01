# -*- coding: UTF-8 -*-

from pychemiq import (
    AnsatzFactory
)

from pychemiq.Transform.Mapping import MappingType
from pychemiq import FermionOperator
import numpy as np
from pychemiq.Transform.Mapping import bravyi_kitaev
import sys

DEF_RESTRICTED                    = "restricted"
DEF_CUTOFF                        = "cutoff"
DEF_MAPPING_METHOD                = "mapping method"
DEF_REORDER                       = "reorder"
DEF_HAMILTONIAN_SIMULATION_SLICES = "hamiltonian_simulation_slices"
DEF_EVOLUTION_TIME                = "evolution_time"
DEF_EXCITED_LEVEL                 = "excited_level"
DEF_CIRCUIT                       = "circuit"

DEF_JORDAN_WIGNER                 = "Jordan-Wigner"
DEF_PARITY                        = "Parity"
DEF_BRAVYI_Kitaev                 = "Bravyi-Kitaev"
DEF_SEGMENT_PARITY                = "SegmentParity"

restricted = "T"
cutoff     = "F"
slices     = "1"
evo_time   = 1.0
reorder    = "F"

ansatz_options = {}
ansatz_options[DEF_RESTRICTED] =  restricted
ansatz_options[DEF_CUTOFF] =  cutoff
ansatz_options[DEF_REORDER] =  reorder
ansatz_options[DEF_HAMILTONIAN_SIMULATION_SLICES] =  slices
ansatz_options[DEF_EVOLUTION_TIME] = str(evo_time)



def get_cc_n_term(n_qubits, n_elec,excited_level):   # get_ccsd_n_term接口
    '''
    get the number of coupled cluster single and double(ccsd) terms.
    e.g. 4 qubits, 2 electrons
    then 0 and 1 are occupied,just consider 0->2,0->3,1->2,1->3,01->23
    '''
    if n_elec > n_qubits:
        err = "Qubit num is less than electron num!"
        raise ValueError(err)

    n_diff = n_qubits - n_elec
    res = 0
    if "S" in excited_level:
        res += n_diff * n_elec
    if "D" in excited_level:
        res += n_diff*(n_diff - 1) * n_elec * (n_elec - 1) // 4

    return  res

f_op1 = lambda i,j:str(i) + "+ " + str(j)
f_op2 = lambda i,j,k,l:str(i)+"+ "+str(j)+"+ "+str(k)+" "+str(l)
def get_cc(n_qubits, n_elec, para,excited_level = "SD"):
    '''
    get Coupled cluster single and double terms with parameters(amplitudes before coupled cluster).
    e.g. 4 qubits, 2 electrons
    then 0 and 1 are occupied,just consider 0->2,0->3,1->2,1->3,01->23.
    returned FermionOperator like this:
    { {"2+ 0":para[0]},{"3+ 0":para[1]},{"2+ 1":para[2]},{"3+ 1":para[3]},
    {"3+ 2+ 1 0":para[4]} }
    '''
    if n_elec>n_qubits:
        err = "n_elec is bigger than n_qubits"
        raise ValueError(err)

    if n_elec==n_qubits:
        return FermionOperator()
    if get_cc_n_term(n_qubits, n_elec,excited_level) != len(para):
        err = "parameter number mismatched"
        raise ValueError(err)

    cnt = 0

    fermion_op = FermionOperator()
    if "S" in excited_level:
        for i in range(n_elec):
            for ex in range(n_elec, n_qubits):
                fermion_op += FermionOperator(f_op1(ex,i), para[cnt])
                cnt += 1

    if "D" in excited_level:
        for i in range(n_elec):
            for j in range(i+1,n_elec):
                for ex1 in range(n_elec,n_qubits):
                    for ex2 in range(ex1+1,n_qubits):
                        fermion_op += FermionOperator(f_op2(ex2,ex1,j,i),para[cnt])
                        cnt +=1
    return fermion_op

def UCC(ucc_type,n_electrons,mapping_type,chemiq=None):
    """
    ucc_type: 
        only "UCCS", "UCCD", "UCCSD" are available
    n_electrons:
        number of electrons
    chemiq:
        object of class ChemiQ
    """
    if chemiq == None:
        err = "parameter chemiq should be assigned"
        raise ValueError(err)

    mapping = ""

    if mapping_type == MappingType.Bravyi_Kitaev:
        mapping = DEF_BRAVYI_Kitaev
    elif mapping_type == MappingType.Jordan_Wigner:
        mapping = DEF_JORDAN_WIGNER  
    elif mapping_type == MappingType.Parity:
        mapping = DEF_PARITY
    else:
        err = "ERROR: no such mapping type!!!"
        raise ValueError(err)

    ansatz_options[DEF_MAPPING_METHOD] =  mapping 
    if ucc_type == "UCCS":
        ansatz_options[DEF_EXCITED_LEVEL] =  "S"
    elif ucc_type == "UCCD":
        ansatz_options[DEF_EXCITED_LEVEL] =  "D"
    elif ucc_type == "UCCSD":
        ansatz_options[DEF_EXCITED_LEVEL] =  "SD"
    else:
        err = "ERROR: invalid ucc type"
        raise ValueError(err)

    ansatz = AnsatzFactory.makeAnsatz("UCC",chemiq.qvec,n_electrons,ansatz_options)
    return ansatz

def HardwareEfficient(n_electrons,chemiq=None):
    if chemiq == None:
        err = "parameter chemiq should be assigned"
        raise ValueError(err)
    
    ansatz = AnsatzFactory.makeAnsatz("Hardware-efficient",chemiq.qvec,n_electrons,ansatz_options)
    return ansatz

def SymmetryPreserved(n_electrons,chemiq=None):
    if chemiq == None:
        err = "parameter chemiq should be assigned"
        raise ValueError(err)
    
    ansatz = AnsatzFactory.makeAnsatz("Symmetry-preserved",chemiq.qvec,n_electrons,ansatz_options)
    return ansatz

def UserDefine(n_electrons,circuit=None,fermion=None,option=None,chemiq=None):
    """
    circuit: 
        originir string of the circuit of the ansatz
    n_electrons:
        number of electrons
    n_qubits:
        number of qubits
    chemiq:
        object of class ChemiQ
    """

    if circuit == None and fermion==None:
        err = "no circuit or fermion is assigned"
        raise ValueError(err)

    if option != None:
        for key in option:
            ansatz_options[key] = option[key]
        option = ansatz_options
    else:
        option = ansatz_options
    if circuit != None:
        option[DEF_CIRCUIT] =  circuit
    if fermion != None:
        option["fermion"] =  fermion

    if chemiq == None:
        err = "parameter chemiq should be assigned"
        raise ValueError(err)

    ansatz = AnsatzFactory.makeAnsatz("User-define",chemiq.qvec,n_electrons,option)
    return ansatz
