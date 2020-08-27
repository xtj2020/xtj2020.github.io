# torch

## 张量

### 属性列表

is_tensor				

is_storage				

is_complex				

is_floating_point				

is_nonzero				

set_default_dtype				

get_default_dtype				

set_default_tensor_type				

numel				

set_printoptions				

set_flush_denormal

### 创建方法

tensor				

sparse_coo_tensor				

as_tensor				

as_strided				

from_numpy				

zeros				

zeros_like				

ones				

ones_like				

arange				

range				

linspace				

logspace				

eye				

empty				

empty_like				

empty_strided				

full				

full_like				

quantize_per_tensor				

quantize_per_channel				

dequantize					

### 切片、索引

cat按指定维度进行堆叠

```
cat(seq,dim=0,out=None)
```

​				

chunk				

gather				

index_select				

masked_select				

narrow				

nonzero				

reshape				

split				

squeeze				

stack				

t				

take				

transpose				

unbind				

unsqueeze				

where				

## 生成器

## 随机化

### 属性

seed				

manual_seed				

initial_seed				

get_rng_state				

set_rng_state

### 随机化

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

### 内建随机化

torch.Tensor.bernoulli_() - in-place version of torch.bernoulli()

torch.Tensor.cauchy_() - numbers drawn from the Cauchy distribution

torch.Tensor.exponential_() - numbers drawn from the exponential distribution

torch.Tensor.geometric_() - elements drawn from the geometric distribution

torch.Tensor.log_normal_() - samples from the log-normal distribution

torch.Tensor.normal_() - in-place version of torch.normal()

torch.Tensor.random_() - numbers sampled from the discrete uniform distribution

torch.Tensor.uniform_() - numbers sampled from the continuous uniform distribution							

## 序列化

pytorch数据保存与加载

save

```
x = torch.tensor([0,1,2,3,4])
torch.save(x,'tensor.pt')
```

load

可以指定映射空间

## 局部禁用梯度计算

no_grad

enable_grad

set_grad_enable

## 数学运算

### 点运算

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

### 缩小运算

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

### 比较运算

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

### 线性代数

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

### 特殊变换

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

### 其它

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