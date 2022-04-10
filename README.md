# Help4Health
Population of the world is progressively getting older. According to United Nations, by 2030, older persons will outnumber children aged 0-9 years (1.4 billion vs. 1.3 billion); by 2050, there will be more people aged 60 or over than adolescents and youth aged 10-24 years (2.1 billion vs. 2.0 billion).

![image](https://user-images.githubusercontent.com/66861243/159152906-d065740d-8c52-488e-8b4e-99e04e479151.png)

In 2050, two out of every three oldest-old persons will live in developing regions.

These people will need help and fortunately with the development of machine learning, and proliferation of IOT devices we will be able to help. One paper that talks about using machine learning to help the elderly is [An Agent-based Approach to Care in Independent Living](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=D4F68AC886F5F0470207D1ACB782BF7A?doi=10.1.1.301.3380&rep=rep1&type=pdf). Our project is based on the Software aspect of this research paper. 

The paper introduces a fall detector based on a neural network and a multi-agent architecture for requesting emergency services. It presented a multi-agent system for the care of elderly people living at home on their own, with the aim to prolong their independence. The system is composed of seven groups of agents providing a reliable, robust and flexible monitoring by sensing the user in the environment, reconstructing the position and posture to create the physical awareness of the user in the environment, reacting to critical situations, calling for help in the case of an emergency, and issuing warnings if unusual behavior is detected.

## Abstract
We intend to develop a web application for a smart healthcare monitoring system for the elderly living alone in developing countries that employs Artificial Intelligence and Machine Learning techniques such as Decision Tree Classifiers and Logistic Regressors to predict the activity performed by the elderly while in their homes using sensor readings from their smartphones. The web application takes sensor readings from sensors used to track hand and leg movements, as well as body temperature, as inputs and predicts activity based on the sensor coordinates provided. Through this smart application, we hope to provide a long-term measure for monitoring the daily activities and physical well-being of the elderly.

## Issues in Existing Systems
With recent technological advancements and a highly competitive work environment, the elderly's self-sufficiency has become a source of concern. As a result, ensuring their physical and mental well-being should be our primary focus. Currently, family members and caregivers provide care and guidance to the elderly in most countries, but with increasing workload, there is a need for smarter methods to take on this job. Researchers are focusing on overcoming the aforementioned shortcomings by utilizing smart devices to look after the population's well-being using emerging technologies such as IoT and Artificial Intelligence. Our product uses a similar approach to tackle this problem and aid to the betterment of the elderly.

## Problem Statement
Our problem statement focuses on addressing the issue of inadequate care for the elderly as a result of the current generation's poor work-life balance and high workload. We intend to create a smart healthcare monitoring system for the elderly's well-being, particularly in developing countries where people must deal with rapidly evolving technology and a rapidly changing working environment. Through our web application, the activities of the elderly can be predicted from anywhere using sensor inputs from smartphones carried by the elderly, and immediate action can be taken in the event of an emergency or if an unusual pattern in their daily lives is discovered.

## Objective
The goal of our project is to gather insights based on our study's findings to assess how active a person is based on physical activities performed, which will be used to create hardware or software. The goal is to use a tri-axial accelerometer to detect falls and report such findings to an emergency centre. The project introduces a machine learning-based fall detector as well as a multi-agent architecture for contacting emergency assistance via an input sensor from a web-based monitoring application.

## PROPOSED METHODOLOGY- DIAGRAMATIC REPRESENTATION
The system requirements are met via a multi-agent architecture. Each system module, job, or activity is meant to function as an agent that provides a service. Agents are grouped into groups at a given level of abstraction and coordinated by another, higher-level agent in the hierarchy. 

- The agent architecture reveals the various groups of agents. Agents from one group have the same architecture and perform logically similar functions, e.g., all sensor agents retrieve the data from sensors. 

- The arrows indicate the communication between agents. The system is made up of seven groups of agents that provide reliable, robust, and flexible monitoring by sensing the user in the environment, reconstructing the user's position and posture to create physical awareness of the user in the environment, reacting to critical situations, calling for help in an emergency, and issuing warnings if unusual behaviour is detected.

![workflow](https://user-images.githubusercontent.com/66861243/162609589-fc83608a-6b4b-4cb1-a4e9-375d6691f3f5.png)

## Installation and Quick Start

- Setting up the Python Environment with dependencies:

        pip install -r requirements.txt

- Cloning the Repository: 

        git clone https://github.com/us4544/Help4Health.git
- Entering the directory: 

        cd Help4Health
- Running the file:

        pip install virtualenv
        python -m venv env
        source env/bin/activate
        pip install -r requirements.txt
        streamlit run main.py
        
<hr>
