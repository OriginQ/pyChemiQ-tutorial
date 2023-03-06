:py:class:`pychemiq.PauliOperator`
=========================================

Classes
----------

.. py:class:: PauliOperator({pauli_string: coefficient})

   :param str pauli_string: 字符形式的泡利算符。
   :param float coefficient: 该项泡利算符的系数。

   :return: 泡利算符类。

   .. py:function:: get_max_index()

   得到最大索引值。如果是空的泡利算符项调用get_max_index()接口则返回SIZE_MAX（具体值取决于操作系统），否则返回其最大索引值。

   .. py:function:: data()

   泡利算符类提供了data接口，可以返回泡利算符内部维护的数据。

.. note::
    该类的详细介绍请参见进阶教程中的算符类教程。
   
