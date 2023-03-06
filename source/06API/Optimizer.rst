:py:mod:`pychemiq.Optimizer`
============================

.. py:module:: pychemiq.Optimizer


Module Contents
---------------


Functions
~~~~~~~~~~~

.. py:function:: vqe_solver(method="NELDER-MEAD", ansatz=None, pauli=None, init_para=None, chemiq=None, Learning_rate=0.1, Xatol=0.0001, Fatol=0.0001, MaxFCalls=200, MaxIter=200)

   该类为VQE求解器，在参数中需要指定经典优化器方法、拟设、分子的泡利哈密顿量、初始参数、chemiq类。

   :param str method: 指定经典优化器方法。目前pyChemiQ支持的方法有NELDER-MEAD、POWELL、COBYLA、L-BFGS-B、SLSQP和Gradient-Descent。若不指定，默认使用NELDER-MEAD优化器。
   :param AbstractAnsatz ansatz: 指定拟设类。详见pychemiq.Circuit.Ansatz。
   :param PauliOperator pauli: 指定分子的泡利哈密顿量。泡利算符类。详见pychemiq.PauliOperator。
   :param list[float] init_para: 指定初始参数。
   :param ChemiQ chemiq: 指定chemiq类。详见pychemiq.ChemiQ。
   :param float Learning_rate: 指定学习率。选择与梯度相关的优化器方法需要此参数。默认为0.1。
   :param float Xatol: 变量的收敛阈值。默认为0.0001。
   :param float Fatol: 函数值的收敛阈值。默认为0.0001。
   :param int MaxFCalls: 函数最大可调用次数。默认为200。
   :param int MaxIter: 最大优化迭代次数。默认为200。

   :return: QOptimizationResult类。详见 `pyqpanda.QOptimizationResult <https://pyqpanda-toturial.readthedocs.io/zh/latest/autoapi/pyqpanda/index.html#pyqpanda.QOptimizationResult>`_ 。

