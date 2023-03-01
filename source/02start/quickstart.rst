氢分子案例计算
=================================

  为了快速上手pyChemiQ，我们先来看下 :math:`H_2` 分子的案例计算。在设置参数前，我们先来了解两个名词：映射和拟设。为了在量子计算机上模拟电子结构问题，我们需要一套转换方式，将电子的费米子算符编码到量子计算机的泡利算符，这就是映射(mapping)。为了获得与体系量子终态相近的试验波函数，我们需要一个合适的波函数假设，我们称之为拟设(Ansatz)。并且理论上，假设的试验态与理想波函数越接近，越有利于后面得到正确基态能量。 

  下面氢分子的例子中我们使用sto-3g基组，映射方式使用JW变换，拟设采用UCCSD，经典优化器方法采用SLSQP。这里我们暂不展开每种方法背后的理论背景，详细的介绍参见理论背景章节：

.. code-block::

    # 先导入需要用到的包
    from pychemiq import Molecules,ChemiQ,QMachineType
    from pychemiq.Transform.Mapping import (jordan_wigner,MappingType)
    from pychemiq.Optimizer import vqe_solver
    from pychemiq.Circuit.Ansatz import UCC
    import numpy as np

    # 初始化分子的电子结构参数，包括电荷、基组、原子坐标、自旋多重度
    multiplicity = 1
    charge = 0
    basis =  "sto-3g"
    geom = "H 0 0 0,H 0 0 0.74"

    mol = Molecules(
        geometry = geom,
        basis    = basis,
        multiplicity = multiplicity,
        charge = charge)

    # 利用JW变换得到泡利算符形式的氢分子哈密顿量
    fermion_H2 = mol.get_molecular_hamiltonian()
    pauli_H2 = jordan_wigner(fermion_H2)

    # 准备量子线路，需要指定的参数有量子虚拟机类型machine_type，拟设映射类型mapping_type，
    # 泡利哈密顿量的项数pauli_size，电子数目n_elec与量子比特的数目n_qubits
    chemiq = ChemiQ()
    machine_type = QMachineType.CPU_SINGLE_THREAD
    mapping_type = MappingType.Jordan_Wigner
    pauli_size = len(pauli_H2.data())
    n_qubits = mol.n_qubits
    n_elec = mol.n_electrons
    chemiq.prepare_vqe(machine_type,mapping_type,n_elec,pauli_size,n_qubits)

    # 设置拟设类型，这里我们使用UCCSD拟设
    ansatz = UCC("UCCSD",n_elec,mapping_type,chemiq=chemiq)

    # 指定经典优化器与初始参数并迭代求解
    method = "SLSQP"
    init_para = np.zeros(ansatz.get_para_num())
    solver = vqe_solver(
            method = method,
            pauli = pauli_H2,
            chemiq = chemiq,
            ansatz = ansatz,
            init_para=init_para)
    result = solver.fun_val
    n_calls = solver.fcalls
    print(result,f"函数共调用{n_calls}次")
    energies = chemiq.get_energy_history()
    print(energies)

打印得到的结果为：

.. code-block::

    -1.1372838317140834 函数共调用9次
    [-1.1167593073964257, -1.0382579032966825, -1.137282968297819, -1.137282968297819, -1.1372838302540205, -1.137283647727291, -1.1372838297780967, -1.1372838317140834, -1.1372838317140834]

  我们将pyChemiQ打印出来的数据作图，与同基组下的经典Full CI进行对比。可以看到随着函数迭代次数的增加，电子能量逐渐收敛至Full CI的能量，如下图所示。而且当函数迭代到第二次时电子能量已经达到了化学精度 :math:`1.6\times 10^3` Hartree。

.. image:: ./picture/energy_convergence_H2.png
   :align: center
.. centered:: 图 : 氢分子能量收敛曲线
