# torch.nn

## 容器

### Module模块

模型是类Model的实例化，而Mode继承于nn.Modole

```python
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
# 层的定义

    def forward(self, x):
#前向传递的定义
```

add_module( name,module)
apply(*fn*)
bfloat16()
buffers(*recurse=True*)

eval() 变为评估模式等价于self.train(False)

### Sequential

也是容器的一种，更加结构化

两种表达方式：

```python
model = nn.Sequential(
                  nn.Conv2d(1,20,5),
                  nn.ReLU(),
                  nn.Conv2d(20,64,5),
                  nn.ReLU()
                )
#通过字典的方法
model = nn.Sequential(OrderedDict([
                  ('conv1', nn.Conv2d(1,20,5)),
                  ('relu1', nn.ReLU()),
                  ('conv2', nn.Conv2d(20,64,5)),
                  ('relu2', nn.ReLU())
                ]))


```

​	•	ModuleList

​	•	ModuleDict

​	•	ParameterList

​	•	ParameterdDict

## 卷积层

​	•	nn.Conv1d

​	•	nn.Conv2d

​	•	nn.Conv3d

​	•	nn.ConvTranspose1d

​	•	nn.ConvTranspose2d

​	•	nn.ConvTranspose3d

​	•	nn.Unfold

​	•	nn.Fold

## 池化层

## Padding Layers填充层

## Non-linear Activations (weighted sum, nonlinearity)

## Non-linear Activations (other)

## Normalization Layers

## Recurrent Layers

## Transformer Layers

## Linear Layers

### Dropout层

•	nn.Dropout

​	在训练期间，使用伯努利分布的样本以概率p将输入张量的某些元素随机置零。

•	nn.Dropout2d

​	将整个通道随机置零

•	nn.Dropout3d

•	nn.AlphaDropout

▾	Sparse Layers

​	•	nn.Embedding

​	•	nn.EmbeddingBag

### 稀疏层（sparse Layers）

​	•	nn.Embedding

​	•	nn.EmbeddingBag

## Distance Functions

## 损失函数

​	•	nn.L1Loss

​	•	nn.MSELoss

​	•	nn.CrossEntropyLoss

​	•	nn.CTCLoss

​	•	nn,NLLLoss

​	•	nn.PoissonNLLoss

​	•	nn.KLDivLoss

​	•	nn.BCELoss

​	•	nn.BCEwithLogitisLoss

​	•	nn.MarginRankingLoss

​	•	nn.HingeEmbeddingLoss

​	•	nn.MultilLabelMarginLoss

​	•	nn.Smooth1Loss

​	•	nn.SotMarginLoss

​	•	nn.MultiLabelSoftMarginLoss

​	•	nn.CosineEmbeddingLoss

​	•	nn.TripleMarginLoss

​	•	nn.TripletMarginLoss

## Vision Layers上采样层

​	•	nn.PixelShuffle

​	•	nn.Sample

​	•	nn.UpsamplingNearest2d

​	•	nn.UpsamplingBilinear2d

## DataParallel Layers (multi-GPU, distributed)

​	•	nn.DataParallel

​	•	nn.parallel.DistributedDataParallel

## Utilities

​	•	From the torch.nn.utils module

​	•	clip_grad_norm_

​	•	Clips gradient norm of an iterable of parameters.

​	•	clip_grad_value_

​	•	Clips gradient of an iterable of parameters at specified value.

​	•	parameters_to_vector

​	•	Convert parameters to one vector

​	•	vector_to_parameters

​	•	Convert one vector to the parameters

​	•	prune.BasePruningMethod

​	•	Abstract base class for creation of new pruning techniques.

​	•	prune.PruningContainer

​	•	Container holding a sequence of pruning methods for iterative pruning.

​	•	prune.Identity

​	•	Utility pruning method that does not prune any units but generates the pruning parametrization with a mask of ones.

​	•	prune.RandomUnstructured

​	•	Prune (currently unpruned) units in a tensor at random.

​	•	prune.L1Unstructured

​	•	Prune (currently unpruned) units in a tensor by zeroing out the ones with the lowest L1-norm.

​	•	prune.RandomStructured

​	•	Prune entire (currently unpruned) channels in a tensor at random.

​	•	prune.LnStructured

​	•	Prune entire (currently unpruned) channels in a tensor based on their Ln-norm.

​	•	prune.CustomFromMask

​	•	prune.identity

​	•	Applies pruning reparametrization to the tensor corresponding to the parameter called name in module without actually pruning any units.

​	•	prune.random_unstructured

​	•	Prunes tensor corresponding to parameter called name in module by removing the specified amount of (currently unpruned) units selected at random.

​	•	prune.l1_unstructured

​	•	Prunes tensor corresponding to parameter called name in module by removing the specified amount of (currently unpruned) units with the lowest L1-norm.

​	•	prune.random_structured

​	•	Prunes tensor corresponding to parameter called name in module by removing the specified amount of (currently unpruned) channels along the specified dim selected at random.

​	•	prune.ln_structured

​	•	Prunes tensor corresponding to parameter called name in module by removing the specified amount of (currently unpruned) channels along the specified dim with the lowest L``n``-norm.

​	•	prune.global_unstructured

​	•	Globally prunes tensors corresponding to all parameters in parameters by applying the specified pruning_method.

​	•	prune.custom_from_mask

​	•	Prunes tensor corresponding to parameter called name in module by applying the pre-computed mask in mask.

​	•	prune.remove

​	•	Removes the pruning reparameterization from a module and the pruning method from the forward hook.

​	•	prune.is_pruned

​	•	Check whether module is pruned by looking for forward_pre_hooks in its modules that inherit from the BasePruningMethod.

​	•	weight_norm

​	•	Applies weight normalization to a parameter in the given module.

​	•	remove_weight_norm

​	•	Removes the weight normalization reparameterization from a module.

​	•	spectral_norm

​	•	Applies spectral normalization to a parameter in the given module.

​	•	remove_spectral_norm

​	•	Removes the spectral normalization reparameterization from a module.

​	•	Utility functions in other modules

​	•	nn.utils.rnn.PackedSequence

​	•	Holds the data and list of batch_sizes of a packed sequence.

​	•	nn.utils.rnn.pack_padded_sequence

​	•	Packs a Tensor containing padded sequences of variable length.

​	•	nn.utils.rnn.pad_packed_sequence

​	•	Pads a packed batch of variable length sequences.

​	•	nn.utils.rnn.pad_sequence

​	•	Pad a list of variable length Tensors with padding_value

​	•	nn.utils.rnn.pack_sequence

​	•	Packs a list of variable length Tensors

​	•	nn.Flatten

​	•	Flattens a contiguous range of dims into a tensor.

## 量化函数

​	量化是指用于执行计算并以低于浮点精度的位宽存储张量的技术。 PyTorch支持每个张量和每个通道非对称线性量化。要了解更多如何在PyTorch中使用量化函数的信息，请参阅量化文档. 

​	量化是指用于执行计算并以低于浮点精度的位宽存储张量的技术。 PyTorch支持每个张量和每个通道非对称线性量化。要了解更多如何在PyTorch中使用量化函数的信息，请参阅量化文档.  