:py:mod:`pychemiq.Transform`
===============================

Module Contents
---------------
- :py:mod:`pychemiq.Transform.mapping`  

将费米子算符映射为泡利算符的mapping子模块。

Classes
~~~~~~~~~~~

.. py:module:: pychemiq.Transform.mapping

   .. py:class:: MappingType

      MappingType这个枚举类有四个不同的取值，分别为：

      .. py:attribute:: Bravyi_Kitaev

      .. py:attribute:: Jordan_Wigner

      .. py:attribute:: Parity

      .. py:attribute:: SegmentParity


Functions
~~~~~~~~~~~

   .. py:function:: jordan_wigner(fermion)

      将输入的费米子算符通过Jordan Wigner变换映射成为泡利算符。

      :param FermionOperator fermion: 输入待映射的费米子算符。

      :return: 映射后的泡利算符。泡利算符类。



   .. py:function:: bravyi_kitaev(fermion)

      将输入的费米子算符通过Bravyi Kitaev变换映射成为泡利算符。

      :param FermionOperator fermion: 输入待映射的费米子算符。

      :return: 映射后的泡利算符。泡利算符类。



   .. py:function:: parity(fermion)

      将输入的费米子算符通过Parity变换映射成为泡利算符。

      :param FermionOperator fermion: 输入待映射的费米子算符。

      :return: 映射后的泡利算符。泡利算符类。



   .. py:function:: segment_parity(fermion)

      将输入的费米子算符通过segment_parity变换映射成为泡利算符。

      :param FermionOperator fermion: 输入待映射的费米子算符。

      :return: 映射后的泡利算符。泡利算符类。













