Prescription Identification Glasses
Overview
This project develops a pair of smart glasses equipped with a Raspberry Pi Zero and an external camera module to assist visually impaired elderly users in identifying their medications. The device uses image recognition to read labels on prescription bottles and provides audible feedback to the user. The system is designed to be voice-activated, enhancing usability and accessibility.

Features
Smart Glasses Design: Compact and wearable device integrating Raspberry Pi Zero and a camera module mounted on 3D-printed glasses.
Medication Identification: Employs image recognition to read and interpret prescription labels.
Voice Activation: Users can operate the device using simple voice commands, thanks to integrated speech recognition technology.
Audible Feedback: Once a medication is identified, the device relays important information audibly to the user.
How It Works
Voice Commands: Users activate the device and command it to scan medication using voice.
Image Capture and Processing: The camera captures images of the medication, which are processed to detect and read labels.
Audio Output: The device provides an audio description of the medication, ensuring the user receives accurate information.
Installation
Clone this repository.
Install required dependencies:
pip install pyzbar pillow speechrecognition picamera

Usage
To operate the glasses:

Wear the glasses and activate them by saying "Picture."
Hold the prescription bottle in front of the glasses.
Listen to the medication details spoken by the device.

Hardware Setup
Raspberry Pi Zero: Acts as the central processing unit.
Camera Module: Captures images of the prescription labels.
3D-Printed Glasses: Custom-designed to house the Raspberry Pi and camera comfortably.
Raspberry Pi Zero Audio Hat
Micro-USB Microphone
