title: Matrix Manipulations in C++ using Eigen Library
description: A quick start guide for working with matrices and linear algebra operations in C++ using the Eigen library. The Eigen is a fast and highly optimized library. The use of expression templates allow it to intelligently remove temporary variables avoiding unnecessary copying of data. The explicit vectorization greatly speed-up certain numeric operation on a variety of platforms. 
date: 2018-06-20 07:00 PM
tags: eigen, C++
cover_image: /images/eigen_introduciton_part1/the_matrix.jpg

[Eigen](eigen.tuxfamily.org){:target="_blank"} is an open source C++ library optimized for handling numeric operations such as addition, subtraction, multiplication etc. of matrices and arrays along with solving linear systems.  Eigen is feature rich and highly optimized. It offers explicit vectorized instruction for multiple platforms. Its use of [C++ expression templates](https://en.wikipedia.org/wiki/Expression_templates){:target="_blank"} allow it to intelligently avoid temporary variables and enable lazy evaluation. The library is very similar in function to the popular Python's [Numpy](http://www.numpy.org/){:target="_blank"}.

Although, the syntax can be a bit tricky at first, but for numeric code, you can gain huge productivity boost by eliminating the need to write explicit for-loops for manipulating matrix or numeric array data. Additionally, you can benefit from its parallel support to speed-up certain operations. 

Here is a quick guide to get you started. 

## Quick Example

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

Here we have declared two matrices, *A & B*, initialized them with some values, using comma value initialization, and then added them up together. Since the shape of the second matrix *B* is incompatible for addition, we added a transpose of it. 

In order to compile this code using GCC compiler, simply download (or clone) the [Eigen headers](https://github.com/eigenteam/eigen-git-mirror) and include them into path:

```shell

g++ -I./<path-to-eigen-dir> -std=c++11 -Wall -O3 -fPIC  -c example.cpp -o example

```


## The Matrix Class

Most of linear algebra operations, in Eigen, are carried through the template class - *Matrix*. It has six arguments for the template, where first three are required. These arguments specify the type, size and storage layout among other configurations. 


```C++

Matrix<typename Scalar,        // Data Type e.g int, float double
       int RowsAtCompileTime,  // umber of Rows at compile time or Dynamic for variable size rows
       int ColsAtCompileTime,  // Number of Columns at compile time or Dynamic for variable size cols.
       int Options = 0,        // Options such as RowMajor,  ColMajor etc. 
       int MaxRowsAtCompileTime =  RowsAtCompileTime, // By default same as rows at compile time. 
       int MaxColsAtCompileTime =  ColsAtCompileTime, // By default same as cols at compile time. 
       >
       
```

Using the template argument, We can declare a *4x4* matrix as follows:

```C++

Matrix<int, 4, 4> A;

```

The scalar type is integer and number of rows and columns are fixed as 4. Instead of typing the full template syntax, we can use  the built-in typedef'd types. So instead of the above syntax, we can just say...

```C++
Matrix4i A;
```

.. by using the following typedef type provided in the library. 


```C++

typedef Matrix<int, 4, 4> Matrix4i;

```

There are a whole lot of these convenient types defined in the library and they follow the following general forma:

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

Whenever you have a choice between dynamic or fixed size Matrix, the fixed size one will typically be more optimized. The fixed size matrices avoids dynamic memory allocation and are further optimized using [loop unrolling](https://en.wikipedia.org/wiki/Loop_unrolling){:target="_blank"}. 

##The Array Class

The multiplication, division and similar operations offered by the *Matrix* class are done following the linear algebra rules. In order to use co-efficient (or element-wise) operations, we have to use the the *Array* class. This class is very similar in declaration to the *Matrix* class. 

```C++
Array<typename Scalar, int RowsAtCompileTime, int ColsAtCompileTime>
``` 

Just like in the case of the *Matrix class*, we can use the typedef notations of *ArrayNt* for 1-dimensional arrays. The multi-dimensional arrays are defined as *ArrayXXt*, where the *XX* specify the dimensions and *t* is used for data type. As an example consider defining two 2-D arrays and then multiplying them together. Here multiplication will take place element wise. 


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

### Array Interface to Matrix

Instead of explicitly defining an *Array* object for element-wise operations, we have the option of using the array interface of an existing *Matrix* objects to do mix types of operations. 

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

We have already seen few examples of initializing a matrix using comma separated values. 

```C++
Eigen::Matrix3f A;
A << 1 , 9, 12,
    14, 7, 8,
    6 , 4, 9;
```

There are few additional methods.

### Special Matrices and Arrays

Another way to initialize matrices and arrays is using the static methods like *Zero()* , *Ones()*, *Identity()* or *Random()*. 

```C++
Matrix2f A = ArrayXXf::Zero(2, 2);
cout<<A<<endl;    // 0 0
				   //	0 0
 
Matrix3f B = Matrix3f::Zero(3, 3);
cout<<B<<endl;     // 0 0 0
				   // 0 0 0
				   // 0 0 0

Matrix3f C = Matrix3f::Ones(3, 3);
cout<<C<<endl;    // 1 1 1
				  // 1 1 1
				  // 1 1 1

```
The **Random()** method will fill the matrix or array with random coefficients. Similarly the static method **Constant(value)** sets all the coefficients to the *value*.

### Using existing data. 

The raw C/C++ buffers can be interfaced with Eigen using the **Map** class. The Map object has a type defined as:


```C++
Map<Matrix<typename Scalar, int RowsAtCompileTime, int ColsAtCompileTime> > 
```

The main argument supplied to the *Map*'s' template is of type **Eigen::Matrix**. Thus, the data type and number of elements in the buffer being interfaced should match the supplied matrix type. 

In the example below we interface an integer array of length 9 to 3 by 3 matrix.

```C++
int data[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

cout<<"Column Major 3 by 3 Matrix"<<endl;
Map<Matrix<int, 3, 3>> A(data, 3, 3);
cout<<A<<endl; 		// 1 4 7
				 	//2 5 8
					//3 6 9
```

By default the Eigen library uses column-major order to process the data within the raw buffer. However this can be changed by explicitly specifying the storage order of the underlying Matrix. 

```C++
cout<<"Row Major 3 by 3 Matrix"<<endl;
Map<Matrix<int, 3, 3, RowMajor>> B(data);
cout<<B<<endl;	           //1 2 3
					     //4 5 6
					     //7 8 9

```

An additional argument to the Map is the **Stride**. The stride offers further control over the layout of the data being processed from the raw buffer. For example, in the following example, we are skipping over an element while interfacing with the raw buffer.

```C++
  int data[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};

  Map<Matrix<int, 3, 2>, 0, Stride<6, 2>> A(data);
  cout<<A<<endl; 	    // 1  7
						// 3  9
						// 5 11
```

The *Stride* class has two parameters: (i) OuterStrideAtComileTime (value 6 above) and (ii) InnerStrideAtCompileTime (value 2 above). 

The **inner stride** controls how many elements to skip between two consecutive entries within a given column (row) for column-major (row-major) matrix. 

The **outer stride** specifies the increment between two consecutive columns (rows) of a column-major (row-major) matrix. 

In the example above, we used an outer stride of 6 and an inner stride of 2. The outer stride of 6 will skip over 6 elements between each column. More specifically, the first column will start at the first  elements and the second column will start at the 7th element. The inner stride of 2 means that we want to skip an element within the consecutive elements of a given column. 

The figure below show this example visually using both column-major and row-major order. 

![post](/images/eigen_introduciton_part1/strides_example1.png)


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
//  that follow linear algebraic rules are supported by the Matrix class. 

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

In addition to above few examples, there are many other [supported operation](http://eigen.tuxfamily.org/dox/group__TutorialMatrixArithmetic.html){:target="_blank"}. Many of these operations can also be applied to a portion of the matrix or array using block operations. 

##Block Operations

Eigen offers operations that can be used to manipulate or extract just a portion of a matrix or array. These block expressions can  either be used as *rvalues* or as *lvalues*. The **block(i, j, p, q)** operation allows us to specify a rectangular block of size *p by q* starting at position *i* and *j*. 

```C++

cout<<"Block of size 2, 2 starting at 1, 1\n"<<A.block(1, 1, 2, 2)<<endl;

```

Similarly, individual rows and cols of an array or matrix can be manipulated as a special case of block operations, using *row(i)* or *col(i)* expressions. 

```C++

cout<<"Row 1 of the Matrix A.row(0)\n"<<A.row(0)<<endl;

A.row(0) = A.row(0) * 3;

cout<<"A.row(0)*3\n"<<A<<endl;

```
Check out the official documentation for more [examples](http://eigen.tuxfamily.org/dox-3.2/group__TutorialBlockOperations.html){:target="_blank"} of block operations. 

##Slicing

There is no direct support for slicing in Eigen as yet. If you are familiar with Numpy, slicing is a very handy feature. However, we can use the **Map** class to mimic this feature. The *data()* interface of a matrix or array gives us direct access (pointer) to the the underlying storage of the matrix class and combining that with *Map*, we can slice the data in any way. 

Lets look at few examples of slicing columns of an existing matrix. 


```C++
Matrix4i A;
A << 1, 2, 3, 4,
     5, 6, 7, 8,
     9, 10, 11, 12,
     13, 14, 15, 16;
cout<<"Original Matrix \n"<<A<<endl;

// Using the raw pointer to underlying storage, we can use the Map class to slice a matrix.  
Map<MatrixXi> B(A.data(), 4, 2);

cout<<"Slicing first two columns \n"<<B<<endl;//  1  2
                                              //  5  6
                                              //  9 10
                                              // 13 14
// Some pointer arithmetic to skip the first eight values (two columns). 
Map<MatrixXi> C(A.data()+8, 4, 2);
cout<<"Slicing last two columns \n"<<C<<endl; //  3  4
                                              //  7  8
                                              // 11 12
                                              // 15 16

```

Similarly, we can pair the *Map* with the *Stride* for more complex options of slicing. For example, the following code, will fetch the first and third column from above Matrix A. 

```C++
Map<MatrixXi, 0, OuterStride<8>> B(A.data(), 4, 2);

// Or

Map<MatrixXi, 0, OuterStride<>> B(A.data(), 4, 2, OuterStride<>(8)

```

Here, we have used the **OuterStride** interface with the stride value of 8. The *OuterStride* and similarly *InnerStride* are convenient specialization classes of *Stride* with the one of the value set to 0. For instance, the *OuterStride* is same as using *```Stride <Value, 0>```*. 

Few examples of slicing rows:

```C++

// Slicing first two rows. 
Map<MatrixXi, 0, OuterStride<4>>(A.data(), 2, 4)// 1 2 3 4
                                                // 5 6 7 8

// Slicing first and third row. 
Map<MatrixXi, 0, Stride<4, 2>>(A.data(), 2, 4) // 1  2  3  4
                                               // 9 10 11 12

```


##Broadcasting

Broadcasting is the idea of constructing an intermediate representation of a vector by replicating its entries in one direction (rows or columns) such that it is possible to perform an operation on a different sized matrix. Eigen supports broadcasting.  Here is a simple example of adding a vector to the matrix. 

```C++
int data[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

Map<Matrix3i> A(data);
cout<<"Matrix A \n"<<A<<endl; // 1 4 7
                              // 2 5 8
                              // 3 6 9

Vector3i B;
B << 4, 5, 6;
cout<<"Vector B\n"<<B<<endl; // 4
                            // 5
                            // 6

//  Broadcast to columns
cout<<A.colwise()+B<<endl;  // 5  8 11
                            // 7 10 13
                            // 9 12 15

// Broadcast to rows 
cout<<A.rowwise()+B.transpose()<<endl; // 5  9 13
                                       // 6 10 14
                                       // 7 11 15

```

##Summary

Eigen is a feature rich library that offers many additional features including support for linear solvers, sparse matrices, and multi-threading through OpenMP to name just the few. In a future post, we will try to cover some of these topics in more detail.  

### Reference ###

- [Code for the Blog](https://github.com/n-log-n/Eigen_Tutorial.git)
- [Official Documentation](http://eigen.tuxfamily.org/dox-3.2/group__TutorialMatrixClass.html)


