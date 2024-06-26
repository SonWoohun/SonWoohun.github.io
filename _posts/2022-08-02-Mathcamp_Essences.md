---
layout: post
title: Mathcamp Essences in OSU (in progress)
tags: [Math, Economics]
usemathjax: true
---

Here, I will list up important definitions and theorems that must be remembered, and objects or properties that was hard for me to understand. So, the materials covered in this page may be rather subjective and does not follow the materials of the mathcamp in OSU as a whole. I will add subjects that is from other texts such as "Mathematics for Economists" (Simon & Blume) or "Principles of Mathematical Analysis" (Walter Rudin). Moreover, to modify the definitions and theorems to be easily remembered, I will actively use abbreviation of notations.

# Set and Logic

- Even subsets are defined in elements.

$$Definition1\: (subset) \: A: \text{subset of }X \text{ if } ∀x∈A,\:x∈X.$$

- Thus we can say that two sets are equal if all the elements of the two coincides.

$$Definition2\: A=B⇔A⊆B\&B⊆A\text{, i.e., }\forall x\in A, \:x\in B\: \& \:\forall y\in B,\: y\in A.$$


$$Definition3\: (power set)\:P\left(X\right) \text{(the power set of }X):=\{A_{i}:A_{i}\subseteq X\}$$

- Then, the number of elements--the power set has sets as elements--in the power set of $$X$$: $$n\left(P\left(X\right)\right)=2^{n\left(X\right)}$$, since it is the same as the number of cases of checking whether each element in $$X$$ is present or not.
- Also, from the reasoning above, we can see that empty set is also an element of the power set, as no elements being present is contained in the cases.

$$Definition4\: (union)\: A\cup B:=\{x\in A\:\text{ or }x\in B\}$$

$$Definition5\: (intersection)\: A\cap B:=\{x\in A\:\text{ and }x\in B\}$$

- It is important to note that $$A\subseteq E$$ or $$A\subseteq E'$$, then $$A\subseteq E\cup E'$$ but not the converse.

- However, $$A\subseteq E$$ and $$A\subseteq E'$$ $$⇔$$ $$A\subseteq E\cap E'$$.

$$Theorem1\: (Commutative,\: Associative,\: Distributive\:Law)\:$$

(1) Commutative Law: $$A\cup B=B\cup A$$ and $$A\cap B=B\cap A$$

(2) Associative Law: 

$$(A\cup B)\cup C=A\cup(B\cup C)=A\cup B\cup C$$

$$(A\cap B)\cap C=A\cap(B\cap C)=A\cap B\cap C$$

(3) Distributive Law:

$$(A\cup B)\cap C=(A\cap C)\cup(B\cap C)$$

$$(A\cap B)\cup C=(A\cup C)\cap(B\cup C)$$

$$Definition6\: (disjoint)\:$$ $$A$$ and $$B$$ are disjoint if $$A\cap B=\phi.$$

$$Definition7\: (pairwise\: disjoint)$$
A family of sets, $$\{A_{i},\:i=1,\dots,n\}$$, is pairwise disjoint if $$\forall i\neq j, \:i,j=1,\dots,n,\: A_{i}\cap A_{j}=\phi.$$

- Pairwise disjoint means a class of sets does not overlap each other.
- From now on, I will use $$i\in I$$, instead of using $$i=1,\dots,n$$.

$$Definition8\: (partition)$$
A family of sets $$\{A_{i}\subseteq X,\:i\in I\}$$, is a partition of $$A$$ if $$\forall i\neq j\in I,\:A_{i}\cap A_{j}=\phi\:\&\:\cup_{i\in I}A_{i}=X.$$

- So, a partition of a set is a class of sets that constitute the set but does not overlap each other.

$$Definition9\:(Complement\:of\:A\:relative\:to\:X)$$
$$A^{c}:=\{x∈X:x∉A\}$$

$$Theorem2\:(De \:Morgan's\:Laws)$$

1. $$(∪_{i∈I}A_{i})^{c}=∩_{i∈I}A_{i}^{c}$$

2. $$(∩_{i∈I}A_{i})^{c}=∪_{i∈I}A_{i}^{c}$$

$$proof$$
1. $$x∈(∪_{i∈I}A_{i})^{c}⇔x∉∪_{i∈I}A_{i}⇔∄i∈I\:s.t.\:x∈A_{i}$$
$$⇔∀i∈I,\:x∉A_{i}⇔∀i∈I,\:x∈A_{i}^{c}⇔x∈∩_{i∈I}A_{i}^{c}.∎$$

2. $$x∈(∩_{i∈I}A_{i})^{c}⇔x∉∩_{i∈I}A_{i}⇔∃i∈I\:s.t.\:x∉A_{i}$$
$$⇔∃i∈I\:s.t.\:x∈A_{i}^{c}⇔x∈∪_{i∈I}A_{i}^{c}.∎$$

$$Theorem3\:∀A,B⊂X,\:A⊂B⇔A^{c}∪B=X$$

$$proof$$
$$(\lvert⇒)\:A⊂B⇒A∩B=B⇒A^{c}∪B^{c}=A^{c}\:(∵ De\:Morgan's\:Laws)$$ 
then 
$$A^{c}∪B=(A^{c}∪B^{c})∪B=A^{c}∪(B^{c}∪B)=A^{c}∪X=X\:(∵associative).∎$$
$$(⇐\rvert)\:A^{c}∪B=X⇒(A^{c}∪B)∩B^{c}=(A^{c}∩B^{c})∪(B∩B^{c})=B^{c}$$
$$⇒A^{c}∩B^{c}=B^{c}⇒A∪B=B\:(∵De\:Morgan's\:Laws)⇒A⊂B.∎$$

### Mathematical Induction

$$Theorem4$$

$$P :$$ A property that $$\mathbb{N}\:(or\:\mathbb{Z}_{+})$$ may or may not have.

If (i) $$∃n_{0}∈\mathbb{N}\:(or\:\mathbb{Z}_{+})$$ $$s.t.\:P(n_{0})$$ holds and (ii) $$∀n∈\mathbb{N}\:(or\:\mathbb{Z}_{+})$$, $$P(n)⇒P(n+1)$$, then $$P$$ holds for $$∀n∈\mathbb{N}\:(or\:\mathbb{Z}_{+})$$ $$s.t.\:n≥n_{0}$$.

### Rudin, PMA part

(p.9)

$$Theorem5\:(Archimedian\:property,\:Density\:of\:\mathbb{Q})$$

(a) $$x,y∈\mathbb{R},\:and\:x>0⇒∃n∈\mathbb{Z}_{+}\:s.t.\:nx>y$$.
(b) $$x,y∈\mathbb{R},\:and\:x<y⇒∃p∈\mathbb{Q}\:s.t.\:x<p<y$$.

$$proof$$ (skip (a))

(b) $$x<y⇒y-x>0$$. Then by (a), $$∃n∈\mathbb{Z}_{+}\:s.t.\:n(y-x)>1.$$

Again by (a), $$∃m_{1},m_{2}∈\mathbb{Z}_{+}\:s.t.\:m_{1}×1>nx\:\&\:m_{2}×1>-nx.$$

Then, $$-m_{2}<nx<m_{1}.$$

This means $$∃m∈\mathbb{Z}_{+}\:s.t.\:-m_{2}≤m≤m_{1}\:\&\:m-1≤nx≤m.$$

Thus, $$nx<m≤1+nx<ny.$$ Since, $$n>0,\:x<\frac{m}{n}<y. ∎$$


# Relation and Function

$$Definition1\:(Cartesian\:product)$$ $$X×Y:=\{(x,y):x∈X\:\&\:y∈Y\}$$

$$Definition2\:(Binary\:Relation\:from\:X\:to\:Y)$$ : $$R⊂X×Y$$

- If $$R⊂X×X$$, we say $$R$$ is relation defined on $$X$$.
- If $$(x,y)∈R⇔y∈R(x)$$, $$y$$ is the **image** of $$x$$, and $$R(x):={y∈Y:(x,y)∈R}$$ : **image set**

$$Definition3\:(Inverse\:relation)$$ : $$R^{-1}:=\{(y,x)∈Y×X:(x,y)∈R\}$$

- Note that inverse relation still depends on R.

$$Definition4\:(Image\: set \:of\: a\: set)$$ $$R⊂X×Y,\:A⊂X$$. The $$R(A):=\{y∈Y : ∃x∈A\:s.t.\:(x,y)∈R\}$$

- From the $$Def4$$, $$R(A)=∪_{x∈A}R(x).$$ Note that $$R(x)$$ may not be singleton.

$$Definition5\:(Inverse\:image\:set\:of\:a\:set)$$ $$R⊂X×Y,\:B⊂Y.\:R^{-1}(B):={x∈X:∃y∈B\:s.t.\:(x,y)∈R}$$

- Similarly, $$R(B)=∪_{y∈B}R^{-1}(y).$$

$$Definition6\:(Domain)\:D_{R}:=R^{-1}(Y)={x∈X:R(x)≠ϕ}$$

- In words, the set of points in $$X\:s.t.$$ each point has at least one image in $$Y$$.

$$Definition7\:(Range)\:R_{R}:=R(X)={y∈Y:R^{-1}(Y)≠ϕ}$$

![](/assets/img/domain_and_range1024_1.jpg)

$$Definition8\:(Sub-relation\:or\:restriction)\:R,S⊂X×Y. S⊂R⇒S: $$ sub-relation, or restriction of $$R$$

- At the same time, $$R$$ is an extension of $$S$$.

$$Definition9\:(Reflexive,\:Symmetric,\:Antisymmetric,\:Transitive)$$ $$R⊂X×Y,$$ then $$∀x,y,z∈X$$

1. $$x∈R(x)⇒R\: :$$ reflexive,
1. $$"x∈R(y)⇔y∈R(x)"⇒R\: :$$ symmetric,
1. $$"x∈R(y)\&y∈R(x)⇔x=y"⇒R\: :$$ antisymmetric, and
1. $$"x∈R(y)\&y∈R(z)⇒x∈R(z)"⇒R\: :$$ transitive.

$$Example1$$ $$"≥"…x≥x$$ (reflexive), $$x_{1}≥x_{2}⇎x_{2}≥x_{1}$$ (not symmetric), $$x_{1}≥x_{2}\&x_{2}≥x_{1}⇔x_{1}=x_{2}$$ (antisymmetric), and $$x_{1}≥x_{2}\&x_{2}≥x_{3}⇒x_{1}≥x_{3}$$ (transitive).

$$Definition10\:(Partial\:Preordering) \:⪰⊂X×X.\:1.\:∀x∈X,\:x⪰x$$ and $$2. \:∀x,y,z∈X,\:x⪰y\&y⪰z⇒x⪰z$$, then $$⪰\: :$$ Partial Preordering (PPO).

$$Definition11\:(Preordering) \:⪰⊂X×X.\:1.\:∀x∈X,\:x⪰x,$$ $$2. \:∀x,y,z∈X,\:x⪰y\&y⪰z⇒x⪰z$$, and $$3. ∀x,y∈X,\:x⪰y\:or\:y⪰x,\:or\:both,$$ then $$⪰\: :$$ Preordering (PO).

$$Definition12\:(Ordering) \:⪰⊂X×X.\:1.\:∀x∈X,\:x⪰x,$$ $$2. \:∀x,y,z∈X,\:x⪰y\&y⪰z⇒x⪰z$$, $$3. ∀x,y∈X,\:x⪰y\:or\:y⪰x,\:or\:both,$$ and $$4. ∀x,y∈X,\:x⪰y\&y⪰x⇔x=y,$$ then $$⪰\: :$$ Ordering (O).

![](/assets/img/PPO_PO_O_table.jpg)

- The antisymmetricity rules out the possibility of "indifference curve".

$$Definition13\:(Ordered\:set)$$ $$⪰⊂X×X$$ : PPO/PO/O $$⇒X$$ : PPO/PO/O'ed set.

$$Definition14\:(Maximal\&Minimal\:elements)$$ $$⪰⊂X×X:$$ PPO, $$X$$ : PPO'ed set, then $$∀x∈X,$$

$$∄x≠\bar{x}\:s.t.\:x⪰\bar{x}\&\bar{x}⪰̸x⇒\bar{x}$$ : maximal with respect to $$⪰$$.

$$∄x≠\underline{x}\:s.t.\:x⪯\underline{x}\&\underline{x}⪯̸x⇒\underline{x}$$ : minimal with respect to $$⪰$$.

$$Definition15\:(Largest\&Smallest\:elements)$$ $$⪰⊂X×X:$$ PO, $$X$$ : PO'ed set, then $$∀x∈X,$$

$$∃\bar{z}∈X\:s.t.\:\bar{z}⪰x⇒\bar{z}$$ : largest in $$X$$.

$$∃\underline{z}∈X\:s.t.\:\underline{z}⪯x⇒\underline{z}$$ : smallest in $$X$$.

- The maximal cannot be strictly dominated by anything, and the minimal can strictly dominate nothing.

-The largest can dominate every other elements, and the smallest can be dominated by every other elements.

- If it is the largest/smallest, then it is the maximal/minimal, but not the other way around. This is because, "non-comparable pair" may be possible in PPO.

$$Example2$$ $$X={-4,0,1,2,4,a}…a$$ : maximal & minimal, but not the largest or smallest. Also, -4 & 4 cannot be the smallest/largest in $$X$$. They are the minimal/maximal.

### Rudin, PMA part

(p.3)

$$Definition16\:(Bounded,\:Bounds)$$ $$≥⊂S×S:\:O,\:S\: :\:O\:set,\:E⊂S.$$

$$∃β∈S\:s.t.\:∀x∈E,\:x≤β⇒E$$ : bounded above, $$β$$ : upperbound of $$E$$.

$$∃γ∈S\:s.t.\:∀x∈E,\:x≥γ⇒E$$ : bounded below, $$γ$$ : lowerbound of $$E$$.

$$Definition17\:(Least\:Upper\:Bound(LUB) \:or \:Supremum(Sup))$$ $$≥:S×S:O,\:S\: :\:O\: set,\:E⊂S,\:E\:$$ : bounded above.

$$∃α∈S\:s.t.\:[\{∀x∈E,\:x≤α\}\&\{∀γ∈S\:s.t.\:(γ<α),\: ∃x∈E,x>γ\}]⇒α$$ : LUB of $$E$$ $$⇔α=supE$$.

$$Definition18\:(Greatest\:Lower\:Bound(GLB) \:or\: Infimum(Inf))$$ $$≥:S×S:O,\:S\: :\:O\: set,\:E⊂S,\:E\:$$ : bounded below.

$$∃β∈S\:s.t.\:[\{∀x∈E,\:x≥β\}\&\{∀γ∈S\:s.t.\:(γ>β),\: ∃x∈E,x<γ\}]⇒α$$ : GLB of $$E$$ $$⇔α=InfE$$.

## Function

$$Definition19\:(Function)$$ $$f⊂X×Y\:s.t.\:∀x∈X,\:∃!y∈Y\:(s.t.\:y∈f(x))⇒f$$ : function from $$X$$ to $$Y$$ $$⇔f:X→Y$$.

$$Definition20\:(Domain,\:Range,\:Image,\:\&\:Inverse\:image)$$ $$f:X→Y,\:A⊂X,\:B⊂Y$$

$$X$$ : domain of $$f$$,

$$f(X)$$ : range of $$f$$,

$$f(A)$$ : image set of $$A$$, and

$$f^{-1}(B)$$ : inverse image set of $$B$$.

- Recall that $$f(A)=\{y∈Y:∃x∈A\:s.t.\:y∈f(x)\}=∪_{x∈A}f(x)$$ and $$f(x)$$ is always singleton in function compared to relations. $$f^{-1}(B)=\{x∈X:∃y∈B\:s.t.\:y=f(x)\}$$. The last part of inverse image set differs from image set due to the uniqueness of $$f(x)$$.

$$Definition21\:(Surjective(Onto))$$ $$f:X→Y.\:f(X)=Y⇒f$$ : surjective, or onto $$Y$$.

$$Definition22\:(Injective(one-to-one))$$ $$f:X→Y.\:∀x_{1},x_{2}∈X\:s.t.\:x_{1}≠x_{2},\:f(x_{1})≠f(x_{2})$$.

- Surjective means "no leftover elements in $$Y$$." Injective means "no overlaps between $$f(x)$$ values."

$$Definition23\:(Bijective(one-to-one\:correspondence))$$ $$f:X→Y.$$

$$f(X)=Y\:\&\:∀x_{1},x_{2}∈X\:s.t.\:x_{1}≠x_{2},\:f(x_{1})≠f(x_{2})⇒f$$ : bijective.

$$Definition24\:(Correspondence)$$ $$Ψ⊂X×Y\:s.t.\:Ψ:X→P(Y)⇒Ψ$$ : correspondence $$⇔Ψ:X→→Y.$$

- The definition of correspondence is not rigorous. But the point is that correspondence is like a function that is from $$X$$ to the power set of $$Y$$. Function is a special case of correspondence, since it is a correspondence from $$X$$ to a subset of $$P(Y)$$ whose elements are elements of $$Y$$.

### Rudin, PMA part

(p.26)
$$Definition25\:(Sequence)\:f:\mathbb{N}(or\:\mathbb{Z})→Y⇒f$$ : sequence.

- $$s_{n}:=f(n)\:\&\:\{s_{n}\}:=f(\mathbb{N})$$ is used customarily.

(p.55)
$$Definition26\:(Monotone\:Sequences)\:\{s_{n}\}:\mathbb{N}→\mathbb{R}.$$

$$1. \:s_{n}≤s_{n+1}⇒\{s_{n}\}$$ : monotonically increasing, and

$$2. \:s_{n}≥s_{n+1}⇒\{s_{n}\}$$ : monotonically decreasing.

(p.32)
$$Definition27\:(Bounded\:set)$$ $$(X,d)$$ : metric space, $$E⊂X.$$

$$∃M∈\mathbb{R}\:\&\:∃q∈X\:s.t.\:∀p∈E,\:d(p,q)<M⇒E$$ : bounded.

(p.47)
$$Definition28\:(Convergence)$$ $$(X,d)$$ : metric space, $$\{p_{n}\}:\mathbb{N}→X.$$

$$∃p∈X\:s.t.\:[∀ϵ>0,∃N∈\mathbb{N}\:s.t.\:∀n>N,\:d(p_{n},p)<ϵ]⇒\{p_{n}\}$$ : converges to $$p$$ $$⇔\:p_{n}→p.$$

(p.48)
$$Definition29\:(Bounded\:sequence)$$ $$(X,d)$$ : metric space, $$f:\mathbb{N}→X.$$

$$f(\mathbb{N})$$ : bounded $$⇒\:f$$ : bounded.

- Note that $$f(\mathbb{N})$$ is the range of  the sequence.

(p.55)
$$Theorem1\:\{s_{n}\}\::\:monotone,\:then\:s_{n}→s⇔\{s_{n}\}\::\:bounded.$$

$$proof$$

WLOG, $$∀n∈\mathbb{N},\:s_{n}≤s_{n+1}.$$
$$(⇐\rvert)$$ Since $$\{s_{n}\}$$ : bounded, $$∃supR_{\{s_{n}\}}=:s.$$ $$∴s_{n}≤s,\:∀n∈\mathbb{N}.$$

Then, $$∀ϵ>0,∃N∈\mathbb{N}\:(s.t.\:∀n≥N,\:s-ϵ<s_{n}≤s)⇒\lvert s_{n}-s \rvert<ϵ. ∎$$

$$(\lvert⇒)$$ Since $$\{s_{n}\}→s,\:∃N∈\mathbb{N},\:s.t.\:\lvert s_{n}-s\rvert <1.$$ 

Then, pick $$r=max{1,\lvert s_{1}-s\rvert,…,\lvert s_{N}-s\rvert}\dots
Then, $$∀n∈\mathbb{N},\:\lvert s_{n}-s\rvert<r.$$

This means that we can come up with an open ball with radius $$r$$ and center $$s$$ that contains all the elements in $$\{s_{n}\}. ∎$$

# Vector Space, Metric Space, Limit, and Continuity

### Rudin, PMA part

(p.5)
$$Definition1\: (Field)$$

A $$field$$ is a set $$F$$ with two operations : $$addition$$ and $$multiplication$$ $$s.t.$$ satisfies the following axioms.

(A : Addition) $$∀x,y,z∈F$$

1. $$x+y∈F$$ (Closed)
2. $$x+y=y+x$$ (Commutativity)
3. $$(x+y)+z=x+(y+z)$$ (Associativity)
4. $$∃0∈F\:s.t.\:0+x=x$$ (Existence of additive identity)
5. $$∃(-x)∈F\:s.t.\:x+(-x)=0$$ (Existence of inverse element)

(M: Multiplication) $$∀x,y,z∈F$$

1. $$xy∈F$$ (Closed)
2. $$xy=yx$$ (Commutativity)
3. $$x(yz)=(xy)z$$ (Associativity)
4. $$∃1∈F\:s.t.\:1≠0,\:and\:1×x=x$$ (Existence of multiplicative identity)
5. $$∀x∈F\:s.t.\:x≠0,\:∃\frac{1}{x}∈F\:s.t.\:x×\frac{1}{x}=1$$ (Existence of inverse element)

(D : The distributive law) $$∀x,y,z∈F$$

$$(x+y)×z=x×z+y×z$$


(p.9)
How do we prove $$\mathbb{R}\backslash\mathbb{Q}$$ is dense in $$\mathbb{R}.$$

$$proof$$

Let $$k∈\mathbb{R}\backslash\mathbb{Q}. $$ $$x<y⇒\frac{x}{k}<\frac{y}{k}.$$ Then, by  $$Thm5$$ in Set and Logic, $$∃p∈\mathbb{Q}\:s.t.\:x<kp<y.$$
If $$kp∈\mathbb{R}\backslash\mathbb{Q},$$ then the statement is proved.

WTS: $$∀x∈\mathbb{R}\backslash\mathbb{Q}\:and\:∀y∈\mathbb{Q},\:xy∈\mathbb{R}\backslash\mathbb{Q}.$$

Assume $$xy∈\mathbb{Q},$$ then, since $$\mathbb{Q}⊂\mathbb{R}$$ and $$\mathbb{R}\: :\:field,$$ $$\mathbb{Q}$$ is closed in multiplication and $$\frac{1}{y}∈\mathbb{Q}$$.
$$⇒xy×\frac{1}{y}=x∈\mathbb{Q}.$$
This makes contradiction with $$x∈\mathbb{R}\backslash\mathbb{Q}. \:∎$$

$$Definition2\: (Vector\: Space)$$ 

A vector space defined over a field $$F$$ is a set $$V$$ of elements called vectors, with (1) a binary operation $$V\times V→V$$ called **vector addition**, and (2) an operator $$F\times V→V$$ called a **scalar multiplication**.

- The two operations of vector space have the following properties.

(1) $$V$$: closed under vector addition, and $$∀x,y,z\in V$$, we have the following:

1. Associative : $$x+(y+z)=(x+y)+z=x+y+z$$
2. Commutative : $$x+y=y+x$$
3. Existence of the additive identity : $$∃! \underline{0} ∈V:\:x+\underline{0}=\underline{0}+x=x$$
4. Existence of inverse elements: $$∀x\in V,\:\exists!(-x)\in V\: : \: x+(-x)=(-x)+x=\underline{0}.$$

(2) $$V$$ : closed under scalar multiplication, and $$∀x,y∈V$$ and $$∀α,β∈F$$, we have the following:

1. Double distributive property: $$α(x+y)=αx+αy$$ and $$(α+β)x=αx+βy$$
2. Associative law for scalars: $$α(βx)=(αβ)x$$
3. Existence of a multiplicative identity: $$\exists!1∈F:\:1x=x$$

$$Definition3\: (Metric \:or\: distance\: function)$$
$$d:\:X×X→\mathbb{R}_{+}\:s.t.\:∀x,y,z∈X,$$

1. $$d(x,y)≥0$$ (nonnegativity) and $$d\left(x,y\right)=0⇔x=y$$ (asymmetry)
2. $$d(x,y)=d(y,x)$$ (commutativity)
3. $$d(x,z)≤d(x,y)+d(y,z)$$ (triangular inequality)

$$Definition4\: (Metric Space)$$
A metric space is a pair $$(X,d)$$ where $$X$$: a set, $$d$$: a metric defined on $$X$$.

$$Definition5\: (Norm)$$
Let $$V$$: a vector space, $$X$$: the underlying set of points. Then $$\|⋅\|:\:X→\mathbb{R}$$ is called a **norm** if it satisfies the following properties $$∀x,y∈X $$,$$∀α∈\mathbb{R}$$:

1. non-negativity: $$\|x\|≥0$$
2. only the zero vector has zero norm: $$\|x\|=0⇔x=0$$
3. triangular inequality: $$\|x+y\|≤\|x\|+\|y\|$$
4. scalar multiplication: $$\|αx\|= \lvert α\rvert \|x\|$$

$$Definition6\:(Normed\: vector\: space)$$

A normed vector space is a vector space $$V$$ equipped with norm.

$$Theorem 1$$
For $$∀x,y∈V,\: d(x,y)=\|x-y\|$$ is a metric.

$$proof$$

1. (non-negativity&asymmetry) $$\|x-y\|≥0$$ and $$\|x-y\|=0⇔x=y$$ by the 1. and 2. of $$Def5$$.
2. (commutativity) $$\|x-y\|= \lvert -1\rvert \|y-x\|=\|y-x\|$$ by the 4. in $$Def5$$.
3. (triangular inequality) $$∀x,y,z∈V,\|x-z\|+\|z-y\|≥\|x-y\|$$ by 3. in $$Def5$$.

$$Definition7\:(Euclidean \:space)$$ 

The $$n$$-dimensional **Euclidean space** is a normed vector space, $$E^{n}\left(\mathbb{R}^{n},d_{E}\right)$$, where $$d_{E}(x,y)=\|x-y\|_{E}=\sqrt{∑_{i=1}^{n}(x_{i}-y_{i})^{2}}$$

$$Theorem 2\: d_{E}\::\:Norm$$

$$proof$$ We have to show that $$d_{E}$$ suffices 1.~4. in the $$Def.5$$. 1, 2, and 4 is rather trivial. We will only show 3. 
3. $$∑_{i}(x_{i}+y_{i})^{2}=∑_{i}(x_{i}^{2}+2x_{i}y_{i}+y_{i}^{2})=∑_{i}x_{i}^{2}+2∑_{i}x_{i}y_{i}+∑_{i}y_{i}^{2}$$

$$≤∑_{i}x_{i}^{2}+2\sqrt{∑_{i}x_{i}^{2}}\sqrt{∑_{i}y_{i}^{2}}+∑_{i}y_{i}^{2}=(\sqrt{∑_{i}x_{i}^{2}}+\sqrt{∑_{i}y_{i}^{2}})^{2}\:(∵Chauchy-Schwartz\:inequality)$$

$$∴\sqrt{∑_{i}(x_{i}+y_{i})^{2}}≤\sqrt{∑_{i}x_{i}^{2}}+\sqrt{∑_{i}y_{i}^{2}}\:∎$$

$$Theorem3\:(Uniqueness\:of\:limit)\:(X,d)\::\:metric\:space,\:\{x_{n}\}:\mathbb{N}→X.\:\{x_{n}\}$$ has at most one limit.

$$proof$$


# Vector Subspace and Affine Subspace


# Convexity and Seperating Hyperplane


# Differential Calculus


