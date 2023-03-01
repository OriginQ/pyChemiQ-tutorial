拟设教程
=================================

  为了获得与体系量子终态相近的试验波函数，我们需要一个合适的波函数假设，我们称之为拟设(Ansatz)。并且理论上，假设的试验态与理想波函数越接近，越有利于后面得到正确基态能量。实际上，使用VQE算法在量子计算机上模拟分子体系基态问题，最终都是转换到在量子计算机上对态进行演化，制备出最接近真实基态的试验态波函数。最后在对哈密顿量进行测量求得最小期望值，即基态能量。经典的传统计算化学领域已经发展了多种多样的波函数构造方法，比如组态相互作用法(Configuration Interaction, CI) [1]_ , 耦合簇方法(Coupled-Cluster, CC)等 [2]_ 。

  目前，应用在VQE上的主流拟设主要分为两大类，一类化学启发拟设，如酉正耦合簇(Unitary Coupled-Cluster, UCC) [3]_ ，另一类是基于量子计算机硬件特性构造的拟设，即Hardware-Efficient拟设 [4]_ 。
截至现在，pyChemiQ支持的拟设有Unitary Coupled Cluster(UCC)、Hardware-Efficient、Symmetry-Preserved [5]_ 来构造量子电路。

  在基础教程中代码示例中使用的都是UCCSD:

.. code-block::

    from pychemiq.Circuit.Ansatz import UCC
    ansatz = UCC("UCCSD",n_elec,mapping_type,chemiq=chemiq)

下面我们来演示如何使用pyChemiQ调用其他拟设：

.. code-block::

    # 使用UCCS拟设
    from pychemiq.Circuit.Ansatz import UCC
    ansatz = UCC("UCCS",n_elec,mapping_type,chemiq=chemiq)
    # 使用UCCD拟设
    ansatz = UCC("UCCD",n_elec,mapping_type,chemiq=chemiq)

    # 使用HardwareEfficient拟设
    from pychemiq.Circuit.Ansatz import HardwareEfficient
    ansatz = HardwareEfficient(n_elec,chemiq = chemiq)

    # 使用SymmetryPreserved拟设
    from pychemiq.Circuit.Ansatz import SymmetryPreserved
    ansatz = SymmetryPreserved(n_elec,chemiq = chemiq)




















**参考文献**


.. [1]  Peter J Knowles and Nicholas C Handy. A new determinant-based full configuration interaction method. `Chemical physics letters`, 111(4-5):315–321, 1984.
.. [2]  Rodney J Bartlett. Many-body perturbation theory and coupled cluster theory for electron correlation in molecules. `Annual review of physical chemistry`, 32(1):359–401, 1981.
.. [3]  Andrew G Taube and Rodney J Bartlett. New perspectives on unitary coupled-cluster theory. `International journal of quantum chemistry`, 106(15):3393–3401, 2006.
.. [4]  Abhinav Kandala, Antonio Mezzacapo, Kristan Temme, Maika Takita, Markus Brink,Jerry M Chow, and Jay M Gambetta. Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. `Nature`, 549(7671):242–246, 2017.
.. [5]  Bryan T Gard, Linghua Zhu, George S Barron, Nicholas J Mayhall, Sophia E Economou, and Edwin Barnes. Efficient symmetry-preserving state preparation circuits for the variational quantum eigensolver algorithm. `npj Quantum Information`, 6(1):10, 2020.