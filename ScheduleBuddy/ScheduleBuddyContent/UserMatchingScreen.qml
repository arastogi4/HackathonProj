import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 800
    height: 600

    // Animated Question
    Text {
        id: questionText
        text: "Do you prefer working alone or in a team?"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        font.pixelSize: 24
        opacity: 0

        // Fade-in animation
        Behavior on opacity {
            OpacityAnimator {
                duration: 1000
            }
        }

        Component.onCompleted: opacity = 1
    }

    // Gradient Slider
    Slider {
        id: choiceSlider
        width: parent.width * 0.8
        anchors.centerIn: parent
        from: 0
        to: 1
        stepSize: 0.01

        background: Rectangle {
            implicitWidth: choiceSlider.width
            implicitHeight: 10
            radius: 5
            gradient: Gradient {
                GradientStop { position: 0.0; color: "blue" } // Left choice
                GradientStop { position: 1.0; color: "red" }  // Right choice
            }
        }

        handle: Rectangle {
            width: 30
            height: 30
            radius: 15
            color: "white"
            border.color: "black"
        }
    }

    // Save Choice Button
    Button {
        text: "Save Choice"
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        onClicked: {
            console.log("Saved choice:", choiceSlider.value)
        }
    }
}
