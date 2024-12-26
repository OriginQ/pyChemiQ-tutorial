import pyqpanda as pq
import numpy as np

def HE_ansatz(machine_type,qn, para):
    machine = pq.init_quantum_machine(machine_type)
    qlist=pq.qAlloc_many(qn)

    # 构建HE拟设线路
    prog = pq.QProg()
    for i in range(qn):
        prog.insert(pq.RZ(qlist[i], para[4*i]))
        prog.insert(pq.RX(qlist[i], para[4*i+1]))
        prog.insert(pq.RZ(qlist[i], para[4*i+2]))

    for j in range(qn-1):
        ry_control = pq.RY(qlist[j+1], para[4*j+3]).control(qlist[j])
        prog.insert(ry_control)

    ry_last = pq.RY(qlist[0], para[4*qn-1]).control(qlist[qn-1])
    prog.insert(ry_last)

    #print(prog)
    OriginIR=pq.convert_qprog_to_originir(prog, machine)
    print(OriginIR)
    return OriginIR

if __name__ == "__main__":
    machine_type = pq.QMachineType.CPU
    qn=4
    para=np.random.random(4*qn)
    HE_ansatz(machine_type,qn, para)