# My Water Chain Project
## About The Project
My water chain is a waste-water management and monitoring project that embeds the security and transparency of BlockChain Technology along with the ease and effectiveness of IoT to reduce water exploitation and provide high-quality maintenance of wastewater.

"My water chain" allows the consumers (such as water industries and water parks) to monitor their water resources precisely and the waste generated. Specific Water coins (known as water drops) are provided to the industries based on their monthly performance. These coins can be used by industries to use water optimally and purchase water assets and allowances from all the locally performing industries.

The providers can understand the resource utility better with reliable and accurate IoT connectors that are interfaced and push water data every hour that includes "Flow Rate," "Conductivity Measure," "Solid Waste," "Spectral Measure," and "Optical Measure."

The project is an attempt to come up with an innovative application rather than the conventional use of BlockChain and follow the Hardware-Software approach and provide the most accurate data that will help in getting the best possible insights. These insights will be focusing on the prevention of water resource exploitation and take a step towards its effective utilization.

### Table of Contents
- Project Components
- Tools and Frameworks
- Installation
- How it Works?
- What's Next?

## Project Components

The three major project components are as follows:

- BlockChain
- IoT
- Computer Vision
- WebDev

### BlockChain

We're using **Blockchain** to bind the sensor Data and record them in real time on hourly basis. The main objective to use blockchain for sensor data is to have a decentralized unaltered system for data storage and facilitate data transparency and verify compliance with set targets and contracts.

All the water allowance are credited to user's account via BlockChain protocol where they make a transaction using water drops (Transaction Currency) and purchase extra allowance on monthly basis. Blockchain ensures security and transparency. It also allows to know about your local competitors.

    BlockChain Implimentation
    
        We have implemented custom blockchain protocol using Python Programming.
        This helped us in customizing the blockchain as per the needs of
        the IoT meters and web-servers. Two parallel chains are implemented
        which include:
            1. A chain for all the IoT data readings
            2. A chain for all the transaction purposes
        The libraries used in implementing the blockchain are:
            1. hashlib (For all sorts of encoding purposes)
            2. json (For json dumping blocks)
            3. datetime (For adding time-stamps)

![blockchain-image](assets/images/readme_editor/block_structure.jpg)

Further here's the process flow of the two blockchain processes that take place within the given architecture:

![datachain-image](assets/images/readme_editor/datachain.jpg)
Datachain Flow Chart

![transaction-image](assets/images/readme_editor/transactionchain.jpg)
Transaction chain Flow Chart


### IoT

**IoT** is the heart of this project. IoT devices are used that allow to read the water data in real time, look for tamperings, give an alert on leakages or faults and enable the users and industralists to get better insights about their consumptions and water conservation practices.


