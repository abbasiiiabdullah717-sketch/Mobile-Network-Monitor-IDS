**​📡 Network Traffic Monitor Project**

​A simple Python-based cybersecurity project that monitors local network traffic and simulates data packet interception using a multi-threaded engine.

​​**📌 Features**

​• Monitors local transport layer traffic on port 9999

• Simulates custom log data and fake network alerts for testing

• Uses multi-threading so the sniffer and generator run at the same time

• Designed to run easily on android phone environments like Pydroid 3 without root permissions

​**🧠 How It Works**

​The tool opens a socket connection on port 9999 to listen for incoming traffic. At the same time, a background thread generates test alerts so you can see live data capture on the screen.

​**📂 Project Structure**

​network_monitor_ids/

 main.py
 
README.md

**​🚀 How To Run**

​Clone the repository:
git clone https://github.com/abbasiiiabdullah717-sketch/Mobile-Network-Monitor-IDS.git
​Open main.py in Pydroid 3 or any Python setup and hit run:
python main.py

**📋 Example Output**

*CYBER SECURITY PROJECT: NETWORK MONITORING TOOL*

*Sniffer Thread*: Active & Listening on port 9999...

*Generator Thread*: Starting traffic simulation...

*Generator*: Sent packet 1...

*PACKET CAPTURED From*: 127.0.0.1:39571
    Payload/Data: ALERT: Malicious activity log test #1

*Generator*: Sent packet 2..

*PACKET CAPTURE From*:127.0.0.1:39571      Payload/data: ALERT: Malicious activity log test #2


**​📦 Requirement**

°No external packages needed

°Works using standard Python libraries only (socket, threading, time) 
