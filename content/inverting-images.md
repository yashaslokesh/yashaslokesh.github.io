Title: Inverting the colors of an image
Date: 2019-01-24 20:46
Modified: 2019-01-24 20:46
Category: Python
Tags: python, numpy, pillow
Authors: Yashas Lokesh
Summary: A small tutorial on inverting the color of images with Python

If you ever design a logo or a sprite for a dark background, and are told the logo/sprite will be used on a light background, what do you do? You've spent all this time working on the design, and it might not even fit the theme anymore! 

I faced this problem this last week when I wanted to use a sprite I designed for a black background for a white background instead. With the use of **Numpy** and **Pillow**, I was able to quickly invert the colors in an image with PNG or JPEG formats. Others formats are untested, so far.

Using Pillow, we can open an image by using the `PIL.Image.open()` method. The type of the returned object will depend on the image format passed in, but all of them support an array interface, so we can safely continue. Then, to be able to manipulate all the pixel values in our image, we use the `numpy.array()` function and pass in the opened image.

```python
>>> from PIL import Image
>>> import numpy as np
>>> 
>>> image = Image.open(path)
>>> image_arr = np.array(image)
>>> type(image_arr)
<class 'numpy.ndarray'>
```

The image array we get will have three channels corresponding to the (R, G, B) values of a pixel with one extra channel if the image format includes an alpha layer. How can we check if we have a PNG or JPEG image? We can use `image_arr.shape`. The returned 3-tuple will have the number of channels in the third slot.

```python
>>> image = Image.open('circle.png')
>>> image_arr = np.array(image)
>>> image_arr.shape
(99, 99, 4)
```

Now we have a usable array and we can invert the colors. Mathematically, to invert the color of one pixel, we subtract the pixel's color values from the maximum, 255. If we have a PNG format image, then we have an extra alpha channel that we don't want to modify, or the transparent parts of the image won't be transparent anymore. We can use numpy slice notation to modify all dimensions of the array.

If the number of channels is four, we'll just add the unaltered alpha channel on top of the inverted colors array and create an `Image` with it. An `Image` can be created with the `Image.fromarray()` method.

```python
>>> colors_arr = image_arr[:, :, :3]
>>> invert_col_arr = 255 - colors_arr
>>>
>>> is_png = image_arr.shape[2] == 4
```

One last thing: If we extract the alpha channel, the returned array has a size `(99, 99)`. If we want to stack the alpha channel on top of our inverted colors array, then we have to use the `numpy.dstack` function. With all this down, we can finish inverting our image:

```python
>>> if is_png:
...     alpha_ch = image_arr[:, :, 3]
...     inverted_arr = numpy.dstack((colors_arr, alpha_ch))
... else:
...     inverted_arr = colors_arr
...
>>> inverted_img = Image.fromarray(inverted_arr)
>>> Image.show()
```

I ran this code on a PNG image to test, turned this (there's a white circle in the middle there) ![original circle][regular] into this ![inverted circle][inverted]. 

Thanks for reading, I hope you learned how to use `Pillow` and `Numpy` to invert image colors without any external software. If you have any comments, questions, or suggestions, feel free to contact me on [Twitter](https://twitter.com/yashaslokesh_).

[regular]: images/shooter.png "Circle Shooter"
[inverted]: images/shooter-inv.png "Inverted Circle Shooter"
