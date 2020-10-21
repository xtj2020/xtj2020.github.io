# 基础与常用库

## torch

包含多维张量的数据结构

### Tensors

#### 属性列表

is_tensor				is_storage				is_complex				is_floating_point				

is_nonzero				set_default_dtype				get_default_dtype				set_default_tensor_type				

numel				set_printoptions				set_flush_denormal

#### 创建方法

tensor				sparse_coo_tensor				as_tensor				as_strided				from_numpy				

zeros				zeros_like				ones				ones_like				arange				

range				linspace				logspace				eye				empty				

empty_like				empty_strided				full				full_like				quantize_per_tensor				

quantize_per_channel				dequantize					

#### 切片、索引

cat按指定维度进行堆叠

```
cat(seq,dim=0,out=None)
```

​				

chunk				gather				

index_select				masked_select				

narrow				nonzero				

reshape				split				squeeze		压缩，去掉维数为一的维度		

stack				t				take				transpose				unbind				unsqueeze				where				

### 生成器

### 随机取样

#### 属性

seed				

manual_seed				

initial_seed				

get_rng_state				

set_rng_state

#### 随机化

bernoulli	伯努利分布			

multinomial				

normal				

poisson				

rand				

rand_like				

randint				

randint_like				

randn				

randn_like				

randperm	

#### 内建随机化

torch.Tensor.bernoulli_() - in-place version of torch.bernoulli()

torch.Tensor.cauchy_() - numbers drawn from the Cauchy distribution

torch.Tensor.exponential_() - numbers drawn from the exponential distribution

torch.Tensor.geometric_() - elements drawn from the geometric distribution

torch.Tensor.log_normal_() - samples from the log-normal distribution

torch.Tensor.normal_() - in-place version of torch.normal()

torch.Tensor.random_() - numbers sampled from the discrete uniform distribution

torch.Tensor.uniform_() - numbers sampled from the continuous uniform distribution							

### 序列化

pytorch数据保存与加载

save

```
x = torch.tensor([0,1,2,3,4])
torch.save(x,'tensor.pt')
```

load

可以指定映射空间

### 局部禁用梯度计算

no_grad

enable_grad

set_grad_enable

### 数学运算

#### 点运算

abs

absolute

acos

acosh

add

addcdiv

addcmul

angle

asin

asinh

atan

atn2

btwise_not

bitwise_and

bitwise_or

bitwise_xor

ceil

clamp

conj

cos

cosh

deg2rad

div

digamma

erf

erfc

erfinv

exp

expm1

floor

floor_divide

fmod

frac

imag

lerp

lgamma

log

log10

log1p

log2

logaddexp

logaddexp2

logical_and

logical_not

logical_or

logical_xor

mul

mvlgamma

neg

polygamma

th

pow

rad2deg

real

reciprocal

remainder

round

rsqrt

sigmoid

sign

sin

sinh

sqrt

square

tan

tanh

true_divide

trunc

#### 缩小运算

argmax

argmin

dist

logsumexp

mean

median

mode

norm

prod

std

std_mean

sum

unique

unique_consecutive

var

var_mean

#### 比较运算

allclose

argsort

eq

equal

ge

gt

isclose

isfinite

isinf

isnan

kthvalue

le

lt

max

min

ne

sort

topk

#### 线性代数

addbmm

addmm

addmv

addr

baddbmm

bmm

chain_matmul

cholesky

cholesky_inverse

cholesky_solve

dot

eig

geqrf

ger

inverse

det

logdet

slogdet

lstsq

lu

lu_solve

lu_unpack

matmul

matrix_power

matrix_rank

mm

mv

orgqr

ormqr

pinverse

qr

solve

svd

T

svd_lowrank

pca_lowrank

symeig

lobpcg

trapz

triangular_solve

#### 特殊变换

fft

ifft

rfft

irfft

stft

istft

bartlett_window

blackman_window

hamming_window

hann_window

### 高级功能

bincount

block_diag

broadcast_tensors

bucketize

cartesian_prod

cdist

combinations

cross

cummax

cummin

cumprod

cumsum

diag

diag_embed

diagflat

diagonal

einsum

flatten

flip

fliplr

flipud

rot90

histc

meshgrid

logcumsumexp

renorm

repeat_interleave

roll

searchsorted

tensordot

trace

tril

tril_indices

triu

triu_indices

vander

view_as_real

view_as_complex

## torch.nn

### 容器

#### Module模块

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

#### Sequential

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

### 卷积层

​	•	nn.Conv1d

​	•	nn.Conv2d

​	•	nn.Conv3d

​	•	nn.ConvTranspose1d

​	•	nn.ConvTranspose2d

​	•	nn.ConvTranspose3d

​	•	nn.Unfold

​	•	nn.Fold

### 池化层

### Padding Layers填充层

### Non-linear Activations (weighted sum, nonlinearity)

### Non-linear Activations (other)

### Normalization Layers

### Recurrent Layers

### Transformer Layers

### Linear Layers

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

### Distance Functions

### 损失函数

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

### Vision Layers上采样层

​	•	nn.PixelShuffle

​	•	nn.Sample

​	•	nn.UpsamplingNearest2d

​	•	nn.UpsamplingBilinear2d

### DataParallel Layers (multi-GPU, distributed)

​	•	nn.DataParallel

​	•	nn.parallel.DistributedDataParallel

### Utilities

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

##### 量化函数

​	量化是指用于执行计算并以低于浮点精度的位宽存储张量的技术。 PyTorch支持每个张量和每个通道非对称线性量化。要了解更多如何在PyTorch中使用量化函数的信息，请参阅量化文档. 

​	量化是指用于执行计算并以低于浮点精度的位宽存储张量的技术。 PyTorch支持每个张量和每个通道非对称线性量化。要了解更多如何在PyTorch中使用量化函数的信息，请参阅量化文档.  

## Torch.nn.functional

torch.nn定义的是一个类，可以提取变化的学习参数
torch.nn.function定义的是一个函数，是一个固定的运算公式。



### 卷积函数

### 池化函数

adaptive_avg_pool2d(自适应平均池化函数)
会改变大小，而不会改变通道数。输入要素等于输出要素。
参数output为元组，为单个整数的话为H*H，为None的话与输入保持一致

### 非线性激活函数

### 正则函数

### 线性函数

### Dropout函数

### 距离函数

### 损失函数

### 并行函数



## Torch.tensor

多维矩阵，单个数据类型的元素。

### 类型

具有十种类型

## Tensor Attributes

每个torch.Tensor有torch.dtype,torch.device,torch.layout

## Tensor Views

# 后端、硬件、并行计算

## Torch.cuda

对CUDA张量类型的支持，利用GPU计算

## torch.cuda.amp

## torch.distributed

## torch.futures

## Distributed RPC Framework

# 脚本与预处理

## torch.hub

预处理模型资料库

## torch.jit

TorchScript脚本

# 某些功能的实现

## torch.distributions

## torch.autograd

## torch.nn.init

## torch.onnx

## torch.optim

### 构建

实现各种优化算法的包，必须先构造出一个优化器，保持当前状态并根据计算出来的梯度不断更新参数。给它一个包含参数（Variable）的可迭代的对象

注意事项：1、通过.cuda()使用gpu，在构建优化器之前使用。因为参数会发生变化 2、在构造和使用优化器时，保证参数处于一致的位置

### 为每个参数设立值

用一个字典的类型的可迭代参数代替变量可迭代参数，用‘parameters’将其独立开来
在需要不同层不同参数时十分有效

### 迭代

第一种 optimizer.step()

第二种 optimizer.step(clouse) 适用于多次评估函数的算法，传入一个运行重新计算模型的闭包，来清理梯度，计算Loss并返回

### 基类

## Complex Numbers

对复数功能的实现

## Quantization（beta）

执行计算并以低于浮点精读的位宽存储张量的技术

## torch.random

## torch.sparse

稀疏张量

## Torch.storeage

单个数据类型的连续一维数组
每个torch.Tensor对象都具有相同数据类型的对应存储:class torch.FloatStorage

bfloat16()

bool()

byte()

char()

clone()

complex_double()

complex_float()

copy_()

cpu()

cuda(device=None, non_blocking=False, **kwargs)

data_ptr()

device

double()

dtype

element_size()

fill_()

float()

Casts this storage to float type

STATIC from_buffer()

STATIC from_file(filename, shared=False, size=0) → Storage

half()

int()

is_pinned()

is_shared()

long()

new()

pin_memory()

resize_()

share_memory_()

short()

tolist()

type(dtype=None, non_blocking=False, **kwargs)

# 单元

## torch.utils.bottleneck

## torch.utils.checkpoint

## torch.utils.cpp_extension

## torch.utils.data

### 数据类型

### 加载数据与数据样本

### 多线程数据加载

### 存储分配

## torch.utils.dlpack

## torch.utils.mobile_optimizer

## torch.utils.model_zoo

## torch.utils.tensorboard

# 信息与命名

## Type Info

## Named Tensors

## Named Tensors operator coverage

