量子线路教程
=================================

  在基础教程中的拟设教程我们展示了如何使用Unitary Coupled-Cluster、Hardware-Efficient、Symmetry-Preserved 接口来直接搭建量子线路，这个教程展示的是如何使用用户自定义的方式来构建量子线路拟设。

  通过调用 pychemiq.Circuit.Ansatz 模块下的UserDefine函数，我们可以通过以下两种方式构建线路：第一种是通过本源量子云平台 `图形化编程界面 <https://qcloud.originqc.com.cn/zh/computerServies/quantumVm/5/0/5>`_ 搭建量子线路后导出originIR格式的代码，输入到circuit参数中，第二种是通过输入耦合簇激发项的费米子算符fermion参数来构建量子线路。该函数的接口介绍如下：

.. py:function:: UserDefine(n_electrons, circuit=None, fermion=None, chemiq=None)

      使用用户自定义的方式构建量子线路拟设。

      :param int n_electrons: 输入分子体系的电子数。
      :param str circuit: 构建量子线路的originIR字符串。
      :param FermionOperator fermion: 构建量子线路的费米子算符类。
      :param ChemiQ chemiq: 指定chemiq类。详见pychemiq.ChemiQ。

      :return: 输出自定义拟设的AbstractAnsatz类。


  我们先来示例通过第一种方式来构建量子线路。如下图，首先在本源量子云平台 `图形化编程界面 <https://qcloud.originqc.com.cn/zh/computerServies/quantumVm/5/0/5>`_ 搭建量子线路。

.. image:: ./picture/circuit_originIR.png
   :align: center
   :scale: 40%
.. centered:: 图 1: 通过本源量子云平台图形化编程界面搭建量子线路

搭建完量子线路后导出如下的originIR格式的字符串，再将其输入到UserDefine函数中的circuit参数即可。

.. code-block::

    X q[0]
    X q[1]
    BARRIER q[2]
    BARRIER q[3]
    H q[0]
    H q[1]
    H q[2]
    RX q[3],(-1.570796)
    CNOT q[0],q[3]
    CNOT q[1],q[3]
    CNOT q[2],q[3]
    RZ q[3],(0.785398)
    CNOT q[2],q[3]
    CNOT q[1],q[3]
    CNOT q[0],q[3]
    H q[0]
    H q[1]
    H q[2]
    X1 q[3]

---------

**接口示例：**

.. code:: 

    from pychemiq import Molecules,ChemiQ,QMachineType
    from pychemiq.Transform.Mapping import jordan_wigner,MappingType
    from pychemiq.Optimizer import vqe_solver
    from pychemiq.Circuit.Ansatz import UserDefine
    import numpy as np

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
    pauli_H2 = jordan_wigner(fermion_H2)

    chemiq = ChemiQ()
    machine_type = QMachineType.CPU_SINGLE_THREAD
    mapping_type = MappingType.Jordan_Wigner
    pauli_size = len(pauli_H2.data())
    n_qubits = mol.n_qubits
    n_elec = mol.n_electrons
    chemiq.prepare_vqe(machine_type,mapping_type,n_elec,pauli_size,n_qubits)

    # 使用自定义量子线路，将originIR格式的字符串输入到circuit参数中
    circuit = """
        X q[0]
        X q[1]
        BARRIER q[2]
        BARRIER q[3]
        H q[0]
        H q[1]
        H q[2]
        RX q[3],(fix,-1.570796)
        CNOT q[0],q[3]
        CNOT q[1],q[3]
        CNOT q[2],q[3]
        RZ q[3],(0.785398)
        CNOT q[2],q[3]
        CNOT q[1],q[3]
        CNOT q[0],q[3]
        H q[0]
        H q[1]
        H q[2]
        RX q[3],(fix,1.570796)
    """
    ansatz = UserDefine(n_elec, circuit=circuit, chemiq=chemiq)

    # 最后指定经典优化器与初始参数并迭代求解
    method = "SLSQP"
    init_para = np.zeros(ansatz.get_para_num())
    solver = vqe_solver(
            method = method,
            pauli = pauli_H2,
            chemiq = chemiq,
            ansatz = ansatz,
            init_para=init_para)
    result = solver.fun_val
    print(result)

打印得到的结果为：0.7151043390810803


  第二种是通过输入耦合簇激发项的费米子算符fermion参数来构建量子线路。例如，对于4个量子比特，2电子体系的双激发耦合簇算符，自旋轨道0和1为占据态，激发后的耦合簇项为：01->23。

.. image:: ./picture/CCD.png
   :align: center
   :scale: 40%
.. centered:: 图 2: 四个自旋轨道的氢分子体系由基态到双激发态

  如要构建如上的激发费米子算符我们需要用 FermionOperator 来构建或者通过调用 pychemiq.Utils 模块中的函数 get_cc() 来构建。

.. code:: 

    from pychemiq import FermionOperator
    a = FermionOperator("3+ 2+ 1 0", 1)
    print(a) 

    from pychemiq.Utils import get_cc_n_term,get_cc
    import numpy as np
    n_para = get_cc_n_term(4,2,"CCD")
    para = np.ones(n_para)
    cc_fermion = get_cc(4,2,para,"CCD")
    print(cc_fermion)

二者打印的结果都为：

.. code:: 

    {
    3+ 2+ 1 0 : 1.000000
    }

将得到的激发费米子算符输入到UserDefine函数中的fermion参数即可。这里我们以氢分子为例：

---------

**接口示例：**

.. code:: 

    from pychemiq import Molecules,ChemiQ,QMachineType,FermionOperator
    from pychemiq.Transform.Mapping import jordan_wigner,MappingType
    from pychemiq.Optimizer import vqe_solver
    from pychemiq.Circuit.Ansatz import UserDefine
    import numpy as np

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
    pauli_H2 = jordan_wigner(fermion_H2)

    chemiq = ChemiQ()
    machine_type = QMachineType.CPU_SINGLE_THREAD
    mapping_type = MappingType.Jordan_Wigner
    pauli_size = len(pauli_H2.data())
    n_qubits = mol.n_qubits
    n_elec = mol.n_electrons
    chemiq.prepare_vqe(machine_type,mapping_type,n_elec,pauli_size,n_qubits)

    # 使用自定义量子线路，将自定义的激发费米子算符输入到fermion参数中
    a = FermionOperator("3+ 2+ 1 0", 1)
    ansatz = UserDefine(n_elec, fermion=a, chemiq=chemiq)

    # 最后指定经典优化器与初始参数并迭代求解
    method = "SLSQP"
    init_para = np.zeros(ansatz.get_para_num())
    solver = vqe_solver(
            method = method,
            pauli = pauli_H2,
            chemiq = chemiq,
            ansatz = ansatz,
            init_para=init_para)
    result = solver.fun_val
    print(result)

打印得到的结果为：-1.1372838304374302
