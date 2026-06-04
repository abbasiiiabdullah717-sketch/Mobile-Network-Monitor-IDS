import socket
import threading
import time

def start_sniffer():
    try:
        # Sniffer socket setup
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('127.0.0.1', 9999))
        
        print("[*] Sniffer Thread: Active & Listening on port 9999...\n")
        
        # Sirf 5 packets capture karenge demo ke liye
        for _ in range(5):
            data, addr = s.recvfrom(1024)
            print(f"\n[+] [PACKET CAPTURED] From: {addr[0]}:{addr[1]}")
            print(f"    Payload/Data: {data.decode('utf-8')}")
            
        print("\n[*] Sniffer Thread: Demo complete. Stopping.")
        s.close()
    except Exception as e:
        print(f"Sniffer Error: {e}")

def start_generator():
    time.sleep(2) # Sniffer ko active hone ka time dein
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("[*] Generator Thread: Starting traffic simulation...")
        
        for i in range(1, 6):
            message = f"ALERT: Malicious activity log test #{i}"
            s.sendto(message.encode('utf-8'), ('127.0.0.1', 9999))
            print(f"[->] Generator: Sent packet {i}...")
            time.sleep(1.5) # Har packet ke beech break
            
        s.close()
    except Exception as e:
        print(f"Generator Error: {e}")

if __name__ == "__main__":
    print("=== CYBER SECURITY PROJECT: NETWORK MONITORING TOOL ===")
    
    # Dono kaam sath karne ke liye threading use kar rhe hain
    sniffer_thread = threading.Thread(target=start_sniffer)
    generator_thread = threading.Thread(target=start_generator)
    
    # Threads ko start karein
    sniffer_thread.start()
    generator_thread.start()
    
    # Wait for completion
    sniffer_thread.join()
    generator_thread.join()
    print("\n=== Project Execution Finished Successfully ===")
