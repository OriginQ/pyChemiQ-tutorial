# 先导入需要用到的包
from pychemiq import Molecules,ChemiQ,QMachineType
from pychemiq.Transform.Mapping import jordan_wigner,MappingType
from pychemiq.Optimizer import vqe_solver
from pychemiq.Circuit.Ansatz import UCC
import numpy as np
import scipy.optimize as opt

def loss(para,grad,iters,fcalls):
    res = chemiq.getLossFuncValue(0,para,grad,iters,fcalls,pauli,chemiq.qvec,ansatz)
    return res[1]

def optimScipy():
    options = {"maxiter":200}
    init_grad = np.zeros(ansatz.get_para_num())
    method = "SLSQP"
    res = opt.minimize(loss,init_para,
            args=(init_grad,0,0),
            method = method,
            options = options)
    final_results = {
            "energy":res.fun,
            "fcalls":f"函数共调用{res.nfev}次",
    }
    print(final_results)


# 初始化氢分子的电子结构参数，包括电荷、基组、原子坐标(angstrom)、自旋多重度
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


# 优化器使用外部scipy库的SLSQP，这时我们需要先定义损失函数
pauli = pauli_H2
init_para = np.zeros(ansatz.get_para_num())
optimScipy()


