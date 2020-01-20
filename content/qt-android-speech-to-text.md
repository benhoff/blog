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

Alright we need a C++ object to hook up to the Java now.  This object is going to interface with our Java code (both ways!) and provide some signals that we're going to use in our `main.cpp` file to talk to the QML. This is the workhorse our our Qt code.


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

So we've got our C++ and QML side mostly stubbed out. Now let's work on the Java/Android side. This gets a little messy for three reasons. The first reason is that in order to have a clean user experience (I.e, not have the native/third-party Speech to Text dialogue pop up for speech recognition) the Android Speech Recognition classes have to be created and run on the Android UI thread. The second piece is that the class that interacts with the results of the speech recognition (`RecognitionListener`) is a Java interface/Abstract class and thus must be subclassed (or implemented) in Java language. The third piece is that we've got to contend with the fact that this is a Qt/QML application, not a native Android one. So we're going to have to subclass `QtActivity` and use that.

Three Issues:
1. Android SpeechRecognizer must be run on the Android UI Thread
2. The RecognitionListener is an interface that has to be implemented
3. We're using Qt/QML and we need to interface back to the C++/QML side

Three Fixes:
1. Implement the `Runnable` interface so we have something that we can pass to the `runOnUiThread` method
2. Implement a `RecognitionListener`
3. Subclass the `QtActivity` class, and then build out the interfaces

Let's start with number 2 first, our `RecognitionListener`. This is starting from the bottom up in our problem space, so we won't build out any code to interact directly with out QT/QML app in this one. Pure Android Java right now.

``` java
// Implement the `RecognitionListener`
public class QtSpeechRecognition implements RecognitionListener
{
	// We're going to define how we want the Android to listen with this object
    private Intent recognizer_intent;

	// This is what's going to do the Speech to Text
    private SpeechRecognizer speech_recognizer = null;

	// NOTE: We haven't defined the `MyQtActivity` class yet
    MyQtActivity my_qt_activity;

	// Remember that we need the `SpeechRecognizer` to be created on the Android Thread
    public MySpeechRecognition(MyQtActivity activity)
    {
		// Store a reference to the activity so that we can check the permissions
        my_qt_activity = activity;

		// Create the speech recognizer and set the listener to be this instance
        speech_recognizer = SpeechRecognizer.createSpeechRecognizer(activity);
        speech_recognizer.setRecognitionListener(this);

		// This intent is to recognize speech
        recognizerIntent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);

		// We're going to define how we want our recognizer to work. Going to use english, return partial results and return up to three results
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_PREFERENCE, "en-us");
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 3);
        recognizerIntent.putExtra(RecognizerIntent.EXTRA_PARTIAL_RESULTS, true);
    }

	// This is our method to start the process
    public void start_listening() {
		// We need to make sure that we have the ability to record audio
        String requiredPermission = Manifest.permission.RECORD_AUDIO;

		// If we don't have permission, ask for it
        if (my_activity.checkCallingOrSelfPermission(requiredPermission) == PackageManager.PERMISSION_DENIED) {
			// Note that I think you can pass notes to the user to tell them why you need this permission,
			// but it should be self evident?
            my_activity.requestPermissions(new String[]{requiredPermission}, 101);
        }

        speech.startListening(recognizerIntent);
    }

	@Override
	public void onPartialResults(Bundle arg0) {
		ArrayList<String> matches = arg0.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);
		String text = matches.get(0);
		System.out.println(text);
		my_qt_activity.partial_text(text);
	}

	@Override
	public void onResults(Bundle results) {
		ArrayList<String> matches = results
				.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);
		String text = matches.get(0);
		my_qt_activity.emit_text(text);
	}

	@Override
	public void onRmsChanged(float rmsdB) 
	{
		// Note that you could use this method to display back to the user how loud they are talking
		// or if the microphone is picking up them talking.
	}

	// NOTE: we have to override the following methods otherwise the Android Java compilier will complain

    @Override
    protected void onStop() {
        super.onStop();
        if (speech != null) {
            speech.destroy();
        }
    }

    @Override
    public void onBeginningOfSpeech() {
     }

     @Override
     public void onBufferReceived(byte[] buffer) {
     }

     @Override
     public void onEndOfSpeech() {
        }

	@Override
	public void onError(int errorCode) {
		String errorMessage = getErrorText(errorCode);
	}

	@Override
	public void onEvent(int arg0, Bundle arg1) {
	}

	@Override
	public void onReadyForSpeech(Bundle arg0) 
	{
	}

	public static String getErrorText(int errorCode) {
		String message;
		switch (errorCode) {
			case SpeechRecognizer.ERROR_AUDIO:
				message = "Audio recording error";
				break;
			case SpeechRecognizer.ERROR_CLIENT:
				message = "Client side error";
				break;
			case SpeechRecognizer.ERROR_INSUFFICIENT_PERMISSIONS:
				message = "Insufficient permissions";
				break;
			case SpeechRecognizer.ERROR_NETWORK:
				message = "Network error";
				break;
			case SpeechRecognizer.ERROR_NETWORK_TIMEOUT:
				message = "Network timeout";
				break;
			case SpeechRecognizer.ERROR_NO_MATCH:
				message = "No match";
				break;
			case SpeechRecognizer.ERROR_RECOGNIZER_BUSY:
				message = "RecognitionService busy";
				break;
			case SpeechRecognizer.ERROR_SERVER:
				message = "error from server";
				break;
			case SpeechRecognizer.ERROR_SPEECH_TIMEOUT:
				message = "No speech input";
				break;
			default:
				message = "Didn't understand, please try again.";
				break;
		}
		return message;
	}

```

Ok, now let's create our `Runnable` infrastructure and our subclass of `QtActivity`.


``` java
class CreateSpeechRecognizerOnUiThreadRunnable implements Runnable
{}

class StartListeningOnUiThreadRunnable implements Runnable
{}

public class MyQtActivity extends QtActivity
{
	private QtSpeechRecognition qt_speech_recog;
	private StartListeningOnUiThreadRunnable listen_runnable;
	private TextToSpeech;


	@Override
	public void onCreate(Bundle savedInstanceState)
	{}

	@Override
	public void onDestroy()
	{}

	public void start_listening()
	{}

	public void speak(String speakme)
	{}

	public void interrupt_speak()
	{}

	public static native void emit_text(String str);
	public static native void partial_text(String str);


}


```

