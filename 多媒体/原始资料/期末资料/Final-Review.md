# Final Review 1 · CMPT365 Multimedia Systems (SFU, 2017 春)

> 来源：`Final-Review.pdf`，pymupdf 逐页抽取。英文原始复习课件，是本课中文讲义的蓝本。


## p.1

CMPT365 Multimedia Systems    1
Final Review - 1
Spring 2017 
CMPT 365 Multimedia Systems

## p.2

CMPT365 Multimedia Systems    2
Outline
❒Entropy
❒Lossless Compression
❍Shannon-Fano Coding
❍Huffman Coding
❍LZW Coding
❍Arithmetic Coding
❒Lossy Compression
❍Quantization
❍Transform Coding - DCT

## p.3

CMPT365 Multimedia Systems    3
Why is Compression possible ?
❒Information Redundancy 
❒Question: How is “information” measured ?

## p.4

CMPT365 Multimedia Systems    4
Self-Information
❒
Intuition 1:
❍I’ve heard this story many times vs This is the first time I hear about this story
❍Information of an event is a function of its probability:
i(A) = f (P(A)). Can we find the expression of f()?
❒
Intuition 2:
❍Rare events have high information content
•
Water found on Mars!!!
❍Common events have low information content
•
It’s raining in Vancouver.
àInformation should be a decreasing function of the probability:
Still numerous choices of f().
❒
Intuition 3: 
❍Information of two independent events = sum of individual information:
If P(AB)=P(A)P(B)  èi(AB) = i(A) + i(B).
àOnly the logarithmic function satisfies these conditions.
Information is related to probability
Information is a measure of uncertainty (or “surprise”)

## p.5

CMPT365 Multimedia Systems    5
Self-information
❒Shannon’s Definition [1948]:
❍Self-information of an event:
)
(
log
)
(
1
log
)
(
A
P
A
P
A
i
b
b
-
=
=
If  b  =  2,  unit  of  information  is  bits
1
P(A)
)
(
log
A
P
b
-
0

## p.6

CMPT365 Multimedia Systems    6
Entropy
❒Suppose:
❍
a data source generates output sequence from a set {A1, A2, …, AN}
❍P(Ai): Probability of Ai
❒First-Order Entropy (or simply Entropy):
❍the average self-information of the data set
å-
=
i
i
i
A
P
A
P
H
)
(
log
)
(
2
❒The first-order entropy represents the minimal number of bits 
needed to losslessly represent one output of the source.

## p.7

CMPT365 Multimedia Systems    7
Example 1
❒X is sampled from {a, b, c, d}
❒Prob: {1/2, 1/4, 1/8, 1/8}
❒Find entropy.

## p.8

CMPT365 Multimedia Systems    8
Outline
❒Why compression ?
❒Entropy
❒Variable Length Coding
❍Shannon-Fano Coding
❍Huffman Coding
❍LZW Coding
❍Arithmetic Coding

## p.9

CMPT365 Multimedia Systems    9
Entropy Coding: Prefix-free Code
❒No codeword is a prefix of another one.
❒Can be uniquely decoded.
❒Also called prefix code
❒Example: 0, 10, 110, 111
❒Binary Code Tree
0
1
0
1
0
1
0
10
110
111
Root  node
leaf  node
Internal  node
❒Prefix-free code contains leaves only.
❒How to state it mathematically?

## p.10

CMPT365 Multimedia Systems    10
Shannon-Fano Coding
❒Shannon-Fano Algorithm - a top-down approach
❍Sort the symbols according to the frequency count of 
their occurrences.
❍Recursively divide the symbols into two parts, each with 
approximately the same number of counts, until all parts 
contain only one symbol.
❒Example: coding of “HELLO“

## p.11

CMPT365 Multimedia Systems    11
Outline
❒Why compression ?
❒Entropy
❒Variable Length Coding
❍Shannon-Fano Coding
❍Huffman Coding
❍LZW Coding
❍Arithmetic Coding

## p.12

CMPT365 Multimedia Systems    12
Huffman Coding
❒A procedure to construct optimal prefix-free code 
❒Result of David Huffman’s term paper in 1952 when he was a 
PhD student at MIT
Shannon àFano àHuffman
❒Observations:
❍Frequent symbols have short codes.
❍In an optimum prefix-free code, the two codewords that occur 
least frequently will have the same length.
a
c
b
Can  be
truncated

## p.13

CMPT365 Multimedia Systems    13
Huffman Coding
❒Human Coding - a bottom-up approach
❍Initialization: Put all symbols on a list sorted 
according to their frequency counts.
• This might not be available !
❍Repeat until the list has only one symbol left:
(1) From the list pick two symbols with the lowest 
frequency counts. Form a Huffman subtree that has these 
two symbols as child nodes and create a parent node.
(2) Assign the sum of the children's frequency counts to 
the parent and insert it into the list such that the order is 
maintained.
(3) Delete the children from the list.
❍Assign a codeword for each leaf based on the 
path from the root.

## p.14

CMPT365 Multimedia Systems    14
More Example
❒
Source alphabet A = {a1, a2, a3, a4, a5}
❒
Probability distribution: {0.2, 0.4, 0.2, 0.1, 0.1}
a2  (0.4)
a1(0.2)
a3(0.2)
a4(0.1)
a5(0.1)
Sort
0.2
combine
Sort
0.4
0.2
0.2
0.2
0.4
combine
Sort
0.4
0.2
0.4
0.6
combine
0.6
0.4
Sort
1
combine
Assign  code
0
1
1
00
01
1
000
001
01
1
000
01
0010
0011
1
000
01
0010
0011
❒
Note: Huffman codes are not unique!
❍Labels of two branches can be arbitrary.
❍Multiple sorting orders for tied probabilities

## p.15

CMPT365 Multimedia Systems    15
Properties of Huffman Coding
❒Unique Prefix Property: 
❍No Human code is a prefix of any other Human code -
precludes any ambiguity in decoding.
❒Optimality: 
❍minimum redundancy code - proved optimal for a given 
data model (i.e., a given, accurate, probability 
distribution) under certain conditions.
❍The two least frequent symbols will have the same length 
for their Human codes, differing only at the last bit.
❍Symbols that occur more frequently will have shorter 
Huffman codes than symbols that occur less frequently.
❒Average Huffman code length for an information 
source S is strictly less than entropy+ 1
1
l
h
<
+

## p.16

CMPT365 Multimedia Systems    16
Example
❒Source alphabet A = {a, b, c, d, e}
❒Probability distribution: {0.2, 0.4, 0.2, 0.1, 0.1}
❒Code: {01, 1, 000, 0010, 0011}
❒Entropy:
H(S) = - (0.2*log2(0.2)*2 + 0.4*log2(0.4)+0.1*log2(0.1)*2)
= 2.122 bits / symbol
❒Average Huffman codeword length:
L = 0.2*2+0.4*1+0.2*3+0.1*4+0.1*4 = 2.2 bits / symbol
❒In general:  H(S) ≤ L < H(S) + 1

## p.17

CMPT365 Multimedia Systems    17
Huffman Decoding
❒Direct Approach:
❍Read one bit, compare with all codewords…
❍Slow
❒Binary tree approach:
❍Embed the Huffman table into a binary tree data structure
❍Read one bit: 
• if it’s 0, go to left child. 
• If it’s 1, go to right child. 
• Decode a symbol when a leaf is reached.
❍Still a bit-by-bit approach

## p.18

CMPT365 Multimedia Systems    18
Table Look-up Method
000          010    011    100
a
b
c
d
a:  00
b:  010
c:  011
d:  1
char HuffDec[8][2] = {
{‘a’, 2}, 
{‘a’, 2},
{‘b’, 3},
{‘c’, 3},
{‘d’, 1}, 
{‘d’, 1}, 
{‘d’, 1}, 
{‘d’, 1}
};
x = ReadBits(3);
k = 0;   //# of symbols decoded
While (not EOF) {
symbol[k++] = HuffDec[x][0];
length = HuffDec[x][1];
x = x << length;
newbits = ReadBits(length);
x = x | newbits;
x = x & 111B;
}

## p.19

CMPT365 Multimedia Systems    19
Extended Huffman Code
❒Code multiple symbols jointly
❍Composite symbol: (X1, X2, …, Xk)
❒Code symbols of different meanings jointly
❍JPEG: Run-level coding
❍H.264 CAVLC: context-adaptive variable length coding
• # of non-zero coefficients and # of trailing ones
❍Studied later
❍Alphabet increased exponentioally: k^N

## p.20

CMPT365 Multimedia Systems    20
Example 
❒P(Xi = 0) = P(Xi = 1) = 1/2
❍Entropy H(Xi) = 1 bit / symbol
❒
Joint probability: P(Xi-1, Xi)
❍P(0, 0) = 3/8,
P(0, 1) = 1/8
❍P(1, 0) = 1/8,
P(1, 1) = 3/8
❒
Second order entropy:
symbol
 / 
bits
 
0.9056
or 
 
symbols,
 2
 / 
bits
 
1.8113
)
,
(
1
=
-
i
i
X
X
H
❒Huffman code for Xi
❒Average code length
❒Huffman code for (Xi-1, Xi)
❒Average code length
0, 1
1 bit / symbol
1, 00, 010, 011
0.9375 bit /symbol
0
1
0
3/8
1/8
1
1/8
3/8
Xi
Xi-­1
Joint  Prob  P(Xi-­1,  Xi)
Consider  10 00 01 00 00 11 11 11    -- every two; non-overlapped

## p.21

CMPT365 Multimedia Systems    21
Outline
❒Why compression ?
❒Entropy
❒Variable Length Coding
❍Shannon-Fano Coding
❍Huffman Coding
❍LZW Coding
❍Arithmetic Coding

## p.22

CMPT365 Multimedia Systems    22
LZW: Dictionary-based Coding
❒LZW: Lempel-Ziv-Welch (LZ 1977, +W 1984)
❍Patent owned by Unisys http://www.unisys.com/about__unisys/lzw/
•
Expired on June 20, 2003 (Canada: July 7, 2004 )
❍ARJ, PKZIP, WinZip, WinRar, Gif,
❒Uses fixed-length codewords to represent variable-length 
strings of symbols/characters that commonly occur together
❍e.g., words in English text.
❍Encoder and decoder build up the same dictionary dynamically 
while receiving the data.
❍
Places longer and longer repeated entries into a dictionary, and 
then emits the code for an element, rather than the string 
itself, if the element has already been placed in the dictionary.

## p.23

CMPT365 Multimedia Systems    23
LZW Algorithm
BEGIN
s = next input character;
while not EOF
{ 
c = next input character;
if s + c exists in the dictionary
s = s + c;
else
{ 
output the code for s;
add string s + c to the dictionary with a new code;
s = c;
}
}
output the code for s;
END

## p.24

CMPT365 Multimedia Systems    24
Example
❒LZW compression for string “ABABBABCABABBA“
❒Start with a very simple dictionary (also referred to as a “string 
table"), initially containing only 3 characters, with codes as 
follows:
❒Input string is “ABABBABCABABBA"

## p.25

CMPT365 Multimedia Systems    25
❒
Input ABABBABCABABBA
❒
Output codes: 1 2 4 5 2 3 4 6 1. Instead of sending 14 characters, only 9 
codes need to be sent (compression ratio = 14/9 = 1.56).
BEGIN
s = next input character;
while not EOF
{ 
c = next input character;
if s + c exists in the dictionary
s = s + c;
else
{ 
output the code for s;
add string s + c to the 
dictionary with a new code;
s = c;
}
}
output the code for s;
END

## p.26

CMPT365 Multimedia Systems    26
LZW Decompression (simple version)
BEGIN
s = NIL;
while not EOF
{
k = next input code;
entry = dictionary entry for k;
output entry;
if (s != NIL)
{add string s + entry[0] to dictionary with a new code;}
s = entry;
}
END
❒Example 7.3:  LZW decompression for string “ABABBABCABABBA”.  
❒Input codes to the decoder are 1 2 4 5 2 3 4 6 1.
❒The initial string table is identical to what is used by the encoder.

## p.27

CMPT365 Multimedia Systems    27
❒
Apparently, the output string is “ABABBABCABABBA”, a truly lossless result!
S
K
Entry/output
Code
String
1
2
3
A
B
C
NIL
A
B
AB
BA
B
C
AB
ABB
A
1
2
4
5
2
3
4
6
1
EOF
A
B
AB
BA
B
C
AB
ABB
A
4
5
6
7
8
9
10
11
AB
BA
ABB
BAB
BC
CA
ABA
ABBA
•
The LZW decompression algorithm then works as follows:
•
Input: 1 2 4 5 2 3 4 6 1
BEGIN
s = NIL;
while not EOF
{
k = next input code;
entry = dictionary 
entry for k;
output entry;
if (s != NIL)
add string s + 
entry[0] to dictionary 
with a new code;
s = entry;
}
END

## p.28

CMPT365 Multimedia Systems    28
Outline
❒Why compression ?
❒Entropy
❒Variable Length Coding
❍Shannon-Fano Coding
❍Huffman Coding
❍LZW Coding
❍Arithmetic Coding

## p.29

CMPT365 Multimedia Systems    29
Basic Idea
000          010    011    100
1
00
010      011
❒Recall table look-up decoding of Huffman code
❍N: alphabet size
❍L: Max codeword length
❍Divide [0, 2^L] into N intervals
❍One interval for one symbol
❍Interval size is roughly
proportional to symbol prob.
❒Arithmetic coding applies this idea recursively
❍Normalizes the range [0, 2^L] to [0, 1].
❍Map a sequence to a unique tag in [0, 1).
0                                                                                                          1
abcd…..
dcba…..

## p.30

CMPT365 Multimedia Systems    30
Arithmetic Coding
❒Disjoint and complete partition of the range [0, 1) 
[0, 0.8), [0.8, 0.82), [0.82, 1)
❒Each interval corresponds to one symbol
❒Interval size is proportional to symbol probability
❒Observation: once the tag falls into an interval, it never gets out 
of it
0                                                              1
❒The first symbol restricts the tag 
position to be in one of the intervals
❒The reduced interval is partitioned 
recursively as more symbols are 
processed.
0
1
0
1
0
1
a                  b      c

## p.31

CMPT365 Multimedia Systems    31
Example:
Symbol
Prob.
1
0.8
2
0.02
3
0.18
1                                                                2            3
0                            
0.8    0.82          1.0
❒Map to real line range [0, 1)
❒Order does not matter 
❍Decoder need to use the same order
❒Disjoint but complete partition: 
❍1: [0, 0.8):
0,      0.799999…9
❍2: [0.8, 0.82):
0.8,   0.819999…9
❍3: [0.82, 1):   
0.82, 0.999999…9
❍(Think about the impact to integer 
implementation)

## p.32

CMPT365 Multimedia Systems    32
Range  0.00288
1                                                                2            3
0.7712
0.773504    0.7735616  0.77408
Range  0.144
1                                                                2            3
0.656
0.7712        0.77408    0.8
Encoding
❒Input sequence: “1321”
Range  1
Final  range:  [0.7712,  0.773504):    Encode  0.7712
1                                                                2            3
0                            
0.8    0.82          1.0
Range  0.8
1                                                                2            3
0
0.64  0.656          0.8
Difficulties:  1.  Shrinking  of  interval  requires  high  precision  for  long  sequence.
2.  No  output  is  generated  until  the  entire  sequence  has  been  processed.

## p.33

CMPT365 Multimedia Systems    33
Encoder Pseudo Code
BEGIN
low = 0.0;  high = 1.0;  range = 1.0;
while (symbol != terminator)
{
get (symbol);
low = low + range * Range_low(symbol);
high = low + range * 
Range_high(symbol);
range = high - low;
}
output a code so that low <= code < high;
END
Input
HIGH
LOW
RANGE
Initial
1.0
0.0
1.0
1
0.0+1.0*0.8=0.8
0.0+1.0*0 = 0.0
0.8
3
0.0 + 0.8*1=0.8
0.0 + 0.8*0.82=0.656
0.144
2
0.656+0.144*0.82=0.77408
0.656+0.144*0.8=0.7712
0.00288
1
0.7712+0.00288*0.8=0.773504
0.7712+0.00288*0=0.7712
0.002304
❒Keep track of LOW, 
HIGH, RANGE 
❍Any two are sufficient, 
e.g., LOW and RANGE.

## p.34

CMPT365 Multimedia Systems    34
Generating Codeword for Encoder
BEGIN
code = 0;
k = 1;
while (value(code) < low)
{ 
assign 1 to the kth binary fraction bit
if (value(code) >= high)
replace the kth bit by 0
k = k + 1;
}
END
•The final step in Arithmetic encoding calls for the generation of a 
number that falls within the range [low, high). The above algorithm will 
ensure that the shortest binary codeword is found.

## p.35

CMPT365 Multimedia Systems    35
1                                                                2            3
0                            
0.8    0.82          1.0
1                                                              2            3
0                            
0.8    0.82          1.0
1                                                                2            3
0                            
0.8    0.82          1.0
1                                                                2            3
0                            
0.8    0.82          1.0
Receive  0.7712
Decode  1
x  =(0.7712-­0)  /  0.8
=  0.964
Decode  3
Simplified Decoding
range
low
x
x
-
¬
❒Normalize RANGE to [0, 1) each time
❒No need to recalculate the thresholds.
x  =(0.964-­0.82)  /  0.18
=  0.8
Decode  2
x  =(0.8-­0.8)  /  0.02
=  0
Decode  1

## p.36

CMPT365 Multimedia Systems    36
Decoder Pseudo Code
BEGIN
get binary code and convert to
decimal value = value(code);
DO
{ 
find a symbol s so that
Range_low(s) <= value < Range_high(s);
output s;
low = Rang_low(s);
high = Range_high(s);
range = high - low;
value = [value - low] / range;
}
UNTIL symbol s is a terminator
END

## p.37

CMPT365 Multimedia Systems    37
Lossless vs Lossy Compression
❒If the compression and decompression processes 
induce no information loss, then the compression 
scheme is lossless; otherwise, it is lossy.
❒Why is lossy compression possible ?
Compression Ratio: 12.3
Compression Ratio: 7.7
Compression Ratio: 33.9
Original

## p.38

CMPT365 Multimedia Systems    38
Outline
❒Quantization
❍Uniform
❍Non-uniform
❒Transform coding
❍DCT

## p.39

CMPT365 Multimedia Systems    39
Uniform Quantizer
❒
All bins have the same size except possibly for the two outer intervals:
❍bi and yi are spaced evenly
❍The spacing of bi and yi are both ∆ (step size)
∆2∆3∆Input
-­3∆-­2∆-­∆
Reconstruction
3.5∆
2.5∆
1.5∆
0.5  ∆
-­0.5∆
-­1.5∆
-­2.5∆
-­3.5∆
Uniform  Midrise Quantizer
Even number  of  reconstruction  levels
0  is  not a  reconstruction  level
-­2.5∆-­1.5∆-­0.5∆
Reconstruction
3∆
2∆
∆
-­∆
-­2∆
-­3∆
Uniform  Midtread Quantizer
0.5∆1.5∆2.5∆Input
Odd number  of  reconstruction  levels
0  is  a  reconstruction  level
(
)
i
i
i
b
b
y
+
=
-1
2
1
for  inner  intervals.

## p.40

CMPT365 Multimedia Systems    40
Measure of Distortion
❒
Quantization error: 
❒
Mean Squared Error (MSE) for Quantization
❍Average quantization error of all input values
❍Need to know the probability distribution of the input
❒
Number of bins: M
❒
Decision boundaries: bi, i = 0, …, M
❒
Reconstruction Levels: yi, i = 1, …, M
❒
Reconstruction: 
i
i
i
b
x
b
y
x
£
<
=
-1
 
iff
   
ˆ
❒MSE:
(
)
(
)
åò
ò
=
¥
¥
-
-
-
=
-
=
M
i
b
b
i
q
i
i
dx
x
f
y
x
dx
x
f
x
x
MSE
1
2
2
1
)
(
)
(
ˆ
x
x
x
e
ˆ
)
(
-
=
❍Same as the variance of e(x) if µ = E{e(x)} = 0 (zero mean).
❍Definition of Variance: 
(
)
de
e
f
e
e
e
)
(
2
2
ò
¥
¥
-
-
=
µ
s

## p.41

CMPT365 Multimedia Systems    41
•
Companded quantization is nonlinear.
•
As shown above, a compander consists of a compressor 
function G, a uniform quantizer, and an expander function 
G−1.
•
The two commonly used companders are the µ-law and A-
law companders.
Non-uniform Quantization

## p.42

CMPT365 Multimedia Systems    42
Outline
❒Quantization
❍Uniform
❍Non-uniform
❍Vector quantization
❒Transform coding
❍DCT

## p.43

CMPT365 Multimedia Systems    43
Vector Quantization (VQ)
•
According to Shannon’s original work on information 
theory, any compression system performs better if it 
operates on vectors or groups of samples rather than 
individual symbols or samples.
•
Form vectors of input samples by simply concatenating 
a number of consecutive samples into a single vector.
•
Instead of single reconstruction values as in scalar 
quantization, in VQ code vectors with n components 
are used. A collection of these code vectors form the 
codebook.

## p.44

CMPT365 Multimedia Systems    44
❒Fig. 8.5: Basic vector quantization procedure.

## p.45

CMPT365 Multimedia Systems    45
Outline
❒Quantization
❍Uniform quantization
❍Non-uniform quantization
❒Transform coding
❍Discrete Cosine Transform (DCT)

## p.46

CMPT365 Multimedia Systems    46
Why Transform Coding ?
❒Transform
❍From one domain/space to another space
❍Time -> Frequency
❍Spatial/Pixel -> Frequency
❒Purpose of transform
❍Remove correlation between input samples
❍Transform most energy of an input block into a few 
coefficients
❍Small coefficients can be discarded by quantization without too 
much impact to reconstruction quality
Entropy
coding
Quantization
Transform
Encoder

## p.47

CMPT365 Multimedia Systems    47
1-D Example
❒
Fourier Transform

## p.48

CMPT365 Multimedia Systems    48
1-D Example
❒
Smooth signals have strong DC (direct current, or zero frequency) and low 
frequency components, and weak high frequency components
High  frequency
DC
1
2
3
4
5
6
7
8
0
100
200
Original Input
1
2
3
4
5
6
7
8
0
1000
2000
DFT Magnitudes
1
2
3
4
5
6
7
8
-500
0
500
DCT Coefficients
Sample  Index
High  frequency
DC

## p.49

CMPT365 Multimedia Systems    49
2-D Example
Original Image
2-D DCT Coefficients. Min= -465.37, max= 1789.00
0
50
100
150
200
250
300
0
2000
4000
6000
8000
10000
-500
0
500
1000
1500
2000
0
1
2
3
x 10
5
❒
Apply transform to each 8x8 block
❒
Histograms of source and DCT coefficients
❒
Most transform coefficients are around 0.
❒
Desired for compression

## p.50

CMPT365 Multimedia Systems    50
Matrix Representation of Transform
❒Linear transform is an N x N matrix:
1
1
´
´
´=
N
N
N
N
x
T
y
T
X
y
❒Inverse Transform:
y
T
x
1
-
=
T
X
y
T
x
-­1
❒Unitary Transform (aka orthonormal):
T
T
T
=
-1
T
X
y
T
x
T
❒For unitary transform: rows/cols have unit norm and are 
orthogonal to each others
î
í
ì
¹
=
=
=
Þ
=
j
i
   
,0
j
i
   
,1
   
   
ij
T
j
i
T
d
t
t
I
TT

## p.51

CMPT365 Multimedia Systems    51
1D Discrete Cosine Transform (1D DCT):
❒(8.19)
❒where i = 0, 1, . . . , 7, u = 0, 1, . . . , 7.
❒1D Inverse Discrete Cosine Transform (1D 
IDCT):
❒(8.20) 
❒where i = 0, 1, . . . , 7, u = 0, 1, . . . , 7.
7
0
( )
(2
1)
( )
cos
( )
2
16
i
C u
i
u
F u
f i
p
=
+
=
å
!f (i )=
u=0
7
∑C (u)
2
cos (2i +1)uπ
16
F (u)

## p.52

CMPT365 Multimedia Systems    52
❒Fig. 8.6: The 1D DCT basis functions.

## p.53

CMPT365 Multimedia Systems    53
❒Fig. 8.6 (Cont’d): The 1D DCT basis functions.

## p.54

CMPT365 Multimedia Systems    54
❒Fig. 8.7:  Examples of 1D Discrete Cosine 
Transform: (a) A DC signal f1(i), (b) An AC signal 
f2(i).
(a)
(b)

## p.55

CMPT365 Multimedia Systems    55
❒Fig. 8.7 (Cont’d):  Examples of 1D Discrete 
Cosine Transform: (c) f3(i) = f1(i)+f2(i), and (d) an 
arbitrary signal f(i).
(c)
(d)

## p.56

CMPT365 Multimedia Systems    56
The Cosine Basis Functions
❒Function Bp(i) and Bq(i) are orthogonal, if
❒(8.22)
❒
Function Bp(i) and Bq(i) are orthonormal, if they are 
orthogonal and
❒(8.23)
❒It can be shown that:
❒
[
( )·
( )]
0
  
p
q
i
B i B i
if p
q
=
¹
å
7
0
(2
1)·
(2
1)·
cos
·cos
0
 
16
16
i
i
p
i
q
if p
q
p
p
=
+
+
é
ù=
¹
ê
ú
ë
û
å
7
0
( )
(2
1)·
( )
(2
1)·
cos
·
cos
1
2
16
2
16
i
C p
i
p
C q
i
q
if p
q
p
p
=
+
+
é
ù=
=
ê
ú
ë
û
å
[
( )·
( )]
1
  
p
q
i
B i B i
if p
q
=
=
å

## p.57

CMPT365 Multimedia Systems    57
2D Discrete Cosine Transform (2D DCT):
❒where i, j, u, v = 0, 1, . . . , 7, and the constants C(u) and C(v) are 
determined by Eq. (8.5.16).
2D Inverse Discrete Cosine Transform (2D IDCT):
❒
The inverse function is almost the same, with the roles of f(i, j) and F(u, 
v) reversed, except that now C(u)C(v) must stand inside the sums:
❒
where i, j, u, v = 0, 1, . . . , 7.
7
7
0
0
( )
( )
(2
1)
(2
1)
( , )
cos
cos
( , )
4
16
16
i
j
C u C v
i
u
j
v
F u v
f i j
p
p
=
=
+
+
=
åå
!f (i , j )=
v=0
7
∑
u=0
7
∑
C (u)C (v)
4
cos (2i +1)uπ
16
cos (2 j +1)vπ
16
F (u,v)

## p.58

CMPT365 Multimedia Systems    58
❒Fig. 8.9:  Graphical Illustration of 8 × 8 2D DCT 
basis.

## p.59

CMPT365 Multimedia Systems    59
2D DCT Matrix Implementation
•
The above factorization of a 2D DCT into two 1D DCTs can 
be implemented by two consecutive matrix multiplications:
❒(8.27)
•
We will name T the DCT-matrix.
❒(8.28)
❒
Where i = 0, … , N-1 and j = 0, … , N-1 are the row and column
indices, and the block size is N x N.

## p.60

CMPT365 Multimedia Systems    60
❒When N = 8, we have:
❒(8.29)
❒(8.30)

## p.61

CMPT365 Multimedia Systems    61
2D IDCT Matrix Implementation
❒The 2D IDCT matrix implementation is 
simply:
❒(8.31)
•
See the textbook for step-by-step derivation of 
the above equation.
- The key point is: the DCT-matrix is orthogonal, 
hence,

## p.62

CMPT365 Multimedia Systems    62
2-D 8-point DCT Example
89   78   76   75   70   82   81   82
122   95   86   80   80   76   74   81
184  153  126  106   85   76   71   75
221  205  180  146   97   71   68   67
225  222  217  194  144   95   78   82
228  225  227  220  193  146  110  108
223  224  225  224  220  197  156  120
217  219  219  224  230  220  197  151
❒Original Data:
❒2-D DCT Coefficients (after rounding to integers):
1155
259  -23    6   11   7   3   0
-377   -50   85  -10   10   4   7  -3
-4  -158  -24   42  -15   1   0   1
-2     3  -34  -19    9  -5   4  -1
1     9    6  -15  -10   6  -5  -1
3    13    3    6   -9   2   0  -3
8    -2    4   -1    3  -1   0  -2
2     0   -3    2   -2   0   0  -1
Most  energy  is  in  the  upper-­
left  corner