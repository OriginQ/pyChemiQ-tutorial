配置文件参数介绍
============================

  除了调用pyChemiQ的基础接口进行计算，您也可以设置配置文件直接运算，更多高级功能开放在配置文件里使用。您可以通过使用内置优化方法缩短量子线路，减少运行时间，还有切片数设置、拟设截断、MP2初参设置等丰富功能的接口可调用。如果您想试用pyChemiQ这些高级功能，请前往 `官网 <https://qcloud.originqc.com.cn/chemistryIntroduce>`_ 申请授权码。ChemiQ和pyChemiQ的license是通用的，如果您已有ChemiQ的license，直接填进配置文件中全局设置的license参数即可。在设置完配置文件后，在终端输入下面的命令行即可运行计算：

.. code-block::

    from pychemiq import directly_run_config
    directly_run_config("test.chemiq")  # 将test替换成您配置文件的名称



  配置文件通常为.chemiq为后缀的文件，主要分五个方面进行设置，详细的参数介绍及默认参数如下：

1. 全局设置(general settings)
    - task : 设置计算类型[energy/MD]，即单点能计算/分子动力学模拟。默认值energy。

    - backend : 设置执行计算的后端类型[CPU_SINGLE_THREAD]。目前仅支持单线程CPU，更多后端类型的接入还在进行中。

    - print_out : 设置是否打印scf迭代过程。默认为F。

    - print_iters : 设置是否打印优化器迭代过程。默认为F。

    - console_level :  设置终端打印日志级别， 0为输出，6为不输出。默认值为0。

    - logfile_name : 设置日志文件名，默认为空。例如，设置的日志名为chemiq.log, 则最终输出的日志名为chemiq-当天日期.log。只有设置了日志文件名，才可以输出日志文件。

    - logfile_level : 设置文件输出日志级别， 0为输出，6为不输出。默认值为6。

    - license : 设置授权序列号。请前往 `官网 <https://qcloud.originqc.com.cn/chemistryIntroduce>`_ 申请授权码。

2. 分子参数设置(Molecule specification)
    - geoms : 设置分子坐标，其中原子类型和原子坐标以空格进行分隔。

    - bohr : 坐标单位是否设置为bohr。布尔值。默认为F，用angstrom为单位。

    - charge : 设置体系的电荷数，电荷数为正时无正号，为负时写负号，默认值0。

    - spin : 设置自旋多重度(M=2S+1)，默认值1。

    - basis : 设置计算所需的基组水平[MINI/sto-3G/sto-6G/3-21G/6-31G]。

    - pure : 使用球谐型还是笛卡尔型Gaussian函数。默认为T, 即使用球谐型Gaussian函数。

    - local : 是否局域化HF轨道。默认为F, 即不局域化HF轨道。

    - active : 设置活性空间，以逗号为分隔符，默认值不设置活性空间。例如active = 4, 4 中第一个4表示4个空间活性轨道，第二个4表示在活性空间中有4个电子。

    - nfrozen : 设置冻结空间轨道数目，默认为0。注：active 与nfrozen不能同时使用。

    - mix_scf : 设置此参数可以有效解决SCF不收敛问题。方法原理为阻尼方法(Damping)。将构建第n+1步Fock矩阵的密度矩阵D(n+1)变为w*D(n-1)+(1-w)*D(n)，此处的w即为设置的参数。参数平均化后的密度矩阵削弱了当前步与上一步密度矩阵之间的差异，使密度矩阵随迭代变化更为平滑，帮助收敛。该参数取值为[0.0, 1.0], 默认为0.5。

3. 拟设参数设置(ansatz settings)
    设置量子线路拟设类型[UCC/Hardware-efficient/Symmetry-presvered/User-define]。选择前三个类型的拟设，量子线路自动生成，选择最后一个线路拟设需要在参数circuit中输入originIR格式的量子线路。详见： `originIR格式介绍 <https://pyqpanda-toturial.readthedocs.io/zh/latest/QProgToOriginIR.html>`_ 。

    - mapping : 设置映射[JK/P/BK/SP]。这几种映射方法分别为Jordan-Wigner Transform，Parity Transform, Bravyi-Kitaev Transform, Segment Parity Transform。

    - excited_level : 设置激发水平[S/D/SD]，仅当ansatz为UCC时生效。

    - restricted : 对激发项进行限制，制备更少组态波函数的叠加态以缩短线路。默认为T。仅当ansatz为UCC时生效。

    - cutoff : 根据MP2的初参对UCC拟设的激发项进行截断。仅当ansatz为UCC且init_para_type=MP2时生效。

    - reorder : 按顺序排列量子比特，前半部分量子比特编码自旋向上，后半部分量子比特编码自旋向下，此参数设置为T时可以减少量子比特的使用。仅当mapping为P时生效。默认为F。

    - circuit : 通过originIR字符串设置线路，仅当ansatz为User-define时生效。

4. 优化器设置(optimizer settings)
    设置经典优化器类型[Nelder-Mead/Powell/Gradient-Descent/COBYLA/L-BFGS-B/SLSQP]。

    - init_para_type : 设置构造初始参数的方式[Zero/Random/input/MP2]，其中Zero表示初参为全零，Random表示初参为[0,1)区间内的随机数，input表示自定义初参，MP2表示为二阶微扰得到的初参结果。其中MP2只在拟设为UCCD和UCCSD时可用。初参默认为Zero。

    - slices : 设置切片数，即量子线路重复次数，默认值1。

    - learning_rate : 设置学习率。默认值0.1。

    - iters : 设置迭代次数，默认值1000。

    - fcalls : 设置函数调用次数，默认值1000。

    - xatol : 设置变量收敛阈值，默认值1e-4。

    - fatol : 设置变量收敛阈值，默认值1e-4。

5. 分子动力学参数设置(molecular dynamics parameter settings)
    - HF : 设置关联采样方法。默认为1。

    - axis : 以字符串形式设置体系沿特定方向运动，格式为"x y z"。

    - save_trajectory : 设置保存分子坐标文件的名称。默认为"traj.csv"。

    - save_topology : 设置保存分子拓扑文件的名称。默认为"topology.txt"。

    - velocity : 设置原子的初始速度，原子间以逗号分隔，"0.1 0.2 0.3, -0.1 -0.2 -0.3\"，单位A/fs，默认值全0。

    - step_size : 设置步长，大于0，单位fs，默认0.2。

    - step_number : 设置总步数，大于1，默认100。

    - delta_r : 设置差分坐标大小，大于0，默认0.001。

下面我们给出一个使用配置文件计算氢分子单点能的案例。基组使用sto-3G，拟设使用UCCSD，映射使用BK，优化器使用NELDER-MEAD。初参为MP2。

.. code-block::

    general = {
        task    = energy
        backend = CPU_SINGLE_THREAD
        license = XXXXX
    }

    mole = {
        geoms = {
            H 0 0 0
            H 0 0 0.74
        }
        bohr    = F
        charge  = 0
        spin    = 1 
        basis   = sto-3G
        pure    = T 
        local   = F 
    }

    ansatz = UCC {
        excited_level = SD
        restricted    = T
        cutoff        = T
        mapping       = BK
        reorder       = F
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


第二个示例我们计算氢分子的势能曲线，这里我们以扫描五个点为例，每个点间隔0.1 angstrom。基组使用sto-3G，活性空间使用[2，2]，拟设使用自定义线路，映射使用parity，优化器使用SLSQP。初参为零。

.. code-block::

    general = {
        task    = energy
        backend = CPU_SINGLE_THREAD
        license = XXXXX
    }

    mole = {
        geoms = {
            H 0 0 0
            H 0 0 0.54;
            H 0 0 0
            H 0 0 0.64;
            H 0 0 0
            H 0 0 0.74;
            H 0 0 0
            H 0 0 0.84;
            H 0 0 0
            H 0 0 0.94
        }
        bohr    = F
        charge  = 0
        spin    = 1 
        basis   = sto-3G
        pure    = T 
        local   = F 
        active = 2,2
    }

    ansatz = User-define {
        circuit = {
            QINIT 4
            CREG 4
            CNOT q[1],q[0]
            CNOT q[2],q[1]
            CNOT q[3],q[2]
            H q[1]
            H q[3]
            S q[1]
    }
        mapping       = P
        reorder       = T
    }

    optimizer = SLSQP {
        learning_rate                 = 0.1 
        init_para_type                = Zero
        slices                        = 1  
        iters                         = 1000 
        fcalls                        = 1000 
        xatol                         = 1e-6 
        fatol                         = 1e-6 
    }


第三个示例我们计算氢化锂分子的分子动力学轨迹。基组使用3-21G，活性空间使用[4，4]，拟设使用Hardware-efficient，映射使用JW，优化器使用L-BFGS-B。初参为随机数。

.. code-block::

    general = {
        task    = MD
        backend = CPU_SINGLE_THREAD
        license = XXXXX
    }

    mole = {
        geoms = {
            H 0 0 0.38
            Li 0 0 -1.13
        }
        bohr    = F
        charge  = 0
        spin    = 1 
        basis   = 3-21G
        pure    = T 
        local   = F 
        active = 4,4
    }

    ansatz = Hardware-efficient {
        mapping       = JW
        reorder       = F
    }

    optimizer = L-BFGS-B {
        learning_rate                 = 0.1 
        init_para_type                = Random
        slices                        = 1  
        iters                         = 1000 
        fcalls                        = 1000 
        xatol                         = 1e-6 
        fatol                         = 1e-6 
    }

    MD = 1 {
        velocity           = 0.0
        step_size          = 0.2
        step_number        = 100 
        delta_r            = 0.001
    }
