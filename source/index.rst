.. pychemiq documentation master file, created by
   sphinx-quickstart on Mon Nov 14 14:20:39 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyChemiQ
====================================
  pyChemiQ是一款由本源量子开发的python软件库, 旨在实现费米子模型的模拟以及量子硬件上或虚拟机的量子化学问题。该软件包为量子化学计算和方法开发提供了一个简单、轻量级且高效的平台。 pyChemiQ 可用于在量子计算机上使用平均场和后平均场方法模拟分子来解决量子化学问题。 pyChemiQ简化了分子结构输入和量子电路之间的转换，最大限度地减少了进入该领域所需的领域专业知识，让感兴趣的学者更方便解决和研究量子计算机上的电子结构问题。

  目前，pyChemiQ支持输入分子结构得到二次量子化后的Fermion Hamiltonian；映射方面，pyChemiQ支持Jordan-Wigner(JW)变换、Bravyi-Kitaev(BK)变换、Parity变换和Multilayer Segmented Parity(MSP)变换方法将二次量子化的Fermion Hamiltonian算符映射成量子计算机上的pauli Hamiltonian算符；拟设方面，pyChemiQ也支持不同的拟设构造量子电路，例如Unitary Coupled Cluster（UCC）、Hardware-Efficient、symmetry-preserved等拟设构造量子电路；优化器方面，pyChemiQ提供了以下几种经典优化器来进行变分参数的优化：NELDER-MEAD、POWELL、COBYLA、L-BFGS-B、SLSQP和Gradient-Descent。通过自定义映射和拟设方式，用户也可以自行构造或优化量子线路，求得电子结构问题的最优基态能量解。

- Github网站链接
- 为特定量子化学问题定制pyChemiQ功能，请联系本源量子陈先生18221003869或给我们发送邮件 dqa@originqc.com。
- 体验全部最新功能的可视化教学工具ChemiQ，请前往 `官网 <https://qcloud.originqc.com.cn/zh/chemistryIntroduce>`_ 下载。
- 若您想在文献中引用pyChemiQ或ChemiQ, 请按照如下格式: Wang Q, Liu H Y, Li Q S, et al. Chemiq: A chemistry simulator for quantum computer[J]. arXiv preprint arXiv:2106.10162, 2021. 




.. toctree::
   :maxdepth: 2
   :caption: pyChemiQ安装
   
   01install/install.rst


.. toctree::
   :maxdepth: 2
   :caption: 快速入门
   
   02start/quickstart.rst


.. toctree::
   :maxdepth: 2
   :caption: 基础教程
   
   03basis/hamiltonian.rst
   03basis/mapping.rst
   03basis/ansatz.rst
   03basis/algorithm.rst
   03basis/function.rst

.. toctree::
   :maxdepth: 2
   :caption: 进阶教程
   
   04advanced/fermionpauliop.rst
   04advanced/optimizer.rst

.. toctree::
   :maxdepth: 2
   :caption: 理论背景
   
   05theory/computationalchemistry.rst
   05theory/theoreticalbackground.rst
   05theory/vqeintroduction.rst

.. toctree::
   :maxdepth: 2
   :caption: API

   06API/index


.. toctree::
   :maxdepth: 2
   :caption: 交流与反馈
   
   07FAQ/feedback.rst
   
