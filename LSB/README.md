# LSB Method

## What is a digital image?

Ok, now that we know the basics of steganography, let’s learn some simple image processing concepts.

Before understanding how can we hide an image inside another, we need to understand what a digital image is.

We can describe a **digital image** as a finite set of digital values, called pixels. Pixels are the smallest individual element of an image, holding values that represent the brightness of a given color at any specific point. So we can think of an image as a matrix (or a two-dimensional array) of pixels which contains a fixed number of rows and columns.

![](https://cdn-images-1.medium.com/max/2000/1*-Vreo05sajRL8dRibXIWXA.png)

When using the “**digital image**” term here, we are referencing to the “**raster graphics**”, which are basically a dot matrix data structure, representing a grid of pixels, which in turn can be stored in image files with varying formats. You can read more about [digital images](https://en.wikipedia.org/wiki/Digital_image), [raster graphics](https://en.wikipedia.org/wiki/Raster_graphics), and [bitmaps](https://en.wikipedia.org/wiki/Bitmap) at the [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) website.

## Pixel concept and color models

As already mentioned, pixels are the smallest individual element of an image. So, each pixel is a sample of an original image. It means, more samples provide more accurate representations of the original. The [intensity](https://en.wikipedia.org/wiki/Intensity_(physics)) of each pixel is variable. In color imaging systems, a color is typically represented by three or four component intensities such as [red, green, and blue](https://en.wikipedia.org/wiki/RGB_color_model), or [cyan, magenta, yellow, and black](https://en.wikipedia.org/wiki/CMYK_color_model).

Here, we will work with the [RGB color model](https://en.wikipedia.org/wiki/RGB_color_model). As you can imagine, the RGB color model has 3 channels, red, green and blue.
> The **RGB color model** is an additive [color model](https://en.wikipedia.org/wiki/Color_model) in which red, green and blue light are added together in various ways to reproduce a broad array of colors. The name of the model comes from the initials of the three additive primary colors, red, green, and blue. The main purpose of the RGB color model is for the sensing, representation and display of images in electronic systems, such as televisions and computers, though it has also been used in conventional [photography](https://en.wikipedia.org/wiki/Photography).

![](https://cdn-images-1.medium.com/max/2000/1*tcTa2Cst3FXkDpxTg-_1mA.jpeg)

So, each pixel from the image is composed of 3 values (red, green, blue) which are [8-bit](https://en.wikipedia.org/wiki/8-bit) values (the range is 0–255).

![](https://cdn-images-1.medium.com/max/2000/1*Mt3yDPhS3aq_spPfWTW9BA.png)

As we can see in the image above, for each pixel we have three values, which can be represented in [binary code](https://en.wikipedia.org/wiki/Binary_code) (the computer language).

When working with binary codes, we have more significant bits and less significant bits, as you can see in the image below.

![](https://cdn-images-1.medium.com/max/2000/1*YQGZLBpDn2U9Bu8sZphzXQ.jpeg)

The **leftmost** bit is the **most significant bit**. If we change the leftmost bit it will have a large impact on the final value. For example, if we change the leftmost bit from **1** to **0** (**11111111** to **01111111**) it will change the decimal value from **255** to **127**.

On the other hand, the **rightmost** bit is the **least significant bit**. If we change the rightmost bit it will have less impact on the final value. For example, if we change the leftmost bit from **1** to **0** (**11111111** to **11111110**) it will change the decimal value from **255** to **254**. Note that the rightmost bit will change only 1 in a range of 256 (it represents less than 1%).

**Summarizing:** each pixel has three values (RGB), each RGB value is 8-bit (it means we can store 8 binary values) and the rightmost bits are least significant. So, if we change the rightmost bits it will have a small visual impact on the final image. This is the steganography key to hide an image inside another. Change the least significant bits from an image and include the most significant bits from the other image.

![](https://cdn-images-1.medium.com/max/2000/1*kpDa0jt6ftSce4b4DQA2MQ.png)

**You can check out the result in the following image**:

The left upper image is the image that will hide the right upper image. The left lower image is the two images merged and the right lower image is the extracted (unmerged) image.

![](https://cdn-images-1.medium.com/max/2000/1*4paRMea_BGeNpJ2VzFGCoA.png)

As you can see in the image above, we lost some image quality in the process, but this does not interfere with image comprehension.
