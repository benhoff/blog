Title: Developing OpenCV's CVAT
Date: 2019-11-24 21:39
Category: CVAT
Slug: developing-cvat
Authors: Ben Hoff
Summary: Summarizing my work up to date with CVAT

As part of a work project, I needed to showcase off some computer vision (specifically, semantic segmentation) capabilities. The client needed to be able to understand both what was technically possibly, but also feel comfortable that it was mature enough to be put into production. I've found that finding open source projects that are being driven by big name players typically gives the required comfort to customers that the tech is mature. Additionally, having a sweet looking and usable user interface that you can drop in to the project day 1 is also very helpful.

Enter CVAT. Intel has recently been trying to flex it's muscle in the deep learning space, making up for the early lead that NVIDIA has taken with CUDA. Intel's approach has been an open source one, leading with a suite of deep learning technologies. I'm a little ignorant on the total depth of all the total tools, but I am now very familiar with CVAT and OpenVINO tool suites.

CVAT is an image annotation platform to be used for training machine learning models. While most image annotation labor is cheap (literally drawing boxes on a static image), there's always a desire to leverage existing work to increase the accuracy, speed, and reduce costs in annotation labor.

To do this, CVAT integrates open source pretrained models to act as "first-pass" annotators using the OpenVINO toolkit.

OpenVINO is an abstracting layer between multiple toolkits, allowing one to use both PyTorch, ONNX, and Tensorflow models in a uniform way. (There's also some optimizations it uses to abstract between CPU and GPU power, but that's less important for this use case).

CVAT was perfect for my needs. Someone else had already built the user interface, I just needed to customize a bit of the OpenVINO code base to showcase what was possible for my client. Well, that was the theory.

In reality, the integration between the web server and the deep learning hadn't had much main stream development support. So while what I wanted to do was theoretically easy, it actually took significant development support to make it possible.

In addition to a few bugs that had to be fixed, the biggest technical contributions I had to do, were quite  odd. Users were required to submit Python scripts to process the results of each model back into a format that CVAT understood. The architects of the code that I was using had set up a limited python sandbox to process this user submitted code. When I first started, there was no way for a user to get the full power of the python language , even if you were an admin. This was obviously not going to work for me. So the first thing I did was fix that. [I added a flag to check if a user was a admin or not and gave them the capability to run all of python if they were an admin](https://github.com/opencv/cvat/commit/f20698921e5355a4b13c4f90612163f56b9835d0). That fixed the majority of my issues, but I still didn't have the full power of Python behind me. Because Python's eval does not actually process import statements.

So the second thing I had to do was add in the capability to import code in these user-submitted scripts. In order to do that, I would have to programmatically assess and import the required packages before running the "eval" statement.

I originally thought that setting up this process was going to be too difficult. However, I did remember that Python has actually exposed a significant amount of it's code processing in the standard library, and that gave me hope. With the help of a [StackOverflow question](https://stackoverflow.com/questions/9008451/python-easy-way-to-read-all-import-statements-from-py-module), I found out that I could indeed quickly parse out the import statements using Python's "ast" library. The only thing left to do was to [parse the import statements and dynamically import the code, before evaluating the code](https://github.com/opencv/cvat/commit/418cdbe1464a06d5d7b26e6385586a2e5cfa12a5).

The most technically impressive peace of this actually ended up being the easiest due to the above linked StackOverflow question (minus the research to get there). Tracing through the code base to manually ensure admin checks were put in place (my first patch) took significantly to ensure everything was in correctly. Grokking code completely and dealing with permissions is difficult, and will always probably be.

However, with the capability to showcase off semantic segmentation in a fully featured web interface, my customer was convinced of the readiness of the technology. Sadly, I left the company before I was able to get the contract in place. I did have a lot of fun building out the tech!
