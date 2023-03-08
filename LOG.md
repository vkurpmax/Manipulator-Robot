# Manipulator-Robot
Log of what I did everyday

## 20230226
No progress. Dynamixel shield doesn't make the servo moved a single degree. I'm frustrated.

## 20230227
- Talk to lecturer for the possibilities of title change. Prefer back to old title, "Internet of Things" than "Deep Learning". One lecturer said to just go on with "Deep Learning".
- There's contact with customer support Digiware. They gave me a document and tutorial regarding the dynamixel shield.
- Buy USB TTL on Tokopedia. We will se later.

## 20230228
- Nothing changed. I'm still waiting for my package (USB TTL).

## 20230302
- Using USB TTL, I try to do recovery using Dynamixel Wizard 2.0 software and scan the dynamixel but my computer read no connection through USB TTL.

## 20230304
- There's movement. I'm success to control Dynamixel AX-12A.
- I found problem that using dynamixel shield. There was problem with my power supply. The voltage was not 12V through TTL pin on Dynamixel shield even though the supply voltage was 12V.
- I also found problem that the baudrate, protocol, and ID was not right.
- I did scanning the dynamixel first to know baudrate, protocol, and ID using U2D2 and software Dynamixel Wizard 2.0.

## 20230306
- I made Grove 4 Pin. I bought 4 pin connectors and assembled it to 4 pin jumper wires. So it will be female jumper wires to female connector. I will use it for my UART (from U2D2/Dynamixel Shield) to USB TTL.