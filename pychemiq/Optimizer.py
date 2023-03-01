# -*- coding: UTF-8 -*-
from pychemiq import OptimizerFactory
import numpy as np
import sys

DEF_NELDER_MEAD      = "Nelder-Mead"
DEF_POWELL           = "Powell"
DEF_COBYLA           = "COBYLA"
DEF_LBFGSB           = "L-BFGS-B"
DEF_SLSQP            = "SLSQP"
DEF_GRADIENT_DESCENT = "Gradient-Descent"
DEF_LEARNING_RATE    = "learning_rate"


def vqe_solver1(loss,
            method=DEF_NELDER_MEAD, 
            init_para = [0, 0],
            Learning_rate = 0.1,
            Xatol=1e-4,
            Fatol=1e-4,
            MaxFCalls=200,
            MaxIter=200):
    """
    Docstrings for method vqe_solver
    """
    if method == "NELDER_MEAD":
        method = DEF_NELDER_MEAD 
    elif method == "POWELL":
        method = DEF_POWELL
    elif method == "L_BFGS_B":
        method = DEF_LBFGSB
    optimizer = OptimizerFactory.makeOptimizer(method)
    
    optimizer.registerFunc(loss, init_para)
    optimizer.setXatol(Xatol)
    optimizer.setFatol(Fatol)
    optimizer.setMaxIter(MaxIter)
    optimizer.setMaxFCalls(MaxFCalls)
    if type(Learning_rate) != type(""):
        Learning_rate = str(Learning_rate)
    optimizer.setOptionalPara({DEF_LEARNING_RATE:Learning_rate})
    optimizer.exec()
    result = optimizer.getResult()
    
    return result 

def vqe_solver(
            method=DEF_NELDER_MEAD, 
            ansatz=None,
            pauli=None,
            init_para = None,
            chemiq=None,
            Learning_rate = 0.1,
            Xatol=1e-4,
            Fatol=1e-4,
            MaxFCalls=200,
            MaxIter=200):
    """
    Docstrings for method vqe_solver
    """

    err = ""
    if chemiq == None:
        err = "ERROR: chemiq is needed!!!"
    if init_para.any() == None:
        err = "ERROR: init_para is needed!!!"
    if pauli== None:
        err = "ERROR: pauli is needed!!!" 
    if ansatz == None:
        err = "ERROR: ansatz is needed!!!"
    if err != "":
        raise ValueError(err)

    if method == "NELDER_MEAD":
        method = DEF_NELDER_MEAD 
    elif method == "POWELL":
        method = DEF_POWELL
    elif method == "L_BFGS_B":
        method = DEF_LBFGSB

    chemiq.setOptimizerType(method)
    chemiq.setOptimizerIterNum(MaxIter)
    chemiq.setOptimizerFuncCallNum(MaxFCalls)
    chemiq.setOptimizerXatol(Xatol)
    chemiq.setOptimizerFatol(Fatol)

    result = chemiq.getOptimizedData(0,init_para,pauli,chemiq.qvec,ansatz)
    
    return result 
