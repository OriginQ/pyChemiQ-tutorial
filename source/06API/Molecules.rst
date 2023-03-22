:py:class:`pychemiq.Molecules`
==================================

Classes
----------

.. py:class:: Molecules(geometry=None, basis=None, multiplicity=None, charge=0, active=None, nfrozen=None)

   初始化分子的电子结构参数，包括电荷、基组、原子坐标、自旋多重度等

   :param str geometry: 输入分子中原子的类型和坐标。可以为字符串类型或者字符串列表。例如：geometry = "H 0 0 0,H 0 0 0.74" 或者 geometry = ["H 0 0 0","H 0 0 0.74"]
   :param str basis: 输入执行计算的基组水平。目前支持的基组为MINI、sto-3G、sto-6G、3-21G、6-31G等高斯型函数基组。不支持极化与弥散基组。
   :param int multiplicity: 输入分子体系的自旋多重度。与分子总自旋量子数的关系为M=2S+1。目前pyChemiQ只支持RHF单重态计算，UHF以及ROHF正在开发中。
   :param int charge: 输入分子体系的电荷。
   :param list[int] active: 分子体系的活性空间，格式为[m,n]，其中m为活性轨道的数目，n为活性电子的数目。默认不设置活性空间。
   :param int nfrozen: 分子体系的冻结轨道数目，从能量最低的分子轨道算起开始冻结该轨道及轨道上的电子。默认不设置冻结轨道。

   :return: 输出执行HF计算的结果。


   **Attributes**

   .. py:attribute:: n_atoms

      得到分子体系中的原子数

   .. py:attribute:: n_electrons

      得到分子体系中的电子数

   .. py:attribute:: n_orbitals

      得到分子体系的总分子轨道数

   .. py:attribute:: n_qubits

      得到计算所需要的总量子比特数(即自旋轨道数量，2*分子轨道数)

   .. py:attribute:: hf_energy

      得到HF计算的能量(单位:Hartree)

   .. py:attribute:: nuclear_repulsion

      得到分子体系的核间斥力(单位:Hartree)

   .. py:attribute:: canonical_orbitals

      得到分子体系的正则轨道系数(即分子轨道系数)

   .. py:attribute:: orbital_energies

      得到体系每个分子轨道的能量
      
   .. py:attribute:: overlap_integrals

      得到分子体系的重叠积分

   .. py:attribute:: one_body_integrals

      得到分子体系的单电子积分

   .. py:attribute:: two_body_integrals

      得到分子体系的双电子积分


   **Methods**

   .. py:method:: get_molecular_hamiltonian()

      得到初始化后的分子体系的哈密顿量


---------

**接口示例：**

.. code:: 

    from pychemiq import Molecules
    multiplicity = 1
    charge = 0
    basis =  "sto-3g"
    geom = "H 0 0 0,H 0 0 0.74"
    mol = Molecules(
          geometry = geom,
          basis    = basis,
          multiplicity = multiplicity,
          charge = charge)

调用以下接口得到该分子体系的信息：

.. code:: 

    print("The number of atoms is", mol.n_atoms)
    print("The number of electrons is", mol.n_electrons)
    print("The number of orbitals is", mol.n_orbitals)
    print("The number of qubits is", mol.n_qubits)
    print("The Hartree-Fock energy is", mol.hf_energy)
    print("The nuclear repulsion is", mol.nuclear_repulsion)


.. parsed-literal::

    The number of atoms is 2
    The number of electrons is 2
    The number of orbitals is 2
    The number of qubits is 4
    The Hartree-Fock energy is -1.1167593072992057
    The nuclear repulsion is 0.7151043390810812


.. code:: 

    print("The canonical orbitals are\n", mol.canonical_orbitals)
    print("The orbital energies are", mol.orbital_energies)
    print("The overlap integrals are\n", mol.overlap_integrals)


.. parsed-literal::

    The canonical orbitals are
     [[-0.54884228  1.21245192]
     [-0.54884228 -1.21245192]]
     
    The orbital energies are [-0.57855386  0.67114349]

    The overlap integrals are
     [[1.         0.65987312]
     [0.65987312 1.        ]]


.. code:: 

    print("The one body integrals are\n", mol.one_body_integrals)
    print("The two body integrals are\n", mol.two_body_integrals)


.. parsed-literal::

    The one body integrals are
     [[-1.25330979e+00  0.00000000e+00]
     [ 4.16333634e-17 -4.75068849e-01]]

    The two body integrals are
     [[[[ 6.74755927e-01 -1.11022302e-16]
       [-8.32667268e-17  6.63711401e-01]]
    
      [[-3.46944695e-17  1.81210462e-01]
       [ 1.81210462e-01  0.00000000e+00]]]
    
    
     [[[-4.85722573e-17  1.81210462e-01]
       [ 1.81210462e-01 -2.22044605e-16]]
    
      [[ 6.63711401e-01 -2.22044605e-16]
       [-1.66533454e-16  6.97651504e-01]]]]

.. code:: 

    print("The molecular hamiltonian is", mol.get_molecular_hamiltonian())


.. parsed-literal::

    The molecular hamiltonian is {
    : 0.715104
    0+ 0 : -1.253310
    1+ 0+ 1 0 : -0.674756
    1+ 0+ 3 2 : -0.181210
    1+ 1 : -1.253310
    2+ 0+ 2 0 : -0.482501
    2+ 1+ 2 1 : -0.663711
    2+ 1+ 3 0 : 0.181210
    2+ 2 : -0.475069
    3+ 0+ 2 1 : 0.181210
    3+ 0+ 3 0 : -0.663711
    3+ 1+ 3 1 : -0.482501
    3+ 2+ 1 0 : -0.181210
    3+ 2+ 3 2 : -0.697652
    3+ 3 : -0.475069
    }
    