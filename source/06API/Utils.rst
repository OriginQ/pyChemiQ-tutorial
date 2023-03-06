:py:mod:`pychemiq.Utils`
============================

.. py:module:: pychemiq.Utils


Module Contents
---------------

Functions
~~~~~~~~~~~

.. py:function:: get_cc_n_term(n_qubits, n_elec, excited_level)

   得到指定激发水平的耦合簇算符项数。例如：对于4个量子比特，2电子体系的单双激发耦合簇算符(CCSD)，自旋轨道0和1为占据态，故耦合簇项数为五项：0->2,0->3,1->2,1->3,01->23。

   :param int n_qubits: 输入计算所需的量子比特数。
   :param int n_elec: 输入分子体系的电子数。
   :param str excited_level: 输入耦合簇算符的激发水平。目前可选：CCS、CCD、CCSD。

   :return: 输出指定激发水平的耦合簇算符项数。整数型。



.. py:function:: get_cc(n_qubits, n_elec, para, excited_level='SD')

   得到含参的指定激发水平的耦合簇算符。例如：对于4个量子比特，2电子体系的单双激发耦合簇算符(CCSD)，自旋轨道0和1为占据态，故激发后的耦合簇项为：0->2,0->3,1->2,1->3,01->23。输出的费米子算符为：{ {"2+ 0":para[0]},{"3+ 0":para[1]},{"2+ 1":para[2]},{"3+ 1":para[3]}, {"3+ 2+ 1 0":para[4]} }

   :param int n_qubits: 输入计算所需的量子比特数。
   :param int n_elec: 输入分子体系的电子数。
   :param list[float] para: 输入初始参数列表。
   :param str excited_level: 输入耦合簇算符的激发水平。目前可选：CCS、CCD、CCSD。默认为单双激发耦合簇算符(CCSD)。

   :return: 输出指定激发水平的耦合簇算符。费米子算符类。




.. py:function:: transCC2UCC(Pauli)

   只有酉算子才可以放在量子线路上进行模拟。该函数在耦合簇算符的基础上，将其中不是厄米矩阵的算子删去，构造出“酉算子版本”的耦合簇算符。

   :param PauliOperator Pauli: 输入耦合簇算符。泡利算符类。

   :return: 输出酉耦合簇算符。泡利算符类。
   



