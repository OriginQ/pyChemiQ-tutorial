配置文件参数介绍
============================

  除了调用pyChemiQ的基础接口进行计算，您也可以设置配置文件直接运算，更多高级功能开放在配置文件里使用。您可以通过使用内置优化方法缩短量子线路，减少运行时间，还有切片数设置、拟设截断、MP2初参设置等丰富功能的接口可调用。如果您想试用pyChemiQ这些高级功能，请前往 `官网 <https://originqc.com.cn/product/zh/chemistryIntroduce?pid=57&bannerId=88>`_ 申请授权码。ChemiQ和pyChemiQ的license是通用的，如果您已有ChemiQ的license，直接填进配置文件中全局设置的license参数即可。在设置完配置文件后，在终端输入下面的命令行即可运行计算：

.. code-block::

    from pychemiq import directly_run_config
    directly_run_config("test.chemiq")  # 将test替换成您配置文件的名称



  配置文件通常为.chemiq为后缀的文件，下一节中我们将给出更多的配置文件示例。这里主要分六个方面进行设置，详细的参数介绍及默认参数如下：

1. 全局设置(general settings)
   
   必要参数：

    - task(str) : 设置计算类型[energy/PES/MD]，即单点能计算/势能曲线计算/分子动力学模拟。默认值energy。

    - backend(str) : 设置执行计算的后端类型[CPU_SINGLE_THREAD]。目前仅支持单线程CPU，更多后端类型的接入还在进行中。
    
    - license(str) : 设置授权序列号。请前往 `官网 <https://originqc.com.cn/product/zh/chemistryIntroduce?pid=57&bannerId=88>`_ 申请授权码。
    
   计算类型为PES时的必要参数:

    - PES_atoms(int) : 指定势能曲线计算时涉及的原子序号，扫描坐标为键长、键角、二面角时分别涉2，3，4个原子。原子序号即为在分子坐标中其所在的行数，在第一行的原子序号为1，依此类推。
  
    - PES_fast_generation(bool) : 指定生成势能曲线扫描坐标的方式，为T时为快速生成，为F时为自定义生成。

    - PES_values(float) : 当生成方式为快速生成时，需要指定三个值：起始值，终止值，节点个数(int)；当生成方式为自定义生成时，需要指定具体的扫描坐标。其中扫描坐标为键长时单位为angstrom，为键角时单位为角度。此时没有个数限制。

   可选参数：

    - chem_method(str) : 使用何种经典计算方法[HF/CCSD]。默认为HF。
    
    - hamiltonian(str) : 使用该关键字可以自定义哈密顿量进行计算。注意自定义哈密顿量需要设置关键字nelec，即电子数量。

    - print_out(bool) : 设置是否打印scf迭代过程。默认为F。

    - print_iters(bool) : 设置是否打印优化器迭代过程。默认为F。

    - console_level(int) :  设置终端打印日志级别， 0为输出，6为不输出。默认值为0。

    - logfile_name(str) : 设置日志文件名，默认为空。例如，设置的日志名为chemiq.log, 则最终输出的日志名为chemiq-当天日期.log。只有设置了日志文件名，才可以输出日志文件。

    - logfile_level(int) : 设置文件输出日志级别， 0为输出，6为不输出。默认值为6。



2. 分子参数设置(Molecule specification)

   必要参数：

    - mole : 对分子模型相关参数进行设置，默认为空。后接子参数设置。

    - geoms(str) : 设置分子坐标，第一列为元素符号(和序号)，后面原子坐标(x,y,z轴坐标)以空格进行分隔。

    - charge(int) : 设置体系的电荷数，电荷数为正时无正号，为负时写负号，默认值0。

    - spin(int) : 设置自旋多重度(M=2S+1)，默认值1。

    - basis(str) : 设置计算所需的基组水平[MINI/sto-3G/sto-6G/3-21G/6-31G/...]。从V2.4.0起，ChemiQ支持常见的600+个基组及用户自定义基组。支持在 `basis set exchange网站 <https://www.basissetexchange.org/>`_ 上的大部分基组（除少量过大的基组外），包括但不限于STO-nG基组、Pople系列基组、Ahlrichs的def系列基组、Dunning系列基组、赝势基组等。往期版本支持的基组有：MINI、STO-3G、STO-6G、3-21G和6-31G，其他基组可直接输入名称，具体的基组名称字符串输入规则如下：

        - 大写字母转小写字母
        - 保留弥散基组的加号+
        - 保留极化基组的正反括号()，星号*转为下划线\_
        - 去除空格，短横线-，斜线/
  
    用户自定义基组请将.g94格式的基组文件放于ChemiQ安装目录下的\\ChemiQ\\basis文件夹下(默认安装路径为C:\\Users\\YOURUSERNAME\\AppData\\Local\\Programs\\ChemiQ)。
    请务必确保在基组框中输入的基组名称与基组文件一致，否则前端程序将会返回报错：XXX.g94 not exist!

   可选参数：

    - diis(str) : 指定是否使用DIIS(Direct Inversion in the Iterative Subspace,迭代子空间中直接求逆)来加速自洽场迭代[cdiis/None]。
    
    - diis_n(int) : cdiis的历史记录长度，即使用前diis_n个密度矩阵计算下一个密度矩阵。默认值为8。仅当diis=cdiis时有效。
    
    - diis_thre(float) : 当迭代前后两个密度矩阵rmsd小于该阈值时，开始运行cdiis算法。默认值为0.1。仅当diis=cdiis时有效。
  
    - pauli_group(str) : 是否使用泡利分组方法[native/none]。默认为none。泡利分组是一种通过分析哈密顿量子项中的对易关系来减少测量次数从而高效求解哈密顿量期望值的方法。
    
    - pauli_reverse(bool) : 设置比特顺序为正序还是倒序。默认为T，即q3-q2-q1-q0的顺序。

    - bohr(bool) : 坐标单位是否设置为bohr。默认为F，用angstrom为单位。

    - pure(bool) : 使用球谐型还是笛卡尔型Gaussian函数。默认为T, 即使用球谐型Gaussian函数。

    - local(bool) : 是否局域化HF轨道。默认为F, 即不局域化HF轨道。

    - active(int,int) : 设置活性空间，以逗号为分隔符，默认值不设置活性空间。例如active = 4, 4 中第一个4表示4个空间活性轨道，第二个4表示在活性空间中有4个电子。

    - nfrozen(int) : 设置冻结空间轨道数目，默认为0。注：active 与nfrozen不能同时使用。

    - mix_scf(float) : 设置此参数可以有效解决SCF不收敛问题。方法原理为阻尼方法(Damping)。将构建第n+1步Fock矩阵的密度矩阵D(n+1)变为w*D(n-1)+(1-w)*D(n)，此处的w即为设置的参数。参数平均化后的密度矩阵削弱了当前步与上一步密度矩阵之间的差异，使密度矩阵随迭代变化更为平滑，帮助收敛。该参数取值为[0.0, 1.0], 默认为0.5。

3. 拟设参数设置(ansatz settings)
   
   必要参数：

    - ansatz(str) : 设置量子线路拟设类型[UCC/Hardware-efficient/Symmetry-preserved/User-define]。选择前三个类型的拟设，量子线路自动生成，选择最后一种自定义线路拟设需要在参数circuit输入originIR格式的量子线路或者在参数pauli中定义。originIR格式说明详见： `originIR格式介绍 <https://pyqpanda-toturial.readthedocs.io/zh/latest/10.%E9%87%8F%E5%AD%90%E7%BA%BF%E8%B7%AF%E7%BC%96%E8%AF%91/QProgToOriginIR.html>`_ 。

    - mapping(str) : 设置映射[JW/P/BK/SP]。这几种映射方法分别为Jordan-Wigner Transform，Parity Transform, Bravyi-Kitaev Transform, Segment Parity Transform。

    - excited_level(str) : 设置激发水平[S/D/SD]，当ansatz为UCC时为必要参数。

    - circuit(str) : 通过originIR字符串设置量子线路，当ansatz为User-define时为必要参数。

   可选参数：

    - restricted(bool) : 对激发项进行限制，制备更少组态波函数的叠加态以缩短线路。默认为T。仅当ansatz为UCC时生效。

    - cutoff(bool) : 根据MP2的初参对UCC拟设的激发项进行截断。仅当ansatz为UCC且init_para_type=MP2时生效。默认为F。

    - reorder(bool) : 按顺序排列量子比特，前半部分量子比特编码自旋向上，后半部分量子比特编码自旋向下，此参数设置为T时可以减少量子比特的使用。当mapping为P和BK时生效。默认为F。


4. 优化器设置(optimizer settings)

   必要参数：

    - Optimizer(str) : 设置经典优化器类型[Nelder-Mead/Powell/Gradient-Descent/COBYLA/L-BFGS-B/SLSQP/GAQPSO]。

    - init_para_type(str) : 设置构造初始参数的方式[Zero/Random/input/MP2/CCSD]，其中Zero表示初参为全零，Random表示初参为[0,1)区间内的随机数，input表示自定义初参，MP2表示为二阶微扰得到的初参结果，CCSD表示为使用单双激发耦合簇得到的初参结果。其中MP2和CCSD只在拟设为UCCD和UCCSD时可用。初参默认为Zero。

   可选参数：

    - slices(int) : 设置切片数，即量子线路重复次数，默认值1。

    - learning_rate(float) : 设置学习率。默认值0.1。

    - iters(int) : 设置迭代次数，默认值1000。

    - fcalls(int) : 设置函数调用次数，默认值1000。

    - xatol(float) : 设置变量收敛阈值，默认值1e-4。

    - fatol(float) : 设置期望值收敛阈值，默认值1e-4。

5. 分子动力学参数设置(molecular dynamics parameter settings)

   必要参数：

    - MD : 设置关联采样方法。默认为1。

   可选参数：

    - axis(str) : 以字符串形式设置体系沿特定方向运动，格式为"x y z"。

    - save_trajectory(str) : 设置保存分子坐标文件的名称。默认为"traj.csv"。

    - save_topology(str) : 设置保存分子拓扑文件的名称。默认为"topology.txt"。

    - velocity(float) : 设置原子的初始速度，原子间以逗号分隔，"0.1 0.2 0.3, -0.1 -0.2 -0.3\"，单位angstom/fs，默认值全0。

    - step_size(float) : 设置步长，大于0，单位fs，默认0.2。

    - step_number(int) : 设置总步数，大于1，默认100。

    - delta_r(float) : 设置差分坐标大小，大于0，默认0.001。

6. 真实量子芯片模拟(real quantum chip computing settings)

    - chip_mode(str) : 设置芯片任务模式[wait/submit/query/none]。wait表示提交任务并等待返回结果，每两秒钟查询1次，持续一分钟。如果查询不到结果后端会结束查询并返回信息：“当前任务还未结束”。submit表示仅提交任务；query表示仅查询任务，此时需要填写任务id，即chip_task_id。默认为submit。

    - chip_task_id(str) : 提交任务的id号，仅chip_mode = query模式需要。

    - cloud_url(str) : 云平台网址，默认为https://pyqanda-admin.qpanda.cn。

    - cloud_api_key(str) : 云平台api key，可以从 `本源量子云平台 <ttps://console.originqc.com.cn/zh/computerServices/dashboard>`_ 上查看并复制个人的api key。
  
    - shots(int) : 量子线路在真实量子计算机上进行测量的采样次数，采样次数越高，统计误差越小，但计算所需的耗时也越长。默认的采样次数为1000次。
  
    - chip_id(str) : 量子比特芯片编号。默认使用悟空72比特超导芯片，即72。

    - chip_amend(bool) : 指的是测量时是否开启误差修正，修正会让概率结果更精确，默认为True。

    - chip_mapping(bool) : 指的是自动在真实芯片拓扑结构上挑选出符合量子线路结构的量子比特，默认为True。
  
    - chip_circuit_opt(bool) : 线路自动优化是指自动在线路编译时使用算法合并逻辑门，以减少线路深度，默认为True。


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


  第二个示例我们计算氢分子的势能曲线，这里我们以扫描五个点为例，键长从0.6 angstrom开始，每个点间隔0.1 angstrom。基组使用sto-3G，拟设使用自定义线路，映射使用parity，优化器使用SLSQP。初参为零。

.. code-block::

    general = {
        task    = PES
        backend = CPU_SINGLE_THREAD
        license = XXXXX
        PES_atoms = 1,2
        PES_fast_generation = T
        PES_values = 0.6,1,5
    }

    mole = {
        geoms = {
            H 0 0 0
            H 0 0 0.54
        }
        charge  = 0
        spin    = 1 
        basis   = sto-3G
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

  第四个示例我们通过配置文件调用真实芯片来计算氢分子的基态能量。下面license和cloud_api_key关键字需自行填写。

.. code-block::

    general = {
        license = XXXXX
        task = energy {
        chip_mode        = wait 
        cloud_url        = https://pyqanda-admin.qpanda.cn
        cloud_api_key    = XXXXX
        shots            = 1000
        chip_id          = 72
        chip_amend       = T
        chip_mapping     = T
        chip_circuit_opt = T
        }
    }

    mole = {
        geoms = {
            H 0 0 0
            H 0 0 0.74
        }
        charge  = 0
        spin    = 1 
        basis   = sto-3G
    }

    ansatz = Hardware-efficient {
        mapping       = BK
    }

    optimizer = NELDER-MEAD {
        learning_rate                 = 0.1 
        init_para_type                = Random
        slices                        = 1 
        iters                         = 1000 
        fcalls                        = 1000 
        xatol                         = 1e-6 
        fatol                         = 1e-6 
    }

