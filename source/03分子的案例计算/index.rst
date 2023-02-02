分子的案例计算
=================================
我们先来看下 :math:`H_2` 分子的案例计算，这里映射方式我们使用JW变换，拟设采用的是UCCSD，优化器方法是SLSQP： 

.. code-block::

   from pychemiq import Molecules,ChemiQ,QMachineType
   from pychemiq.Transform.Mapping import (
        jordan_wigner,
        bravyi_kitaev,
        parity,
        MappingType)
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

   # 得到费米子形式的氢分子哈密顿量并打印结果
       fermion_H2 = mol.get_molecular_hamiltonian()
       print(fermion_H2)
   # 通过JW变换得到泡利形式的氢分子哈密顿量并打印结果
       pauli_H2 = jordan_wigner(fermion_H2)
       print(pauli_H2)

   # 设置簇算符需要的映射方法及簇算符类型，这里我们使用UCCSD拟设
   chemiq = ChemiQ()
   machine_type = QMachineType.CPU_SINGLE_THREAD
   mapping_type = MappingType.Jordan_Wigner
   pauli_size = len(pauli_H2.data())
   n_qubits = pauli_H2.get_max_index() + 1
   n_elec = mol.n_electrons
   chemiq.prepare_vqe(machine_type,mapping_type,n_elec,pauli_size,n_qubits)
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
   print(result,f"调用函数{solver.fcalls}次")
   
 
   