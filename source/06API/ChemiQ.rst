:py:class:`pychemiq.ChemiQ`
=============================

Classes
----------

.. py:class:: ChemiQ()

   封装好的量子线路类，为VQE算法中在量子计算机/虚拟机上进行的部分。包括搭建参数化的量子线路来制备试验波函数和对哈密顿量的各个子项进行测量与求和。

   .. py:function:: prepare_vqe(machine_type, mapping_type, n_elec, pauli_size, n_qubits)

   准备VQE算法量子线路的函数。

   :param QMachineType machine_type: 输入量子模拟器类型。目前pyChemiQ仅支持单线程CPU，即QMachineType.CPU_SINGLE_THREAD。含噪声量子模拟器的接入还在进行中。该类的介绍详见 `pyqpanda.QMachineType <https://pyqpanda-toturial.readthedocs.io/zh/latest/autoapi/pyqpanda/index.html#pyqpanda.QMachineType>`_ 。

   :param MappingType mapping_type: 输入映射类型。详见pychemiq.Transform.Mapping。
   :param int n_elec: 输入分子体系的电子数。
   :param int pauli_size: 输入泡利哈密顿量的项数。
   :param int n_qubits: 输入计算所需要的总量子比特数。

   :return: void



   .. py:function:: getExpectationValue(index, fcalls, task_index, qvec, hamiltonian, para, ansatz, extra_measure)

   对线路进行测量得到哈密顿量期望值。

   :param int index: 输入体系编号。
   :param int fcalls: 输入函数调用次数。
   :param int task_index: 任务编号。
   :param QVec qvec: 存储量子比特的数组。该类的介绍详见 `pyqpanda.QVec <https://pyqpanda-toturial.readthedocs.io/zh/latest/autoapi/pyqpanda/index.html#pyqpanda.QVec>`_ 。
   :param Hamiltonian hamiltonian: 输入Hamiltonian类。PauliOperator中的哈密顿量是字符串形式，不利用后续的处理，Hamiltonian在存储方式上将泡利算符其转换成自定义的Hamiltonian类，方便提取每一项的信息。
   :param list[float] para: 指定初始待优化参数。
   :param AbstractAnsatz ansatz: 指定拟设类。详见pychemiq.Circuit.Ansatz。
   :param bool extra_measure: 用于区分噪声模拟和非噪声模拟。布尔值。 

   :return: 哈密顿量期望值，即基态能量。双精度浮点数。



   .. py:function:: getLossFuncValue(index, para, grad, iters, fcalls, pauli, qvec, ansatz)

   得到损失函数的值。

   :param int index: 输入体系编号。
   :param list[float] para: 指定初始待优化参数。
   :param list[float] grad: 指定初始待优化梯度。
   :param int iters: 输入函数迭代的次数。
   :param int fcalls: 输入函数调用的次数。
   :param PauliOperator pauli: 指定分子的泡利哈密顿量。泡利算符类。详见pychemiq.PauliOperator。
   :param QVec qvec: 存储量子比特的数组。该类的介绍详见 `pyqpanda.QVec <https://pyqpanda-toturial.readthedocs.io/zh/latest/autoapi/pyqpanda/index.html#pyqpanda.QVec>`_ 。
   :param AbstractAnsatz ansatz: 指定拟设类。详见pychemiq.Circuit.Ansatz。

   :return: 损失函数的值。dict类型。



   .. py:function:: get_energy_history()

   :return: 每一次函数迭代后的能量值。双精度浮点数数组。


   Example::


      from pychemiq import Molecules,ChemiQ,QMachineType,PauliOperator
      from pychemiq.Transform.Mapping import MappingType
      from pychemiq.Circuit.Ansatz import UCC

      chemiq = ChemiQ()
      machine_type = QMachineType.CPU_SINGLE_THREAD
      mapping_type = MappingType.Jordan_Wigner
      chemiq.prepare_vqe(machine_type,mapping_type,2,4,4)

      ansatz = UCC("UCCD",2,mapping_type,chemiq=chemiq)
      pauli = PauliOperator(" ",0)
      # 期望值函数与代价函数
      H = pauli.to_hamiltonian(True)
      result1 = chemiq.getExpectationValue(0,0,0,chemiq.qvec,H,[0],ansatz,False)
      result2 = chemiq.getLossFuncValue(0,[0],[0],0,0,pauli,chemiq.qvec,ansatz)


