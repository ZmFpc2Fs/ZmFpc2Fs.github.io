title: Quickstart Guide for Manipulating Matrix Data in C++ using  Eigen Library
subtitle: Matrix data manipulation and operations using C++ and Eigen library
date: 2018-03-16 07:00 PM
tags: eigen, C++

I recently got a chance to work with Eigen Matrix library for a parallel application. Having used Numpy before, I found that Eigen provides a great interface for matrix manipulation for C++. Although, the syntax can be tricky at first, but for numeric code, you can gain huge productivity boost by eliminating the need to write explicit for-loops for manipulating matrix data. I have put together a quick start 

[Eigen](eigen.tuxfamily.org) is an open source C++ template library, similar to Python’s [Numpy](http://www.numpy.org/), for handling linear algebra operations including manipulation of matrices, vectors, and solving numerical problems. The Eigen library is fast thanks to its utilization of [expression templates ](https://en.wikipedia.org/wiki/Expression_templates) and support of vector instructions.

The expression templates allows it to intelligently remove intermediate temporary variables and enables lazy evaluations. Additionally, it is also very easy to setup and use. As a hear only library, all you need to get started is include the library is inclined. 

I have been using extenWe will use GCC compiler for our examples in this post. 

## Quick Example

Lets dive right in with a quick example of adding two matrices.  

``` C++
#include <Eigen/Dense>
#include <iostream>

// Declare and initialize matrices  
Eigen::MatrixXi A(2, 3);
A <<  1, 1, 1,
      0, 1, 0;

Eigen::MatrixXi B(3, 2);
B << 2, 0,
     3, 0,
     1, 2;

Eigen::MatrixXi C = A + B.transpose();

std::cout<<C<<std::endl;

```

Here we have declared two matrices, *A & B*, initialized them with some data and then added them together. Since the shape of the second matrix *B* is incompatible for addition, we take a transpose of *B* matrix. 

In order to compile this code using GCC compiler, simply download (or clone) the [Eigen headers](https://github.com/eigenteam/eigen-git-mirror) and include that path something like this: 

```shell
g++ -I./<path-to-eigen-dir> -std=c++11 -Wall -g -fPIC  -c example.cpp -o example
```


## The Matrix Class

The main class for most linear algebra operations is *Matrix*. It is a template class taking up to six arguments that specify the data type, size and storage layout. 

```C++
Matrix<typename Scalar,        // Data Type e.g int, float double
       int RowsAtCompileTime,  // umber of Rows
       int ColsAtCompileTime,  // Number of 
       int Options = 0,        // Options such as RowMajor,  ColMajor etc. 
       int MaxRowsAtCompileTime = RowsAtCompileTime,
       int MaxColsAtCompileTime = ColsAtCompileTime>

```

So, in order to declare a *4x4* matrix that will hold integer values, we can do it something like this:

```C++
Matrix<int, 4, 4> m;
```

However, the Eigen library have provided a lot of convenience typedefs to make it easier to declare common case matrices. Instead of the above  syntax, we can use *Matrix4i* to declare a *4x4* integer matrix. This is particularly typedef as follows: 

```C++
typedef Matrix<int, 4, 4> Matrix4i;
```

Eigen defines the following Matrix typdefs:

```C++
1. typedef Matrix<type, N, N> MatrixNt
2. typedef Matrix<type, N, 1> VectorNt
3. typedef Matrix<type, 1, N> RowVectorNt
```

where: 

* N can be any of 2, 3, 4, or X for Dynamic (Explained next)
* t can be any of i (int), f (float), d (double). There are additional options defined for complex types as well. 

##Dynamic Size Matrices

The size of the matrix  doesn't have to be known at the compile time. You can define A dynamic matrix  using one of the typedef'd  type. Here is a code example showing declaration of dynamically allocated integer matrices. The first one is initialized using random values, the second one using the Eigen's comma initializer syntax.  

```C++
MatrixXi A = MatrixXi::Random(4, 5);
Eigen::MatrixXi A(2, 3);
A <<  5, 6, 7,
      8, 9, 10;
```

The fixed sized matrices - *Matrix4i* is 

##Basic Operations

Eigen supports a variety of basic arithmetic operations. The Matrix class provides overloaded arithmetic operators that only supports linear-algebra operations. The element-wise or other mixed operations can be performed by the Array class. 

```C++
Eigen::Matrix3f A;
A << 4, 7, 5,
   8, 9, 1,
   2, 6, 0;

Eigen::MatrixXf B(3, 3);
// Matrix of all ones. 
B.setOnes();

Eigen::MatrixXf C;

C = A + B;
C = A - B;
C = A * B;

```


Similarly, you can multiply and divide by a scalar variable:

```C++
  Eigen::MatrixXf A (2, 2);
  A << 4, 7,
       8, 9;

  // Scale the matrix values by 2. 
  Eigen::MatrixXf C = A * 2;
  // Same as above without assigning the values to an additional Matrix. 
  A *= 0.5;
```

All operations involving vectors are just the special case of *Nx1* matrix. You can multiply a matrix with a vector as long as the rules of matrix-vector multiplication are meet. 

```C++
Eigen::Matrix2f A;
A << 4, 7,
   8, 9;

Eigen::Vector2f B(2, 1);
Eigen::Vector2f C(0, 3);


cout <<" A * B\n"<<(A * B)<<endl;
cout << "Vector * Vector"<<B.transpose() * C<<endl;
}
```

You can also easily compute the sum, product or max/min element of a matrix:

```C++
Eigen::Matrix3f A;
A << 1 , 9, 12,
   14, 7, 8,
   6 , 4, 9;

cout << "A\n" <<A<<endl;
cout << "Sum of A = " <<A.sum()<<endl;
cout << "Max of A = " <<A.maxCoeff()<<endl;
cout << "Min of A = " <<A.minCoeff()<<endl;
cout << "Sum of diagonal elements = " <<A.trace()<<endl;

```

##The Array Class

The support for co-efficient wise operations in Eigen is offered by the Array class. This class is very similar in declaration to the *Matrix* class. As a template class it offers similar option and comes with a variety of typedef'd types for further convenience. 


```C++
Array<typename Scalar, int RowsAtCompileTime, int ColsAtCompileTime>
``` 

Eigen use the typedef notation of *ArrayNt* for 1-dimensional arrays. The multi-dimensional arrays are defined as *ArrayXXt*, where the *XX* specify dimensions and *t* is used for data type. Here is an exmaple of declaring two 2-D arrays and then multiplying them together. Here instead of matrix-matrix multiplicaiton, the elements of the array are multiplied using coefficient wise. 


```C++
Eigen::Array22d;
A << 1, 4,
   8, 9;

Eigen::ArrayXXd B(2, 2);
B << 2, 5,
     1, 3;

cout << "Array A \n" << A <<endl;
cout << "Array B \n" << B <<endl;
cout << "Element wise multiplication of A * B\n" << (A * B)<<endl;

```

