Title: Tensorflow Serving is Dead
Date: 2019-12-11 07:50
Category: Other
Slug: tensorflow-serving-dead
Authors: Ben Hoff
Summary: Tensorflow Serving is Dead, or at least not being maintained

As part of my OpenCV CVAT development, one of the things that I want to focus on is making it easier to develop computer vision models within the platform. There's quite a few startups that are also working in this space, but the idea of crowdsourcing labeling/annotation in a single platform and then using that same platform to integrate and train a machine learning model, is powerful. It's the vision I was working towards with my last company, and still an interesting one.

As part of that vision, the CVAT platform needs to integrate in some of the top tier machine learning frameworks. CVAT has already integrated in OpenVINO (which is an Intel Deep Learning framework. Actually hilariously, OpenVINO is rebranded [DLDT](https://github.com/opencv/dldt)). But the next obvious enterprise framework is Tensorflow.

One important thing from a systems perspective is to separate out your resources, so you don't risk breaking your entire system and you can scale different pieces at different rates. So the model integration really needed to be of the microservices brand. Enter stage left: Tensorflow serving.

There's only one slight hangup. Tensorflow has recently transitioned into Tensorflow 2.0, an API breaking upgrade. This has (as API breaks always do), thrown the entire ecosystem into chaos. But it has shown some light on an interesting thing.

Tensorflow Serving is Dead. Or at least, not being actively maintained.

See part of the upgrades to Tensorflow 2.0 was to remove the `contrib` module, a top level module that used a very popular Tensorflow library known as Slim. This breaks Tensorflow Serving's examples. See [here](https://github.com/tensorflow/serving/issues/1475). No big deal though, software is flexible and can heal right? Well, only if you keep development resources on the project. Two perspective pull fixes, both [one of mine](https://github.com/tensorflow/serving/pull/1477) and [someone else's](https://github.com/tensorflow/serving/pull/1486) have gone unmerged or commented for 30+ days. The last pull request accepted was September 11th, 2019.

So Tensorflow Serving is officially dead. Or at least unmaintained at this point.
