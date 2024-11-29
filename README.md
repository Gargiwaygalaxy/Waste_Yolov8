Overview
The AI Waste Classifier is a cutting-edge solution that combines Artificial Intelligence, IoT, and robotics to tackle one of the most pressing environmental challenges—efficient waste management. By leveraging YOLOv8 Nano for real-time waste classification and Arduino-driven mechanisms for automated sorting, this system aims to revolutionize how waste is segregated at the source, reducing human error and promoting sustainable recycling practices.

How It Works
Live Waste Detection:

A webcam captures the waste items on a moving conveyor belt powered by an Arduino Uno and DC motors.
Real-Time Classification:

The captured video feed is processed by a YOLOv8 Nano-based machine learning model trained for 100 epochs to classify waste into wet or dry categories.
Automated Sorting:

The classification result is sent via FastAPI to a secondary system where Arduino-controlled mechanical arms segregate the waste into designated bins.
Key Features
AI-Powered Classification: High accuracy in detecting and classifying waste in real-time.
IoT Integration: Smooth communication between devices using FastAPI for rapid decision-making.
Automated Sorting: Reduces reliance on manual labor, improving efficiency and safety.
Scalable Design: Adaptable to include additional waste categories (e.g., hazardous, recyclable).
Environmentally Conscious: Contributes to sustainable waste management by optimizing segregation for recycling.
Why It Matters
Environmental Impact: Mismanaged waste leads to pollution and inefficient recycling processes. Our project directly addresses this by enabling precise waste segregation.
Cost Efficiency: Reduces the need for manual sorting, cutting down labor costs and time.
Future Potential: Scalable for industrial, municipal, and household use, with the ability to classify more complex waste types.
Technologies Used
YOLOv8 Nano: Lightweight, high-speed object detection model.
NodeMCU & Arduino: For conveyor belt and mechanical arm control.
FastAPI: Facilitates seamless data transfer between devices.
Python & OpenCV: For video stream processing and ML integration.
How to Set It Up
Hardware Requirements:

Arduino Uno, DC Motors, Servo Motors for arms, IR Sensors, Conveyor Belt, Webcam.
Software Requirements:

Python 3.8+, YOLOv8 Nano, FastAPI, Arduino IDE.
Steps to Deploy:

Train the YOLOv8 model with your dataset (100 epochs recommended).
Run the FastAPI server to handle data communication.
Load Arduino code to control motors and sorting mechanisms.
Connect all hardware components and start the system.
Future Enhancements
Add support for multi-category classification (e.g., recyclable, organic, hazardous).
Integrate cloud-based monitoring for real-time performance tracking.
Develop a low-cost consumer version for household waste management.
