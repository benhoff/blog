Title: Qt/Qml and Android's Built in Speech to Text and Text to Speech Capabilities
Date: 2020-01-19 21:39
Category: Random
Slug: qt-android-stt-tts
Authors: Ben Hoff
Summary: Getting Speech to Text and Text to Speech to work in Android


This is the blog post that I wish I would have had about two weeks ago. You can totally get Qt/QML to work with Android's Speech to Text and Text to Speech API's, but it isn't easy. So let's get started.

First we're going to need someway to trigger a listen and display some text. So we'll use a button to trigger and a text field to show our results.

Before you ask, is this app going to win any design awards? No, it certainly won't.

```
// main.qml
import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Rectangle {
        height: 100
        width: 100
        id: push_to_talk
        x: 270
        y: 34
        color: "red"
        radius: .5 * height

        MouseArea {
            anchors.fill: parent
            onClicked: {
                // we'll be doing stuff here later

            }
        }
    }

    TextField {
        id: text_edit
        x: 220
        y: 183
        placeholderText: "Text to showup here"
    }
}

```

Brutal and efficent. Ok, we need to get access to our QML objects on the C++ side. We could probably talk for some time about C++/QML integration, but this isn't the blog for it.


``` cpp
// main.cpp

#include <QGuiApplication>
#include <QQmlApplicationEngine>

int main(int argc, char *argv[])
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;
    const QUrl url(QStringLiteral("qrc:/main.qml"));
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
                     &app, [url](QObject *obj, const QUrl &objUrl) {
        if (!obj && url == objUrl)
            QCoreApplication::exit(-1);
    }, Qt::QueuedConnection);
    engine.load(url);

    // NOTE: Access QML Objects here
    QObject *qml_main_window = engine.rootObjects()[0];

    return app.exec();
}
```

Alright we need a C++ object to hook up to the Java now. 

``` cpp
// androidintegration.h

class AndroidIntegration : public QObject
{
    Q_OBJECT
public:
    explicit AndroidIntegration(QObject *parent = nullptr);

public slots:

    // ----- These slots trigger these actions in java
    void use_text_to_speech(QString speak_me);
    void stop_text_to_speech();

    void transcribe_speech_to_text();
    // End ----- slots that trigger actions in java

signals:
    // ---- Our text to emit to the QML side using Qt signals

    void recognized_final_speech(const QString &text);
    void recognized_partial_speech(const QString &text);

    // End ---- Our text to emit to the QML side using Qt signals

private:
    // Since we have to use static to interface with the Java side,
    // we're going to use a singleton pattern to make this happen.
    static AndroidIntegration *this_pointer;

#ifdef Q_OS_ANDROID
    QAndroidJniObject my_activity;

    // ------ These are Java methods that will be redirected to C++

    static void emit_final_text(JNIEnv *env, jobject thiz, jstring final_text);
    static void emit_partial_text(JNIEnv *env, jobject thiz, jstring partial_text);

    // End ------ of Java methods that will be redirected to C++

#endif

};
```

There's a lot of stuff going on. We've defined the user interface using QML, we've gotten access to that QML in the `main.cpp` file, and we've defined a complete header file in C++ to interface with the Java. 

The public slots defined in the above class are Qt/C++ slots that are going to call Java methods. The private static methods at the bottom of the `AndroidIntegration` class are going to be Java methods, that are going to call C++ code. Confused yet? Perfect!

Let's define some Java code now, starting with the Speech to Text. As a side note, we're totally going to define the class/instance `MySpeechRecogWrapper` in a second.


``` java
package com.MyCompany.myPackage;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

import org.qtproject.qt5.android.bindings.QtActivity;


class CreateSpeechInstance implements Runnable
{
    # FIXME
    public MySpeechRecogWrapper speech;
    private MyActivity my_activity_instance;
    # FIXME
    MyRunnable(MyActivity in_activity)
    {
        my_activity_instance = in_activity;
    }

    @Override
    public void run()
    {
        speech = new MySpeechRecogWrapper(act);
    }

}

class RunSpeechRecog implements Runnable
{
    public MySpeechRecognition speech;

    Reuse(MySpeechRecognition sp)
    {
        speech = sp;
    }

    @Override
    public void run()
    {
        speech.start_listening();
    }

}


public class MyActivity extends QtActivity

{
    private MySpeechRecogWrapper my_speech_recog_wrapper;
    private RunSpeechRecog run_speech_recognition;

    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        my_speech_recog_wrapper = new MySpeechRecogWrapper(this);

	# FIXME
        MyRunnable run = new MyRunnable(this);
        runOnUiThread(run);
        my_speech_recog_wrapper = run.speech;
        reuse = new Reuse(run.speech);
    }

    public void start_listening()
    {
        runOnUiThread(reuse);
    }


    public static native void emit_text(String str);
    public static native void partial_text(String str);


}



```


