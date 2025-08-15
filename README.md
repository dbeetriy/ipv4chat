IPv4 Broadcast Chat
---
**A Python implementation of a dual-threaded UDP broadcast chat for local networks.**

**Usage:** 

`./ipv4chat -a <IP> -p <PORT>`

**Options:**

- `-a` IP address that other clients can connect to (`0.0.0.0`);

- `-p` connection port (`12345`).

**How it works:**

Program has **2** POSIX threads:
- **Reciever** thread
  "listens" to the socket (`recvfrom`) and after receiving a UDP datagram displays the sender's IPv4 address, their nickname, and the received message. 
- **Sender** thread 
   waits for the user to input a text message (limited to 1000 bytes), and after the input is complete, forms and sends a UDP datagram (`sendto`) to the broadcast IPv4 address 255.255.255.255 and the port (specified in the command line options).

---

This is just my tech project for an internship interwview. 
