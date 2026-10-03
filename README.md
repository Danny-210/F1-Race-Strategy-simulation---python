# F1-Race-Strategy-simulation---python

F1 Race strategy engine

This is a data driven f1 race simulation and strategy tool built in python. This engine evaluates realistic tyre degradation (non linear), fuel burn off during the race making the car faster as the fuel burns, driver pace varience and sporting rules including differnt tyre compounds having to be used during a race


**Key Features**

* Realistic tyre degradation - using quadratic formula
* Realistic fuel burn off - car gets lighter/faster as fuel burns off late in the race
* Fastest strategy search (monte carlo) - iterates through thousands of possible race scenarios to work out the fastest race strategy
* Customisable race conditions - race length, lap time, tyre wear rate, tyre pace, driver pace, driver consistency etc
* Puncture threshold - once the tyre has a puncture the laptimes reflect this

This project has 2 files for 2 different scenarios



**Strategy Generator**




This file when ran will display the top 10 strategies based on thousands of simulations using the conditions that you have given it including tyre, track and driver data


<img width="1237" height="190" alt="Screenshot (141)" src="https://github.com/user-attachments/assets/714712df-3ec3-44eb-8e1e-a9da35a24b0c" />





**Single Race Generator**
Running this file will simulate 1 full race showing details such as tyre condition, laptime, when you pitted and pace gained due to fuel burn

<img width="964" height="822" alt="Screenshot (142)" src="https://github.com/user-attachments/assets/7a0fb441-5318-4cb9-adfe-c4f57e335200" />



Strategy for this race is set by yourself and is done by changing this strategy variable. The strategy below shows a 2 stop with the first tyre being your starting tyre and the number being when you box
  NOTE: The last lap must be the number for the last stint





<img width="886" height="68" alt="Screenshot (144)" src="https://github.com/user-attachments/assets/2b6a9a57-9577-4671-a166-371277075ac8" />


