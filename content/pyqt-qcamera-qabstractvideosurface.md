Title: Integrating QCamera and QAbstractVideoSurface Together
Date: 2019-12-10 20:28
Category: PyQt
Slug: qcamera-and-qabstractvideosurface
Authors: Ben Hoff
Summary: Working with a new client to integrate video and desktop together

I had a client approach me about doing a webcam integration user interface, which was great! I've been looking (ITCHING) for a reason to play with Qt's video stack again.

Specifically the last time I left off with my explorations with Qt, I really wanted to integrate an Augmented Reality demo together with a webcamera. I wanted to integrate it with the Qt3D framework to show off the ability to integrate it all. I never could figure out how to do it (see [this Stackoverflow question](https://stackoverflow.com/questions/50291828/how-to-display-an-image-in-qt3d)), but that doesn't mean I had given up the problem.

Being technology greedy, I was also interested in learning how Qt' QVideoFilter classes worked (see [here](https://doc.qt.io/qt-5/qvideofilterrunnable.html)), to create a snapchat clone.

So you know, Augmented Reality, Snapchat, webcam-driven QML application. Just a casual Tuesday for me really.

However I ran into issues getting to the data (and getting Qt3D to display an image as noted above).

So when the client approached me to do an Qt and OpenCV integration, I knew I would finally have my chance to conquer Qt's QCamera class.

Which is exactly what I did.

So the QCamera class has a `setViewfinder` method, where you can set an interface that can work with the raw data. In levels of concereteness to abstraction, the available classes are `QVideoWidget`, `QCameraViefinder` and `QAbstractVideoSurface`. QVideoWidget is a fully featured widget, whereas `QAbstractVideoSurface` is the abstract version ready to be subclassed and implemented.

When you dig through the source code for the more concrete classes, you get exposed to a lot of raw OpenGL. Having done some OpenGL programming before, I kind of know OpenGL, but I'm no expert. Additionally, it's not anything I wanted to introduce into the class I was teaching at the time. So I kind of punted on the whole thing.

Creating a video course takes a lot of time, and I had to abandon any ideas that were too complex for my time frame. I couldn't figure out if the OpenGL implementation made the program significantly more robust, because I couldn't figure out if NOT implementing the program as OpenGL, would force me to download the data out of video memory and push it back up into video memory (a significant battery drainer for a mobile application). I don't think that is the case, but I didn't have time to explore. Luckily for this particular client, everything was on Desktop, so I didn't need to worry about the specific battery constraints.

In order to implement QAbstractVideoSurface, you have to override/implement two methods: `supportedPixelFormats` and `present`. In the `supportedPixelFormats` method, you describe to the rest of the framework which types of QVideoFrame data formats that your implementation can support. My understanding is, if the data comes in a format that you don't explicitly authorize, then the Qt framework uses the underlying system to convert the data into the format that you want.

Again, running on desktop and for a MVP, this wasn't a big concern for me.

Instead, I wanted the system to handle as much of the conversion as possible, so I only exposed a single video format, RGB32.

``` python
class VideoSurface(QtMultimedia.QAbstractVideoSurface):
    def supportedPixelFormats(self, handle_type):
        result = []
        if handle_type == QtMultimedia.QAbstractVideoBuffer.NoHandle:
            result = [QtMultimedia.QVideoFrame.Format_RGB32,]

        return result
```

This leaves only the `present` method. Present is where you actually handle the video data. I wanted to convert the video data into a format that I can use for the rest of my program.

I still find the image data types in Qt to be slightly confusing (I always have to look them up). Broadly though, I use primarily either QImage or QPixmap. I know QPixmap is to be used for display images, and I still wanted to manipulate my image, so I settled on QImage. So I had to convert my QVideoFrame to a QImage. Easy enough.

``` python
# class VideoSurface(QtMultimedia.QAbstractVideoSurface):
    def present(self, frame: QtMultimedia.QVideoFrame):
        copy = QtMultimedia.QVideoFrame(frame)
        copy.map(QtMultimedia.QAbstractVideoBuffer.ReadOnly)

        image_format = QtMultimedia.QVideoFrame.imageFormatFromPixelFormat(copy.pixelFormat())

        my_image = QtGui.QImage(copy.bits(), copy.width(), copy.height(), copy.bytesPerLine(), QtGui.QImage.Format(image_format))

        copy.unmap()
        # Do something with your new `QImage` here!
        return True
```

Now I finally had what I wanted all that time ago! A simple example of low level access out of a QCamera. The only thing to do is wire it up to a QCamera

``` python
camera = QtMultimedia.QCamera()
video_surface = VideoSurface()
camera.unload()
camera.setViewfinder(video_surface)
camera.start()
```
