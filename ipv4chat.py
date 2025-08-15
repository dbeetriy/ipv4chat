#!/usr/bin/env python3

import threading
import sys
import argparse
import socket

MAX_SIZE_BYTES = 1000
BROADCAST = '255.255.255.255'

def send(soket, port, nickname):
    while 1:
        try:
            text = input()
            if len(text) > MAX_SIZE_BYTES:
                print("Message too long (max 1000 bytes)")
                continue
            
            data = f"{nickname}:{text}".encode('utf-8')
            soket.sendto(data, (BROADCAST, port))
            
        except KeyboardInterrupt:
            print("\nExiting...")
            soket.close()
            sys.exit(0)
            
        except Exception as e:
            print(f"Error sending message: {e}")
            break
    
def receive(soket):
    while 1:
        try:
            msg, addr = soket.recvfrom(MAX_SIZE_BYTES)
            ip, port = addr
            try:
                nickname, text = msg.decode('utf-8').split(':',1)
                print(f"\n[{ip}]{nickname}: {text}\n", end="", flush=True)
            except:
                print(f"\n[{ip}] Received malformed message\n", end="", flush=True)
                
        except Exception as e:
            print(f"\nError receiving message: {e}\n", end="", flush=True)
            break

def main():
    parser = argparse.ArgumentParser(description='IPv4 UDP Broadcast Chat')
    parser.add_argument('-a', '--address', required=True, help='IPv4 address to bind')
    parser.add_argument('-p', '--port', type=int, required=True, help='Port number to bind')
    args = parser.parse_args()
    
    nickname = input("Your nickname: ").strip()
    if not nickname:
        print("Nickname can't be empty!")
        sys.exit(1)
    
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        soket.bind((args.address, args.port))
        
        print(f"Chat started on {args.address}:{args.port}. Nickname: {nickname}")
        print("Type your message and press Enter to send. Ctrl+C to exit.\n")

        receiver_thread = threading.Thread(
            target=receive,
            args=(soket,),
            daemon=True
        )
        
        receiver_thread.start()
        send(soket, args.port, nickname)

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        soket.close()
        
if __name__ == "__main__":
    main()