Title: Project Euler Problem #125
Date: 2018-12-31 11:58
Modified: 2018-12-31 11:58
Category: Python
Tags: python, math
Authors: Yashas Lokesh
Status: published
Summary: Solving [Project Euler's problem #125](https://projecteuler.net/problem=125)

Here's the [problem link](https://projecteuler.net/problem=125).

If you haven't attempted solving this problem, yet, go try it first!!

The problem wants us to find the sum of all palindromic numbers which can be written as the sum of consecutive squares of integers, under 10 million. This range is small enough that we don't have to do any optimizations, so I brute-forced the search.

A palindromic number is such that when its reversed, it's still the same number. Some examples: 1, 121, 595, 67876, 923329. Since we'll be computing the sum of squares of integers, we need an upper limit for the integers, which will be the square root of our limit: 10 thousand. 10 thousand squared will be exactly the limit, so we will go upto 10 thousand in our integer ranges. We're not counting 1 because the problem states that we're only concerned with the squares of positive integers.

So we'll go with **i = 1..9,999** and create a new variable for summing up the squares of consecutive integers. This new variable will start with the value **i\*\*2**. Then, we make another loop inside this loop, going with **j = i+1..9,999**. We start with **i+1** for **j** so that we start with the square of the next consecutive integer. Then we can add **j\*\*2** to our temporary sum. There *is* still a possibility that we will go over the limit with our temporary sum, like with:

$$
9,999^2 + 9,998^2 = 199940005
$$

An extreme example, but it illustrates the need for an extra limit-check. Let's add in a check for if our temporary sum is greater than the limit; if it is, we'll exit the inner loop and continue with a new start integer for our temporary sum.

Here's what our code looks like so far:
<script src="https://gist.github.com/yashaslokesh/73a32aed50c87bda7d739e9284467056.js"></script>

Okay, now we'll be generating all numbers which are sums of squares of consecutive integers. This is where we check if the number is a palindrome! Python makes this extremely easy with their slice objects syntax. Any **str** type in Python is an iterable, so we can use the syntax **iterable\[start:stop:step\]** to reverse a string: **string\[::-1\]**. We omit the start and stop, so the whole string is included, and then we use **-1** as the step size, which will reverse the string, then, we can check if the number is a palindrome by first converting it to a string, and then comparing this string to its reversed version. If they equal, then we have a palindrome.

If the candidate number is indeed a palindrome, then we have to add it to the overall sum we're trying to find. Recall: the sum of palindromic numbers which, in turn, can be written as the sum of squares of consecutive integers. So let's make a **result_sum = 0** that we'll add to if a number is a palindrome.

Here's the updated code:
<script src="https://gist.github.com/yashaslokesh/4ed6d1e48b6143d19f26c9cd96ca59c8.js"></script>

The last if-statement is ugly, so we'll turn it into a function to make our code cleaner and easier to read:
<script src="https://gist.github.com/yashaslokesh/a8fe484a57bab4d18db150f7f68f0dc7.js"></script>

There's still one case we haven't considered: what if two different sums turn out to be the same? This has an easy fix, let's keep track of every number. We could use a list or a set.

In the case of a list, we add the temporary sum to the result sum if and only if the temporary sum is not in the list and the temporary sum is a palindrome. Otherwise, we can just continue the inner loop without any special case handling. If we want to use a set, we know that a set contains only unique elements. With a set, we know that the sum of all the elements in the final set will be the answer we're looking for, so we wouldn't need a result sum in this case. I've included both cases below:

<script src="https://gist.github.com/yashaslokesh/be8bd509220b9b7fbe7d66dc5fa47a6d.js"></script>

Running either function gives the correct answer, as verified by Project Euler: **2906969179**.

Thanks for reading! If you have any comments, questions, or suggestions for improvement, feel free to reach out to me on [Twitter](https://twitter.com/yashaslokesh_) or on [GitHub](https://github.com/yashaslokesh).