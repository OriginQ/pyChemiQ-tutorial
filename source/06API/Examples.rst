配置文件示例
============================

上一节结尾我们给出了常见的几种配置文件示例，在这一节中，我们将给出更多配置文件示例、


1. 在设置量子线路时，使用pauli算符进行自定义拟设。

.. code-block::

    general = {
        task    = energy
        backend = CPU_SINGLE_THREAD
        license = XXXXX
    }

    mole = {
        geoms = {
            H 0.000000 0.000000 0.356115
            H 0.000000 0.000000 -0.356115
        }
        charge  = 0
        spin    = 1
        basis   = sto-3g
    }

    ansatz = User-define{
        pauli = {
            X0 Y2 : -0.125000
            X0 Y2 Z3 : -0.125000
            X0 Z1 Y2 : -0.125000
            X0 Z1 Y2 Z3 : -0.125000
            Y0 X2 : 0.125000
            Y0 X2 Z3 : 0.125000
            Y0 Z1 X2 : 0.125000
            Y0 Z1 X2 Z3 : 0.125000
        }
        mapping  = BK
    }

    optimizer = NELDER-MEAD {
        learning_rate                 = 0.1 
        init_para_type                = MP2
        slices                        = 1 
        iters                         = 1000 
        fcalls                        = 1000 
        xatol                         = 1e-6 
        fatol                         = 1e-6 
    }

2. 使用参数线性组合对自定义线路中的泡利项进行参数优化的限制。

.. code-block::

    general = {
        task    = energy
        backend = CPU_SINGLE_THREAD
        license = XXXXX
    }

    mole = {
        geoms = {
            H 0 0 0.38
            Li 0 0 -1.13
        }
        charge  = 0
        spin    = 1 
        basis   = sto-3g
        active  = 4,4
    }

    ansatz = User-define{
        pauli = {
            X0 Y2 : -0.125
            X0 Y2 Z3 : -0.125
            X0 Z1 Y2 : -0.125
            X0 Z1 Y2 Z3 : -0.125
            Y0 X2 : 0.125
            Y0 X2 Z3 : 0.125
            Y0 Z1 X2 : 0.125
            Y0 Z1 X2 Z3 : 0.125
        }
        mapping       = BK
    }
    optimizer = NELDER_MEAD {
        learning_rate                 = 0.1
        init_para_type                = Zero
        # There are 8 parameters x1,x2,...,x8 since there are 8 pauli items
        # only two variables t1,t2 is used for optimizing
        # x1,x2,x3,x4 = t2
        # x5,x6,x7,x8 = t1
        parameter_matrix = {
            0 0 0 0 1 1 1 1
            1 1 1 1 0 0 0 0
        }
        slices = 1
        iters                         = 200
        fcalls                        = 200
        xatol                         = 1e-4
        fatol                         = 1e-4
    }


3. 在设置量子线路时，使用originIR进行自定义拟设。

.. code-block::

    general = {
        task    = energy
        backend = CPU_SINGLE_THREAD
        license = XXXXX
    }

    mole = {
        geoms = {
            H 0.000000 0.000000 0.356115
            H 0.000000 0.000000 -0.356115
        }
        charge  = 0
        spin    = 1
        basis   = sto-3g
    }

    ansatz = User-define{
        circuit = {
            H q[0]
            RX q[2],(1.5707963)
            CNOT q[0],q[3]
            CNOT q[1],q[3]
            CNOT q[2],q[3]
            RZ q[3],(1.5707963)
            CNOT q[0],q[3]
            CNOT q[1],q[3]
            CNOT q[2],q[3]
            DAGGER
            H q[0]
            RX q[2],(1.5707963)
            ENDDAGGER
        }
        mapping  = BK
    }

    optimizer = NELDER-MEAD {
        learning_rate                 = 0.1 
        init_para_type                = MP2
        slices                        = 1 
        iters                         = 1000 
        fcalls                        = 1000 
        xatol                         = 1e-6 
        fatol                         = 1e-6 
    }


4. 定义分子构型时，直接使用自定义哈密顿量来指定所需要计算的分子。

.. code-block::

    general = {
        task    = energy
        backend = CPU_SINGLE_THREAD
        license = XXXXX
    }

    mole = {
        hamiltonian = {
            : -0.059663
            X0 Z1 X2 : 0.044918
            X0 Z1 X2 Z3 : 0.044918
            Y0 Z1 Y2 : 0.044918
            Y0 Z1 Y2 Z3 : 0.044918
            Z0 : 0.175755
            Z0 Z1 : 0.175755
            Z0 Z1 Z2 : 0.167143
            Z0 Z1 Z2 Z3 : 0.167143
            Z0 Z2 : 0.122225
            Z0 Z2 Z3 : 0.122225
            Z1 : 0.170014
            Z1 Z2 Z3 : -0.236656
            Z1 Z3 : 0.175702
            Z2 : -0.236656
        }
        # nelec is needed when the hamiltonian is user-defined
        nelec = 2
    }
    ansatz = UCC {
        excited_level = SD
        mapping       = BK
    }
    optimizer = NELDER_MEAD {
        learning_rate                 = 0.1
        init_para_type                = Zero
        slices = 1
        iters                         = 200
        fcalls                        = 200
        xatol                         = 1e-4
        fatol                         = 1e-4
    }

5. 执行势能面曲线扫描时，扫描三个原子间的键角，定义为PES_values中四个不同的值。

.. code-block::

    general = {
        task    = PES
        backend = CPU_SINGLE_THREAD
        license = XXXXX
        PES_atoms = 1,2,3
        PES_values = 30,60,90,120
    }

    mole = {
        geoms = {
            H 0.625276 0.625276 0.625276
            C 0.000000 0.000000 0.000000
            H -0.625276 -0.625276 0.625276
            H -0.625276 0.625276 -0.625276
            H 0.625276 -0.625276 -0.625276
        }
        charge  = 0
        spin    = 1
        basis   = sto-3g
        active  = 4,4
    }
    ansatz = UCC{
        excited_level = SD
        mapping       = BK
    }
    optimizer = SLSQP {
        slices = 1
        learning_rate                 = 0.1
        init_para_type                = MP2
        iters                         = 200
        fcalls                        = 200
        xatol                         = 1e-4
        fatol                         = 1e-4
    }

6. 这个例子中，我们使用GAQPSO优化器进行变分量子线路的优化。在这个优化算法中，我们需要额外设置一些参数算法相关的参数。pso_wi指的是最大惯性权重，pso_we指的是最小惯性权重，pso_c1设置粒子向自身最好位置方向的加速常数，pso_c2设置粒子向全局最好位置方向的加速常数；pso_glr是指使用GD或SPSA更新粒子位置时的学习率，pso_deltap设置使用GD时的微扰变量；pso_thres/pso_thresf是指目标函数在当前与上一步迭代的差值阈值，pso_nearenough指粒子距离全局最优点G的距离阈值，pso_cmax设置使用局部搜索的最大次数，pso_alpha/pso_alphae 扩张-收缩系数；下面是一些算法的全局参数设置，pso_repeatn设置算法最大迭代次数，pso_seed设置随机数种子，方便复现结果，pso_n设置种群数量，pso_prefix设置输出结果默认存放的文件夹名称。

.. code-block::

    general = {
        task    = energy
        backend = CPU_SINGLE_THREAD
        license = XXXXX
    }

    mole = {
        geoms = {
            H 0.000000 0.000000 0.356115
            H 0.000000 0.000000 -0.356115
        }
        charge  = 0
        spin    = 1
        basis   = sto-3g
    }

    ansatz = UCC {
        excited_level = SD
        mapping       = BK
    }

    optimizer = GAQPSO {
        learning_rate                 = 0.01
        init_para_type                = MP2

        pso_wi         = 0.8
        pso_we         = 0.8
        pso_c1         = 2.0
        pso_c2         = 3.0
        pso_glr        = 0.01
        pso_deltap     = 1e-4
        pso_thres      = 0.001
        pso_thresf     = 1e-5
        pso_nearenough = 1e-2
        pso_alpha      = 1.0
        pso_alphae     = 0.5
        pso_repeatn    = 1
        pso_seed       = 300
        pso_n          = 20
        pso_cmax       = 2
        pso_prefix     = pso_result

        hamiltonian_simulation_slices = 1
        iters                         = 100
        xatol                         = 1e-8
        fatol                         = 1e-8 
    }
