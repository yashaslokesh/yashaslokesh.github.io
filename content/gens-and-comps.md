Title: Generator Expressions and List Comprehensions
Date: 2019-01-08 08:46
Modified: 2019-01-08 08:46
Category: Python
Tags: python
Authors: Yashas Lokesh
Summary: We learn about generator expressions and list comprehensions, useful ways to create iterators and lists, respectively.

Generator expressions and list comprehensions are functional programming tools that are very useful in creating iterators and lists, respectively.

If we want to create a list, we can just use the square bracket notation or the **list()** constructor. Lists can store any data values. If we want to create a list of the squares of numbers below 10, we can just add to the list:

```python
>>> a_list = ['This is a list element', 'and so is this one', 1, 2, 3, ['inner list!']]
>>>
>>> squares = []
>>> for num in range(10):
...     squares.append(num ** 2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

List comprehensions provide a more readable way to create lists. We can use it to create a list of the first 10 numbers, only even numbers, or only include numbers that satisfy some other requirement. Here's a way to create a list of all numbers under 20, and then all numbers below 20:

```python
>>> numbers = [num for num in range(20)]
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>>
>>> evens_under_twenty = [num for num in range(20) if num % 2 == 0]
>>> evens_under_twenty
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Here we see two basic syntax structures for creating list comprehensions. We can use **i for i in iterable**, where **iterable** is a generator, list, string, or some other iterable. You can check if an object is iterable by checking for the **__iter__()** magic method, and these are two ways to do it:

```python
>>> '__iter__' in dir(range)
True
>>> hasattr(range, '__iter__')
True
```

You can also make list comprehensions with the **if...else** pattern as many times as needed:

```python
>>> bool_evens = [True if num % 2 == 0 else False for num in range(10)]
>>> bool_evens
[True, False, True, False, True, False, True, False, True, False]
>>> 
>>> numbers = [num for num in range(10)]
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> divide_list = ['div by 2' if num % 2 == 0 else 'div by 3' if num % 3 == 0 else num for num in numbers]
>>> divide_list
['div by 2', 1, 'div by 2', 'div by 3', 'div by 2', 5, 'div by 2', 7, 'div by 2', 'div by 3']
```

Generator expressions are created the same way as list comprehensions but with parentheses around the expression instead of square brackets. To get all of the elements in the generator, you can iterate over it. When you want to create a list to iterate over, generator expressions can be used instead for an increase in performance. The increase in performance comes from not storing all of the elements in the iterable beforehand. The generator expression supplies elements as the iterator asks for them.

```python
>>> evens_gen = (num for num in range(20) if num % 2 == 0)
>>> evens_gen
<generator object <genexpr> at 0x103daf5e8>
>>>
>>> sum = 0
>>> for num in evens_gen:
...     sum += num
...
>>> sum
90
```

If you want to create dictionaries or sets using these expressions, you can! Here are some examples:

```python
>>> num_set = {num for num in range(10)}
>>> num_set
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>>
>>> num_set.add(6)
>>> num_set
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>>
>>> num_dict = {num : str(num) for num in range(10)}
>>> num_dict
{0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
```

The difference between set and dictionary comprehensions is that dictionary comprehensions have a **key:value** pair as the element you're inserting into the dictionary. Both set and dictionary comprehensions use curly braces instead of square brackets or parentheses.

Make sure not to use these expressions for a side-effect. These expressions should be used to create iterables. If you wanted to print out all even numbers below 10, you should use a for loop instead of a generator or a list:

```python
# Use this:
for num in range(10):
    if num % 2 == 0
        print(num)

# Instead of this:
[print(num) for num in range(10) if num % 2 == 0]
```

It can be memory-expensive to create a large list, and if you're only using the list for its side-effects, then the list is thrown away after you create it and you potentially lost a lot of performance speed creating the intermediate list.

Thanks for reading! If you have any comments, questions, or suggestions for improvement, feel free to contact me on [Twitter](https://twitter.com/yashaslokesh_).


