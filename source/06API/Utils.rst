:py:mod:`pychemiq.Utils`
============================

.. py:module:: pychemiq.Utils


Module Contents
---------------

Functions
~~~~~~~~~~~

.. py:function:: get_cc_n_term(n_qubits, n_elec, excited_level)

   得到指定激发水平的耦合簇算符项数。例如：对于4个量子比特，2电子体系的单双激发耦合簇算符，自旋轨道0和1为占据态，故耦合簇项数为五项：0->2,0->3,1->2,1->3,01->23。

   :param int n_qubits: 输入计算所需的量子比特数。
   :param int n_elec: 输入分子体系的电子数。
   :param str excited_level: 输入耦合簇算符的激发水平。目前可选：CCS、CCD、CCSD。

   :return: 输出指定激发水平的耦合簇算符项数。整数型。



.. py:function:: get_cc(n_qubits, n_elec, para, excited_level='SD')

   得到含参的指定激发水平的耦合簇算符。例如：对于4个量子比特，2电子体系的单双激发耦合簇算符，自旋轨道0和1为占据态，故激发后的耦合簇项为：0->2,0->3,1->2,1->3,01->23。输出的费米子算符为：{ {"2+ 0":para[0]},{"3+ 0":para[1]},{"2+ 1":para[2]},{"3+ 1":para[3]}, {"3+ 2+ 1 0":para[4]} }

   :param int n_qubits: 输入计算所需的量子比特数。
   :param int n_elec: 输入分子体系的电子数。
   :param list[float] para: 输入初始参数列表。
   :param str excited_level: 输入耦合簇算符的激发水平。目前可选：CCS、CCD、CCSD。默认为单双激发耦合簇算符(CCSD)。

   :return: 输出指定激发水平的耦合簇算符。费米子算符类。




.. py:function:: transCC2UCC(Pauli)

   只有酉算子才可以放在量子线路上进行模拟。该函数在耦合簇算符的基础上，将其中不是厄米矩阵的算子删去，构造出“酉算子版本”的耦合簇算符。

   :param PauliOperator Pauli: 输入耦合簇算符。泡利算符类。

   :return: 输出酉耦合簇算符。泡利算符类。
   

---------

**接口示例：**

下面这个例子中，我们计算4个量子比特，2电子体系的单双激发耦合簇算符，并将其转化为可以直接构建量子线路拟设的酉耦合簇算符。

.. code:: 

    from pychemiq.Utils import get_cc_n_term,get_cc,transCC2UCC
    from pychemiq.Transform.Mapping import jordan_wigner
    import numpy as np

    # 计算4个量子比特，2电子体系的单双激发耦合簇算符的项数来初始化参数列表，这里我们先令初参为全1的列表
    n_para = get_cc_n_term(4,2,"CCSD")
    para = np.ones(n_para)

    # 打印设定初参后，4个量子比特，2电子体系的单双激发耦合簇算符
    cc_fermion = get_cc(4,2,para,"CCSD")
    print(cc_fermion)

打印的结果为：

.. code:: 

    {
    2+ 0 : 1.000000
    3+ 0 : 1.000000
    2+ 1 : 1.000000
    3+ 1 : 1.000000
    3+ 2+ 1 0 : 1.000000
    }


.. code:: 

    # 接着使用JW映射将费米子算符映射成泡利算符
    cc_pauli = jordan_wigner(cc_fermion)
    # 将非酉耦合簇算符删去，留下酉耦合簇算符
    ucc_pauli = transCC2UCC(cc_pauli)
    print(ucc_pauli)

打印的结果为：

.. code:: 

    {
    "X0 X1 X2 Y3" : -0.125000,
    "X0 X1 Y2 X3" : -0.125000,
    "X0 Y1 X2 X3" : 0.125000,
    "X0 Y1 Y2 Y3" : -0.125000,
    "X0 Z1 Y2" : 0.500000,
    "X0 Z1 Z2 Y3" : 0.500000,
    "X1 Y2" : 0.500000,
    "X1 Z2 Y3" : 0.500000,
    "Y0 X1 X2 X3" : 0.125000,
    "Y0 X1 Y2 Y3" : -0.125000,
    "Y0 Y1 X2 Y3" : 0.125000,
    "Y0 Y1 Y2 X3" : 0.125000,
    "Y0 Z1 X2" : -0.500000,
    "Y0 Z1 Z2 X3" : -0.500000,
    "Y1 X2" : -0.500000,
    "Y1 Z2 X3" : -0.500000
    }

