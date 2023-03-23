:py:mod:`pychemiq.Transform`
===============================

Module Contents
---------------
- :py:mod:`pychemiq.Transform.mapping`  

将费米子算符映射为泡利算符的mapping子模块。在使用UCC拟设搭建参数化的量子线路来制备试验波函数时，我们需要输入酉耦合簇算符的映射类型。这时我们通过pychemiq.Transform.mapping.MappingType来指定酉耦合簇算符的映射类型。这里的映射类型需要与哈密顿量的映射方式保持一致，也就是说在计算中我们要保持同一套映射方式。

Classes
~~~~~~~~~~~

.. py:module:: pychemiq.Transform.mapping

   .. py:class:: MappingType

      MappingType这个枚举类有四个不同的取值，分别为：

      .. py:attribute:: Bravyi_Kitaev

      .. py:attribute:: Jordan_Wigner

      .. py:attribute:: Parity

      .. py:attribute:: SegmentParity

---------


**接口示例：**

.. code:: 

      from pychemiq import ChemiQ,QMachineType
      from pychemiq.Transform.Mapping import MappingType
      from pychemiq.Circuit.Ansatz import UCC

      chemiq = ChemiQ()
      machine_type = QMachineType.CPU_SINGLE_THREAD
      # 使用JW映射方式
      mapping_type = MappingType.Jordan_Wigner
      # 使用BK映射方式
      # mapping_type = MappingType.Bravyi_Kitaev
      # 使用Parity映射方式
      # mapping_type = MappingType.Parity
      # 使用SegmentParity映射方式
      # mapping_type = MappingType.SegmentParity
      chemiq.prepare_vqe(machine_type,mapping_type,2,1,4)
      ansatz = UCC("UCCSD",2,mapping_type,chemiq=chemiq)


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


---------


**接口示例：**

  下面这个例子中我们使用以上四种映射方式来将二次量子化后氢分子哈密顿量从费米子算符映射成为泡利算符的形式。首先，初始化分子的电子结构参数，得到费米子形式的哈密顿量。

.. code:: 

      from pychemiq import Molecules

      multiplicity = 1
      charge = 0
      basis =  "sto-3g"
      geom = "H 0 0 0,H 0 0 0.74"

      mol = Molecules(
      geometry = geom,
      basis    = basis,
      multiplicity = multiplicity,
      charge = charge)
      fermion_H2 = mol.get_molecular_hamiltonian()

  通过JW变换得到泡利形式的氢分子哈密顿量并打印结果。

.. code::

      from pychemiq.Transform.Mapping import jordan_wigner
      pauli_H2 = jordan_wigner(fermion_H2)
      print(pauli_H2)

.. code::

      {
      "" : -0.097066,
      "X0 X1 Y2 Y3" : -0.045303,
      "X0 Y1 Y2 X3" : 0.045303,
      "Y0 X1 X2 Y3" : 0.045303,
      "Y0 Y1 X2 X3" : -0.045303,
      "Z0" : 0.171413,
      "Z0 Z1" : 0.168689,
      "Z0 Z2" : 0.120625,
      "Z0 Z3" : 0.165928,
      "Z1" : 0.171413,
      "Z1 Z2" : 0.165928,
      "Z1 Z3" : 0.120625,
      "Z2" : -0.223432,
      "Z2 Z3" : 0.174413,
      "Z3" : -0.223432
      }

  通过BK变换得到泡利形式的氢分子哈密顿量并打印结果。

.. code::

      from pychemiq.Transform.Mapping import bravyi_kitaev
      pauli_H2 = bravyi_kitaev(fermion_H2)
      print(pauli_H2)

.. code::

      {
      "" : -0.097066,
      "X0 Z1 X2" : 0.045303,
      "X0 Z1 X2 Z3" : 0.045303,
      "Y0 Z1 Y2" : 0.045303,
      "Y0 Z1 Y2 Z3" : 0.045303,
      "Z0" : 0.171413,
      "Z0 Z1" : 0.171413,
      "Z0 Z1 Z2" : 0.165928,
      "Z0 Z1 Z2 Z3" : 0.165928,
      "Z0 Z2" : 0.120625,
      "Z0 Z2 Z3" : 0.120625,
      "Z1" : 0.168689,
      "Z1 Z2 Z3" : -0.223432,
      "Z1 Z3" : 0.174413,
      "Z2" : -0.223432
      }

  通过Parity变换得到泡利形式的氢分子哈密顿量并打印结果。

.. code::

      from pychemiq.Transform.Mapping import parity
      pauli_H2 = parity(fermion_H2)
      print(pauli_H2)


.. code::

      {
      "" : -0.097066,
      "X0 Z1 X2" : 0.045303,
      "X0 Z1 X2 Z3" : 0.045303,
      "Y0 Y2" : 0.045303,
      "Y0 Y2 Z3" : 0.045303,
      "Z0" : 0.171413,
      "Z0 Z1" : 0.171413,
      "Z0 Z1 Z2" : 0.120625,
      "Z0 Z1 Z2 Z3" : 0.120625,
      "Z0 Z2" : 0.165928,
      "Z0 Z2 Z3" : 0.165928,
      "Z1" : 0.168689,
      "Z1 Z2" : -0.223432,
      "Z1 Z3" : 0.174413,
      "Z2 Z3" : -0.223432
      }

  通过SP变换得到泡利形式的氢分子哈密顿量并打印结果。

.. code::

      from pychemiq.Transform.Mapping import segment_parity
      pauli_H2 = segment_parity(fermion_H2)
      print(pauli_H2)

.. code::

      {
      "" : -0.097066,
      "X0 Z1 X2" : 0.045303,
      "X0 Z1 X2 Z3" : 0.045303,
      "Y0 Z1 Y2" : 0.045303,
      "Y0 Z1 Y2 Z3" : 0.045303,
      "Z0" : 0.171413,
      "Z0 Z1" : 0.171413,
      "Z0 Z1 Z2" : 0.165928,
      "Z0 Z1 Z2 Z3" : 0.165928,
      "Z0 Z2" : 0.120625,
      "Z0 Z2 Z3" : 0.120625,
      "Z1" : 0.168689,
      "Z1 Z2 Z3" : -0.223432,
      "Z1 Z3" : 0.174413,
      "Z2" : -0.223432
      }
