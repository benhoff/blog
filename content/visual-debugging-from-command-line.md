Title: Visual Debugging from the Command Line
Date: 2019-11-24 22:39
Category: Other
Slug: command-line-visual-debugging
Authors: Ben Hoff
Summary: How to visually debug something from the command line

Working with images is interesting. In a previous piece of work, a customer wanted to bring in some semantic segmentation. Semantic Segmentation goes pixel by pixel and assigns probabilities that the pixel belongs to label. You'll typically see this in street images, with individual cars, people, bikes, etc being segmented out of the overall picture on a pixel level.

The interesting problem of working with semantic segmentation technologies is working with the outputs. Typically the output of a semantic segmentation model is a list of pixel probabilities. Because it's a pixel-by-pixel technology, you end up with probabilities for every single pixel in an image. Combine that with an estimation for each type of class that a pixel can be, and every pixel in an 800 x 600 image suddenly has 50 probabilities associated with it.

(There's some tech where they use the bounding box to limit the number of pixels passed back (Mask RCNN), but it's still a lot of data to work with.)

I'm not sure I've ever figured out a good way to work with multi-layered array data like that contained within pictures. Leave a comment below if you have any hints.

Since I was working with images though, the nice thing is that you can just, you know, _display_ the images. After much trail and error, that was the best way I could figure out how to actually iteratively develop semantic segmentation code. 

Interestingly, I've never much cared for how OpenCv handles windows until know.

``` python
# Note that `some_numpy_array` is just that, a numpy array

# Visualize the array or image
cv2.imshow('My Array', some_numpy_array)
# wait until user presses keys
# Note that without this waitkeys, the window will be created and destroyed before you can notice it
cv2.waitKeys()

# Do some kind of manipulation here or you could show another picture to compare
some_numpy_array = do_some_action(some_numpy_array)

# Visualize the array or image again after the changes
cv2.imshow('My Array', some_numpy_array)
cv2.waitKeys()
```

The method cv2.destroyAllWindows() or cv2.destroyWindow('your-name-here') might be useful depending on the specifics of what you have to visualize. I just reused the existing context/window, but there might be cases where you'd want to display multiple windows side-by-side or some other setup.

This was a funny setup because I was actually building some server code. So as I was debugging, my web server started spitting some Desktop Graphical User Interfaces. While none of this code made it into production, it definitely helped me track down the logic errors in my code and get the result [submitted up and working correctly](https://github.com/opencv/cvat/commit/a435b410ede92130ca2bc67a7ae2a60962f6ebef).
