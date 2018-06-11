title: Matrix Manipulations using C++ Eigen Library
subtitle: Matrix data manipulation and operations using C++ and Eigen library
date: 2018-03-16 07:00 PM
tags: eigen, C++
cover_image: /images/eigen_introduciton_part1/abstract-access-close-up-1089438.jpg

[Eigen](eigen.tuxfamily.org) is an open source C++ library for handling linear algebra operations such as matrix and vector manipulation and solving linear algebra problems.  The library is very similar in function to popular Python's Numpy [Numpy](http://www.numpy.org/). It also offers a lot of nifty optimization including support for vectorized insturction and elimination of temporary variable because of its use of using [C++ expression templates](https://en.wikipedia.org/wiki/Expression_templates). Although, the syntax can be a bit tricky at first, but for numeric code, you can gain huge productivity boost by eliminating the need to write explicit for-loops for manipulating matrix data. Here is a small how-tos to quickly get started with the library. 

## Quick Example

Lets dig right in..


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

Here we have declared two matrices, *A & B*, initialized them with some value and then added them up together. Since the shape of the second matrix *B* is incompatible for addition, we had to take a transpose of *B* matrix. 

In order to compile this code using GCC compiler, simply download (or clone) the [Eigen headers](https://github.com/eigenteam/eigen-git-mirror) and include that path,  something like this: 

```shell

g++ -I./<path-to-eigen-dir> -std=c++11 -Wall -O3 -fPIC  -c example.cpp -o example

```


## The Matrix Class

Most of linear algebra operations, in Eigen, are carried through the template class - *Matrix*. It has six arguments for the template, where first three are required. These arguments specify the type, size and storage layout among other configurations. 


```C++

Matrix<typename Scalar,        // Data Type e.g int, float double
       int RowsAtCompileTime,  // umber of Rows at compile time or Dynamic for variable size rows
       int ColsAtCompileTime,  // Number of Columns at copile time or Dynamic for variable size cols.
       int Options = 0,        // Options such as RowMajor,  ColMajor etc. 
       int MaxRowsAtCompileTime = RowsAtCompileTime,
       int MaxColsAtCompileTime = ColsAtCompileTime>
       
```

Using the template argument, We declare a *4x4* matrix as follows:

```C++

Matrix<int, 4, 4> m;

```

However, there is an easy way to avoid the extra typing by making use of the typedef'd types.

```C++

typedef Matrix<int, 4, 4> Matrix4i;

```

There are a bunch of typedef declarations defined in the library. Their general format is:

```C++
1. typedef Matrix<type, N, N> MatrixNt
2. typedef Matrix<type, N, 1> VectorNt
3. typedef Matrix<type, 1, N> RowVectorNt
```

where: 

* N specify the dimensions of the matrix and can be 2, 3, 4, or X for Dynamic (Explained next)
* t is the data-type can be i (int), f (float), d (double). There are additional options defined for complex types as well. 

##Dynamic Size Matrices

So far we have only looked at declaring fixed size matrices. The dynamic size matrices can be declared by either specifying *Dynamic* for the size of the rows/cols as the template argument or using the typedef syntax. 

```C++
int rows = 4;
int cols = 5;
Matrix<int, Dynamic Dynamic> A(rows, cols);

// Or

Eigen::MatrixXi B(2, 3);
B <<  5, 6, 7,
      8, 9, 10;
```

Whenever you have a choice between dynamic or fixed size Matrix, the fixed size one will typically be more optimized. The fixed size matrices avoids dynamic memory allocation and are further optimized using [loop unrolling](https://en.wikipedia.org/wiki/Loop_unrolling). 

##The Array Class

The multiplication, divison and similar operations offered by the *Matrix* class are done following the linear algebra rules. In order to use co-efficient (or element-wise) operations, we have to use the the *Array* class. This class is very similar in declaration to the *Matrix* class. 

```C++
Array<typename Scalar, int RowsAtCompileTime, int ColsAtCompileTime>
``` 

Just like in th case of the *Matrix class*, we can use the typedef notations of *ArrayNt* for 1-dimensional arrays. The multi-dimensional arrays are defined as *ArrayXXt*, where the *XX* specify the dimensions and *t* is used for data type. As an example consider defining two 2-D arrays and then multiplying them together. Here multiplicaiton will take place element wise. 


```C++
Eigen::Array22d;
A << 1, 4,
     8, 9;

Eigen::ArrayXXd B(2, 2);
B << 2, 5,
     1, 3;

cout << "Array A \n" << A <<endl;
cout << "Array B \n" << B <<endl;
cout << "Element wise multiplication of A * B\n" << (A * B)<<endl; // 2 20
                                                                   // 8 27
```

Instead of explicitly defining an *Array* for element-wise operation, we have the option of using the array interface of the *Matrix* class to do mix types of operations. 

```C++
Eigen::MatrixXf Am(2, 2);
Am << 1, 4,
      8, 9;
Eigen::MatrixXf Bm(2, 2);
Bm << 2, 5,
      1, 3;

cout << "Matrix A \n"<<Am<<endl;
cout << "Matrix B \n"<<Am<<endl;
cout << (Am.array() * Bm.array())<<endl;

```

##Initializing Matrix and Array values

### Comma Initializer

We have already seen few examples of initializing a matrix using comma seperated values. 

```C++
Eigen::Matrix3f A;
A << 1 , 9, 12,
   14, 7, 8,
   6 , 4, 9;
```

There are few additional methods. Later, we will also see how to interface existing data to the eigen matrix. 

### Speical Matrices and Arrays

Another way to initialize matrices and arrays is using the static methods like *Zero()* , *Ones()*, or *Identity()*. 

```C++
Matrix2f A = ArrayXXf::Zero(2, 2);
cout<<A<<endl; // 0 0
				 //	 0 0

Matrix3f B = Matrix3f::Zero(3, 3);
cout<<B<<endl;  // 0 0 0
				   // 0 0 0
				   // 0 0 0

Matrix3f C = Matrix3f::Ones(3, 3);
cout<<C<<endl; // 1 1 1
				  // 1 1 1
				  // 1 1 1

```
The *Random()* method will fill the matrix or array with random coefficients. Similary the static method *Constant(value)* sets all the coefficients to value.

### Using existing data. 

A pre-defined numeric array can be used with Eigen either as a vector or matrix. This is done through the **Map** class. 


##Performing Basic Operations

Eigen supports a variety of basic arithmetic operations. The Matrix class provides overloaded arithmetic functions that supports linear-algebra operations. The element-wise or other mixed operations can be performed through the Array interface. 

```C++
Eigen::Matrix3f A;
A << 4, 7, 5,
   8, 9, 1,
   2, 6, 0;

Eigen::MatrixXf B(3, 3);
// Matrix of all ones. 
B.setOnes();

Eigen::MatrixXf C;

// Operations such as matrix-matrix or matrix-vector addition, subtraction, multiplication 
//  that follow linear algebric rules are supported by the Matrix class. 

C = A + B;
C = A - B;
C = A * B;

```

Similarly, we can multiply and divide by a scalar variable:

```C++
Eigen::MatrixXf A (2, 2);
A << 4, 7,
   8, 9;

// Scale the matrix values by 2. 
Eigen::MatrixXf C = A * 2;
// Same as above without assigning the values to an additional Matrix. 
A *= 0.5;
```

All operations involving vectors are just the special case of *Nx1* matrix. You can multiply a matrix with a vector as long as the rules of matrix-vector multiplication are satisfied. 

```C++
Eigen::Matrix2f A;
A << 4, 7,
   8, 9;

Eigen::Vector2f B(2, 1);
Eigen::Vector2f C(0, 3);


cout <<" A * B\n"<<(A * B)<<endl;
cout << "Vector * Vector"<<B.transpose() * C<<endl;

```

We can also compute the sum, product and max/min element of a matrix. 

```C++
Eigen::Matrix3f A;
A << 1 , 9, 12,
   14, 7, 8,
   6 , 4, 9;

cout << "A\n" <<A<<endl;
cout << "Sum of A = " <<A.sum()<<endl;
cout << "Overall Max of A = " <<A.maxCoeff()<<endl;
cout << "Overall Min of A = " <<A.minCoeff()<<endl;
cout<< "Max of A along rows = " <<A.rowwise().maxCoeff().transpose()<<endl;
cout<< "Max of A along cols = " <<A.colwise().maxCoeff()<<endl;
cout<< "Min of A along rows = " <<A.rowwise().minCoeff().transpose()<<endl;
cout<< "Min of A along cols = " <<A.colwise().minCoeff()<<endl;
cout << "Sum of diagonal elements = " <<A.trace()<<endl;

```

In addition to above few examples, there are many other supported operations. Many of these operations can also be applied to a portion of the Matrix or Array Cass. 

Block



### Using existing data





