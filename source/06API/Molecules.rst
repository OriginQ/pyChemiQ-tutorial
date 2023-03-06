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


