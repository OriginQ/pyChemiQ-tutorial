:py:mod:`pychemiq.Circuit`
==============================

.. py:module:: pychemiq.Circuit


Module Contents
---------------
- :py:mod:`pychemiq.Circuit.Ansatz`  

构建量子线路拟设的Ansatz子模块。


Functions
~~~~~~~~~~~

.. py:module:: pychemiq.Circuit.Ansatz

   .. py:function:: UCC(ucc_type, n_electrons, mapping_type, chemiq=None)

      使用酉耦合簇算符构建量子线路拟设。

      :param str ucc_type: 输入酉耦合簇的激发水平。目前可选：UCCS、UCCD、UCCSD。
      :param int n_electrons: 输入分子体系的电子数。
      :param MappingType mapping_type: 输入酉耦合簇算符的映射类型。详见pychemiq.Transform.Mapping。
      :param ChemiQ chemiq: 指定chemiq类。详见pychemiq.ChemiQ。

      :return: 输出指定激发水平的AbstractAnsatz类。



   .. py:function:: HardwareEfficient(n_electrons, chemiq=None)

      使用HardwareEfficient构建量子线路拟设。

      :param int n_electrons: 输入分子体系的电子数。
      :param ChemiQ chemiq: 指定chemiq类。详见pychemiq.ChemiQ。

      :return: 输出该拟设的AbstractAnsatz类。



   .. py:function:: SymmetryPreserved(n_electrons, chemiq=None)

      使用SymmetryPreserved构建量子线路拟设。

      :param int n_electrons: 输入分子体系的电子数。
      :param ChemiQ chemiq: 指定chemiq类。详见pychemiq.ChemiQ。

      :return: 输出该拟设的AbstractAnsatz类。



   .. py:function:: UserDefine(n_electrons, circuit=None, fermion=None, chemiq=None)

      使用用户自定义的方式构建量子线路拟设。

      :param int n_electrons: 输入分子体系的电子数。
      :param str circuit: 构建量子线路的originIR字符串。
      :param FermionOperator fermion: 构建量子线路的费米子算符类。
      :param ChemiQ chemiq: 指定chemiq类。详见pychemiq.ChemiQ。

      :return: 输出自定义拟设的AbstractAnsatz类。


.. note::
    Ansatz模块前三个函数的详细调用示例请参见基础教程中的 :doc:`../03basis/ansatz`。最后一个函数的调用示例请参见进阶教程中的 :doc:`../04advanced/circuit`。
   




