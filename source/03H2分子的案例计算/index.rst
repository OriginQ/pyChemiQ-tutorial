H2分子的案例计算
=================================
 

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

   # 初始化分子的电子结构参数，包括电荷、基组、电子坐标、自旋多重度
   multiplicity = 1
   charge = 0
   basis =  "sto-3g"
   geom = "H 0 0 0,H 0 0 0.74"

   mol = Molecules(
      geometry = geom,
      basis    = basis,
      multiplicity = multiplicity,
      charge = charge)
   # 得到费米子形式的氢分子哈密顿量
   fermion_H2 = mol.get_molecular_hamiltonian()
   print(fermion_H2)
   # 得到泡利形式的氢分子哈密顿量
   pauli_H2 = jordan_wigner(fermion_H2)
   print(pauli_H2)

   n_qubits = pauli_H2.get_max_index() + 1
   print("n_qubits = ",n_qubits)

   # 设置簇算符需要的映射方法及簇算符类型
   mapping_type = MappingType.Jordan_Wigner
   ansatz = UCC("UCCSD",mol.n_electrons,n_qubits,mapping_type)

   chemiq = ChemiQ()
   machine_type = QMachineType.CPU_SINGLE_THREAD
   pauli_size = len(pauli_H2.data())
   n_elec = mol.n_electrons
   chemiq.prepare_vqe(machine_type,mapping_type,n_elec,pauli_size,n_qubits)

   # 计算损失函数
   def loss(para,grad,iters,fcalls):
      return chemiq.getLossFuncValue(0,para,grad,iters,fcalls,pauli_H2,chemiq.qvec,ansatz)


   print("parameter number is ",ansatz.get_para_num())
   init_para = np.zeros(ansatz.get_para_num())
   result = vqe_solver(loss,method="SLSQP",init_para=init_para)
   print(result.fun_val)
   
 
   