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
