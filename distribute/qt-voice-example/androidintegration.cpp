#include "androidintegration.h"

#ifdef Q_OS_ANDROID
#include <QtAndroid>
#include <QAndroidJniEnvironment>
#endif

AndroidIntegration *AndroidIntegration::this_pointer;

AndroidIntegration::AndroidIntegration(QObject *parent) : QObject(parent)
#ifdef Q_OS_ANDROID
  , my_activity(QtAndroid::androidActivity())
#endif
{
    if (this_pointer != nullptr)
        this_pointer = this;
#ifdef Q_OS_ANDROID
    QAndroidJniEnvironment env;
    jclass object_class = env->GetObjectClass(my_activity.object<jobject>());
    JNINativeMethod methods [] = {
        {"emit_final_text", "(Ljava/land/String;)V", reinterpret_cast<void*>(&AndroidIntegration::emit_final_text)},
        {"emit_partial_text", "(Ljava/land/String;)V", reinterpret_cast<void*>(&AndroidIntegration::emit_partial_text)}
    };
    env->RegisterNatives(object_class, methods, sizeof(methods)/ sizeof(methods[0]));
    env->DeleteLocalRef(object_class);
#endif
}


#ifdef Q_OS_ANDROID
void AndroidIntegration::emit_final_text(JNIEnv *env, jobject thiz, jstring final_text)
{
    Q_UNUSED(thiz)
    if (this_pointer != nullptr)
    {
        QString final_string_from_java(env->GetStringUTFChars(final_text, 0));
        emit this_pointer->recognized_final_speech(final_string_from_java);
    }
}

void AndroidIntegration::emit_partial_text(JNIEnv *env, jobject thiz, jstring partial_text)
{
    Q_UNUSED(thiz)
    if (this_pointer != nullptr)
    {
        QString partial_string_from_java(env->GetStringUTFChars(partial_text, 0));
        emit this_pointer->recognized_partial_speech(partial_string_from_java);
    }

}
#endif
