# AI_Project
Population of the world is progressively getting older. According to United Nations, by 2030, older persons will outnumber children aged 0-9 years (1.4 billion vs. 1.3 billion); by 2050, there will be more people aged 60 or over than adolescents and youth aged 10-24 years (2.1 billion vs. 2.0 billion).

![image](https://user-images.githubusercontent.com/66861243/159152906-d065740d-8c52-488e-8b4e-99e04e479151.png)

In 2050, two out of every three oldest-old persons will live in developing regions.

These people will need help and fortunately with the development of machine learning, and proliferation of IOT devices we will be able to help. One paper that talks about using machine learning to help the elderly is [An Agent-based Approach to Care in Independent Living](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=D4F68AC886F5F0470207D1ACB782BF7A?doi=10.1.1.301.3380&rep=rep1&type=pdf). Our project is based on the Software aspect of this research paper. 

The paper introduces a fall detector based on a neural network and a multi-agent architecture for requesting emergency services. It presented a multi-agent system for the care of elderly people living at home on their own, with the aim to prolong their independence. The system is composed of seven groups of agents providing a reliable, robust and flexible monitoring by sensing the user in the environment, reconstructing the position and posture to create the physical awareness of the user in the environment, reacting to critical situations, calling for help in the case of an emergency, and issuing warnings if unusual behavior is detected.

## Installation and Quick Start

- Setting up the Python Environment with dependencies:

        pip install -r requirements.txt

- Cloning the Repository: 

        git clone https://github.com/us4544/AI_Project 
- Entering the directory: 

        cd AI_Project
- Running the file:

        pip install virtualenv
        python -m venv env
        source env/bin/activate
        pip install -r requirements.txt
        streamlit run main.py
        
<hr>
