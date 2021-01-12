import urllib.request
from zadanie1 import down_page_data
import time
import matplotlib.image
import matplotlib.pyplot as plt


class Meteorology:
    def __init__(self, url):
        self.url = url
        self.__weather_key_to_file_name = {
            "1": "tempt",
            "2": "cisnt",
            "3": "wilgzt",
            "4": "wiatrt",
            "5": "opadyt",
            "6": "UVt"
        }
        self.__repr__()

    def run(self):
        print("1 - download weather diagram\n2 - download page binary data\n0 - exit\n")
        while True:
            choice = input()
            if choice == "1":
                self.weather_menu()
                print("1 - download weather diagram\n2 - download page binary data\n0 - exit\n")
            elif choice == "2":
                print(down_page_data(self.url))
            elif choice == "0":
                break
            else:
                print("wrong input")

    def weather_menu(self):
        print("Which diagram do you want to download:\n\n1 - temperature\n2 - pressure\n3 -humidity\n4 - wind\n5 - rainfall\n6 - UV\n0 - exit\n")
        while True:
            weather_choice = input()
            if weather_choice in self.__weather_key_to_file_name:
                print(f'{self.down_image(f"{self.__weather_key_to_file_name[weather_choice]}.jpg")}\n\nWhich diagram do you want to download:\n\n1 - temperature\n2 - pressure\n3 -humidity\n4 - wind\n5 - rainfall\n6 - UV\n0 - exit\n')
            elif weather_choice == "0":
                break
            else:
                print("wrong input")

    def __repr__(self):
        return f"Object downloads weather diagrams from {self.url}.\nAvailable methods:\n.main_menu\n.weather_menu\n.down_image(img_name)\n"

    def down_image(self, img_name):
        try:
            img_req = urllib.request.Request(f"{self.url}warszawapw/{img_name}.jpg")
            with urllib.request.urlopen(img_req) as img_resp:
                img_data = img_resp.read()
                time_now = time.strftime("%Y%m%d%H%M", time.localtime())
                with open(f"{img_name}_{time_now}.jpg", "wb+") as f:
                    f.write(img_data)
            if input("1 - Show diagram\nother - Continue\n") == "1":
                img = matplotlib.image.imread(f"{img_name}_{time_now}.jpg")
                plt.imshow(img)
                plt.show()
            return "file downloaded correctly"
        except:
            return "file downloaded incorrectly"
