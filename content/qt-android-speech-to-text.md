Title: Qt/Qml and Android's Built in Speech to Text and Text to Speech Capabilities
Date: 2020-01-19 21:39
Category: Random
Slug: qt-android-stt-tts
Authors: Ben Hoff
Summary: Getting Speech to Text and Text to Speech to work in Android


This is the blog post that I wish I would have had about two weeks ago. You can totally get Qt/QML to work with Android's Speech to Text and Text to Speech API's builtin, but it ain't going to be easy. So let's get started.

First we're going to need someway to trigger a listen and display some text. So we'll use a button and a text field to show our results. And before you ask, is this app going to win any design awards? No, it certainly won't.

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

Brutal and efficent. Ok, we need to get access to our objects on the C++ side. We could probably talk for some time about C++/QML integration, but this isn't the blog for it.


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

Alright we need a C++ object to hook up to the Java now. Also we're going to be doing some Java programming, so you need some light experience in QML, C++, and Java. At the end of this blog post, you'll be a polyglot, congrats! In order to integrate with the Java Native Interface, a lot of this stuff needs to be static. I was on (self-imposed) deadline while I was working on this stuff, so I didn't dive into the details of *why* it needs to be wrapped in static methods, but if you know, feel free to drop a comment below.

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
    void recognized_final_speech(const QString &text);
    void recognized_partial_speech(const QString &text);

private:
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

Let's just take stock for a minute. Because there's a lot of stuff going on. We've defined the user interface using QML, we've gotten access to that QML in the `main.cpp` file, and we've defined a complete header file in C++ with static methods to recieve 


