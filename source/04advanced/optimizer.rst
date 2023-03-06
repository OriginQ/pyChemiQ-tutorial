优化器教程
=================================

  在拟设教程中我们构造了含参数的拟设线路，进行量子期望估计后，需要不断迭代优化Ansatz中涉及的参数以获取最低的能量，并以此能量最低的叠加态作为当前分子模型的基态。VQE中对这些参数的优化是利用经典优化器来处理的，截止目前，pyChemiQ提供了以下几种优化器：NELDER-MEAD、POWELL、COBYLA、L-BFGS-B、SLSQP和Gradient-Descent。其中无导数优化方法为NELDER-MEAD、POWELL、COBYLA; 一阶方法为L-BFGS-B、SLSQP和Gradient-Descent。在pyChemiQ中，我们通过在最后的VQE求解器中的method来指定不同的经典优化器。

.. code-block::

    # 用method指定经典优化器与初始参数并迭代求解
    #method = "NELDER-MEAD"
    #method = "POWELL"
    #method = "COBYLA"
    #method = "L-BFGS-B"
    #method = "Gradient-Descent"
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

  除了使用pyChemiQ自带的优化器外，我们也可以调用外部的python库来实现经典优化部分，这里我们以调用scipy.optimize为例。首先我们要先要利用chemiq.getLossFuncValue()来得到损失函数：


.. code-block::

    # 优化器使用外部scipy库的SLSQP，这时我们需要先定义损失函数
    def loss(para,grad,iters,fcalls):
        res = chemiq.getLossFuncValue(0,para,grad,iters,fcalls,pauli,chemiq.qvec,ansatz)
        return res[1]

    def optimScipy():
        import scipy.optimize as opt
        options = {"maxiter":2}
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

    # 在主函数中指定loss函数中的泡利哈密顿量pauli和优化器的初始参数init_para
    if __name__ == "__main__":
        pauli = pauli_H2
        init_para = np.zeros(ansatz.get_para_num())
        optimScipy()


  如果不想使用现有的优化器，我们也可以自己定义优化器，下面我们以梯度下降法为例。首先我们要先利用chemiq.getExpectationValue()得到期望值来定义损失函数：

.. code-block::

    # 优化器使用自定义的梯度下降法，首先定义损失函数：
    def loss3(para,grad):
        new_para[:] = para[:]
        global result
        result = chemiq.getExpectationValue(0,0,0,chemiq.qvec,H,new_para,ansatz,False)
        if len(grad) == len(para):
            for i in range(len(para)):
                new_para[i] += delta_p
                result_p = chemiq.getExpectationValue(0,0,0,chemiq.qvec,H,new_para,ansatz,False)
                grad[i] = (result_p - result)/delta_p
                new_para[i] -= delta_p
        return result
    def GradientDescent():
        para_num = ansatz.get_para_num()
        seed = 20221115
        np.random.seed(seed)
        para = np.zeros(para_num)
        grad = np.zeros(para_num)
        lr = 0.1
        result_previous = 0
        result = 0
        threshold = 1e-8
        for i in range(1000):
            result_previous = result
            result = loss3(para,grad)
            para -= lr*grad
            if abs(result - result_previous) < threshold:
                print("final_energy :",result)
                print("iterations :",i+1)
                break
    # 在主函数中指定loss函数中的泡利哈密顿量H和参数delta_p，以及初始参数new_para
    if __name__ == "__main__":
        new_para = np.zeros(ansatz.get_para_num())
        delta_p = 1e-3
        H = pauli_H2.to_hamiltonian(True)
        GradientDescent()
