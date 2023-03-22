:py:class:`pychemiq.FermionOperator`
=========================================

Classes
----------

.. py:class:: FermionOperator({fermion_string: coefficient})

   :param str fermion_string: 字符形式的费米算符。
   :param float coefficient: 该项费米算符的系数。

   :return: 费米算符类。


   .. py:function:: normal_ordered()

   normal\_ordered接口对费米子算符进行整理。在这个转换中规定所作用的轨道编码从高到低进行排序，并且产生算符出现在湮没算符之前。

   .. py:function:: data()

   费米子算符类还提供了data接口，可以返回费米子算符内部维护的数据。

.. note::
    该类的详细介绍请参见进阶教程中的 :doc:`../04advanced/fermionpauliop`。
   
