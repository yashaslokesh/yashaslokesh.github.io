Title: Optimizing Fibonacci Computation
Date: 2018-12-28 08:46
Modified: 2018-12-28 08:46
Category: Python
Tags: python, algorithms
Authors: Yashas Lokesh
Summary: We go over my linear-algebra inspired algorithms to compute Fibonacci numbers

I posted about this on [Twitter](https://twitter.com/yashaslokesh_/status/1078510658633846785) yesterday.

I've been attempting to study the topic of algorithms this break because one of my classes next semester will cover exactly that. I came upon an MIT series of lectures for a class named "Introduction to Algorithms", and I reached [this video](https://youtu.be/OQ5jsbhAv_M) yesterday on dynamic programming.

The professor says that there is a O(log *n*) algorithm for computing fibonacci numbers, and I'm instantly intrigued. I assumed that O(*n*) was the best that could be accomplished because all of the fibonacci functions we used in our classes were written that way.

I went to [this Wikipedia article](https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form) and started reading.
In particular, they list this formula:
$$
 \begin{pmatrix}
  1 & 1 \\
  1 & 0 \\
 \end{pmatrix}^{n}
=
 \begin{pmatrix}
  F_{n+1} & F_{n} \\
  F_{n}   & F_{n-1} \\
 \end{pmatrix}
$$

I realized that I could use numpy to represent the first matrix, and I could use a loop up to a number *n*, continuously multiplying a resultant matrix with the first matrix above. This is one way to get a O(*n*) algorithm.

Here's the code for a linear fibonacci function. I know numpy has a matrix_power() method, but that method is optimized for calculation and doesn't help to demonstrate the linear runtime of the code below.
<script src="https://gist.github.com/yashaslokesh/604c6343478eea17c5171b386d186008.js"></script>

Now to make the O(log *n*) algorithm. These types of algorithms are usually created by splitting the input in half many times. I chose an arbitrary *n*=10. The exponent rule of  

$$ a^n * a^m = a^{n + m} (1) $$
still applies for matrices. Along this line of logic, if we want to compute the fibonacci matrix for *n*=10, we can multiply two fibonacci matrices of power *n*=5. That is, 

$$ A^5 * A^5 = A^{10} $$

and the second and third entries of the resultant matrix will be our desired fibonacci numbers for *n*=10. Now we have to figure out a way to find the fibonacci matrix for *n*=5. Five isn't divisible by two, so we'll have to use a slightly different method. We know

$$ A^2 * A^2 = A^{4} $$

If we multiply the resultant matrix by our base matrix, then

$$ A^4 * A^1 = A^5 $$

We get the desired matrix! So we now have another rule: if the desired matrix has an odd power, we have to multiply two matrices with floor(n / 2) and then multiply once more by the base matrix.

Now we have to figure out a way to start from the base matrix and go up to our desired matrix. Recursion seemed like the best way forward, but I think writing functions iteratively is easier to read, so I'll do it iteratively.

<script src="https://gist.github.com/yashaslokesh/9eba45c889d61391912fcbd435c805b0.js"></script>

In this script, we put 10 into a list. The base case will be where *n*=1, so we loop and add floor(n / 2) to the list as long as we haven't added one to the end of the list. Here are some examples of what the stack would look like when we finish:

<script src="https://gist.github.com/yashaslokesh/64b97014d59161ce71ecbfb6506852dd.js"></script>

Now we create a matrix *result*. We know all the possible stacks will have a 1 in its last element, so we can just remove it from the stack without losing any information. Now we can process the numbers in the stack. While the stack is not empty, we multiply *result* by itself. If the number we popped from the stack is odd, then we multiply *result* by the base matrix. 

Here's the code for this part:

<script src="https://gist.github.com/yashaslokesh/7d32c618c0956e42264334d8ae3231e0.js"></script>

I wanted to test to see if I implemented these algorithms correctly, so I created another module to time these functions. We can use the **timeit** module to time small code snippets. By default, **timeit** will run the code snippet one million times.

Here's the code for the timing part:

<script src="https://gist.github.com/yashaslokesh/d079ed48dce402a43c7f75c289d93678.js"></script>

The code snippet inside **timeit.timeit()** has to be self-contained. It cannot use any external variables. We can, however, pass in a string containing commands that will setup the environment for the code snippet to work. We can use the **make_setup_string()** function for this purpose.

My final results, as I also posted on Twitter, are shown here:

![Image of the timing results, you can look on Twitter if you can't view it here using the link above.]({static}/images/lower-res-timings.png)

The timing for the linear_fibonacci() function increases by about 28 seconds every increase of 15 to the input, so we accomplished a linear, or O(*n*) algorithm.

The timing for the log_fibonacci() function does not follow this same trend. For *n*=60 and *n*=90, the timings are lower than the next lower value of *n*. Even with the input size increasing linearly, there is not a large change in the timing, so we implemented a correct O(log *n*) algorithm for finding fibonacci numbers.

Thanks for reading! Follow me on Twitter or look at some of my other work on GitHub by clicking on the social links below.