#ifndef ANDROIDINTEGRATION_H
#define ANDROIDINTEGRATION_H

#include <QObject>
#ifdef Q_OS_ANDROID
#include <QAndroidJniObject>

#endif



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

#endif // ANDROIDINTEGRATION_H
