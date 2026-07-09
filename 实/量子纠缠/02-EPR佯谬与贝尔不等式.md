# EPR 佯谬与贝尔不等式

## EPR 佯谬（1935）

1935 年，**爱因斯坦**（Albert Einstein）、**波多尔斯基**（Boris Podolsky）和**罗森**（Nathan Rosen）在 *Physical Review* 上发表了一篇划时代论文，题为：

> "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?"

这篇论文的核心论点是：**量子力学是不完备的**，必定存在"隐变量"来解释纠缠粒子之间的关联。

### 爱因斯坦的逻辑

爱因斯坦的推理基于两个基本假设：

1. **定域性**（Locality）：一个地方发生的事件不能瞬间影响远处的事件（光速极限）
2. **实在性**（Realism）：物理量在被测量之前就具有确定的值

如果一个粒子 A 和粒子 B 处于纠缠态，测量 A 的自旋立刻就知道 B 的自旋——即使 B 在光年之外。爱因斯坦认为：

- 要么信息超光速传递（违反相对论）→ 不可能
- 要么 B 的自旋在测量之前就已经确定了 → 存在**隐变量**

爱因斯坦将纠缠称为"**鬼魅般的超距作用**"（spukhafte Fernwirkung / spooky action at a distance），认为这暴露了量子力学的缺陷。

### EPR 论文的结论

EPR 论文认为量子力学只是对更深层确定性理论的**统计近似**，就像热力学是分子运动的统计近似一样。一定存在**隐变量**（Hidden Variables）——粒子携带着某种"指令集"，预先规定了在不同测量条件下的行为。

## 玻尔的回应

**尼尔斯·玻尔**（Niels Bohr）同年发表了回应文章，维护了量子力学的完备性。他的核心观点是：

- 纠缠粒子构成一个**不可分割的整体**，不能将它们视为独立的个体
- 测量本身是实验装置与量子系统的相互作用，不是简单地"揭示"预存的属性
- "实在性"的定义取决于实验语境——在量子层面，不存在独立于测量的"客观现实"

玻尔的观点被称为**哥本哈根诠释**（Copenhagen Interpretation），但在 EPR 问题上，爱因斯坦的质疑在逻辑上是成立的——双方都无法用实验来区分"不完备的量子力学+隐变量"和"完备的量子力学+非定域性"。

这个僵局持续了近 30 年。

## 贝尔不等式（1964）

### 约翰·贝尔的突破

1964 年，北爱尔兰物理学家**约翰·斯图尔特·贝尔**（John Stewart Bell）发表了一篇改变物理学走向的论文：

> "On the Einstein Podolsky Rosen Paradox"

贝尔的伟大贡献在于：**他将一个哲学争论转化为了一个可实验验证的数学不等式**。

### 贝尔不等式的内容

贝尔证明：如果爱因斯坦是对的（存在局域隐变量），那么对大量纠缠粒子对的测量结果之间的**关联度**（correlation）永远不会超过一个特定的上限。

用数学语言表达：对于任何**局域隐变量理论**（Local Hidden Variable Theory），以下不等式必须成立：

```
|S| ≤ 2

其中 S = E(a,b) - E(a,b') + E(a',b) + E(a',b')

E(a,b) = 在测量方向 a 和 b 上的关联函数
a, a' = Alice 的两个测量方向
b, b' = Bob 的两个测量方向
```

这就是**贝尔不等式**（Bell Inequality），也称 **CHSH 不等式**（Clauser-Horne-Shimony-Holt，1969 年的推广版本）。

### 量子力学的预测

量子力学预测，对于特定的测量角度选择，关联值 S 可以达到：

```
|S| = 2√2 ≈ 2.828
```

这**明显超过了**经典隐变量理论的上限 2。

### 贝尔不等式的意义

| 假设 | S 值上限 | 含义 |
|------|---------|------|
| 局域隐变量理论（爱因斯坦） | ≤ 2 | 粒子携带预设指令，无超距作用 |
| 量子力学（玻尔） | ≤ 2√2 ≈ 2.828 | 纠缠是真实的非定域关联 |

贝尔不等式第一次使得"爱因斯坦 vs 玻尔"的争论可以通过实验裁决：

- 如果实验测得 |S| ≤ 2 → 爱因斯坦赢，需要隐变量理论
- 如果实验测得 |S| > 2 → 玻尔赢，量子力学正确，纠缠是真实的非定域现象

## Bell 定理的深远影响

贝尔定理（Bell's Theorem）可以表述为：

> **任何与量子力学预测一致的物理理论，都不可能是局域实在论的。**

也就是说，你必须至少放弃以下两个信念之一：

1. **定域性** — 放弃"没有超光速影响"
2. **实在性** — 放弃"物理量在测量前有确定值"

量子力学选择了放弃（2），保留了"无超光速信号传递"（虽然纠缠看起来超距，但不能用来传递信息——这被称为**无信号定理**）。

## 贝尔的遗产

约翰·贝尔于 1990 年去世，未能亲眼看到 2022 年诺贝尔奖颁发给验证其不等式的三位实验物理学家。但他的贡献被公认为 20 世纪物理学最重要的理论成果之一：

- 他将形而上学的哲学争论变成了可实验的数学命题
- 他证明了量子力学的非定域性是**可检验的**
- 他奠定了整个量子信息科学的理论基础

正如诺贝尔委员会所说：

> "John Stewart Bell developed the mathematical inequality that is named after him. This states that if there are hidden variables, the correlation between the results of a large number of measurements will never exceed a certain value."

## 参考来源

- Bell, J.S. (1964). On the Einstein Podolsky Rosen paradox. *Physics*, 1, 195–200.
- Einstein, A., Podolsky, B. & Rosen, N. (1935). Can quantum-mechanical description of physical reality be considered complete? *Physical Review*, 47, 777–780.
- Clauser, J.F. et al. (1969). Proposed experiment to test local hidden-variable theories. *Physical Review Letters*, 23, 880–884.
- Nobel Prize: [Press Release — The Nobel Prize in Physics 2022](https://www.nobelprize.org/prizes/physics/2022/press-release/)
