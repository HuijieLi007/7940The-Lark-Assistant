# Product Manual
***
## Implementation method
web bot
***
## Goals and Objectives
At this special moment in 2020, people in China are working hard to fight the new coronavirus. 
In order to help everyone understand the development status of the epidemic in time, 
and get timely assistance when encountering difficulties, we decided to design a chat robot called Lark Assistant 
to fight the epidemic.
***
## Outline design
### Nucleic acid test appointment
+ **Description** We observed a phenomenon in which a large number of suspected patients gathered in hospitals for nucleic acid tests to check whether they were infected with the new coronavirus. But in this case there is a high possibility of cross infection. So in order to avoid the risk of cross infection when people are waiting in line for nucleic acid testing, we have designed a function called online appointment testing. When you have mild symptoms such as fever, cough, etc., you can ask the Lark Assistant to make a test appointment. 
+ **Implement** The Lark Assistant will first locate your location and return the information of the nearest three designated hospitals: 1. The current number of people in the queue, 2. Number of patients, 3, the number of remaining admissible patients. Then recommend the most reasonable hospital to make an appointment based on the returned data, and finally remind the appointment time in time.
### Material aid
+ **Description** At an important time for the whole nation to fight the epidemic, medical supplies are indispensable. However, at this time, the shortage of medical supplies has become a lethal key, and people cannot buy medical supplies. Therefore, the Larkbird Assistant compiles some e-commerce platform sales data such as Tmall, JD.com, and Amazon data, and constantly monitors the latest medical supplies on the shelf, and timely feedbacks medical supplies purchase links for everyone to purchase.
+ **Implement** First tell The Lark Assistant the names of the materials you need to buy, such as medical masks, medical alcohol disinfectant, alcohol disinfectant hand sanitizer, medical gloves, medical goggles, etc. The Lark Assistant then returns the relevant product purchase link.
### New coronavirus broadcast
+ **Description** The latest development of the epidemic has stirred everyone's heart, so timely broadcast of the epidemic information is also important.
+ **Implement** When you ask the Lark Assistant for the latest epidemic situation, he will return the latest epidemic report map. The map distribution visually displays the epidemic information in various regions of the country, including the latest confirmed cases, suspected cases and death cases.

