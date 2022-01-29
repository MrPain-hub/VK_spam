import tkinter as tk
from tkinter import ttk
import vk
import time
from datetime import datetime


class MyTk(tk.Tk):
    """
    Параметры окна
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Рассылка по группам')
        self.resizable(False, False)  # запрет на изименение размера окна
        self.set_ui()
    """
    Структура окна (LabelFrame, Frame)
    """
    def set_ui(self):
        self.fr1()
        self.lf1()
        self.lf2()
        self.lf3()
        ttk.Button(self,
                   text="start",
                   command=self.start)\
            .pack(fill=tk.BOTH)

    def fr1(self):  # Ввод токена
        fr = ttk.Frame(self)
        fr.pack(fill=tk.BOTH)
        ttk.Label(fr, text="введите token").pack(side=tk.LEFT)
        self.ent_TOKEN = ttk.Entry(fr)
        self.ent_TOKEN.pack(side=tk.RIGHT)

    def lf1(self):  # Директория файла с id группами
        lf = ttk.LabelFrame(self, text="Директория файла с id группами")
        lf.pack(fill=tk.BOTH)
        self.ent_groups = ttk.Entry(lf)
        self.ent_groups.insert(0, "id_groups.txt")
        self.ent_groups.pack(fill=tk.X)

    def lf2(self):  # Директория файла с id фотографиями
        lf = ttk.LabelFrame(self, text="Директория файла с id фото")
        lf.pack(fill=tk.BOTH)
        self.ent_photo = ttk.Entry(lf)
        self.ent_photo.insert(0, "id_photo.txt")
        self.ent_photo.pack(fill=tk.X)

    def lf3(self):  # Директория файла с id фотографиями
        lf = ttk.LabelFrame(self, text="Директория файла с текстом")
        lf.pack(fill=tk.BOTH)
        self.ent_txt = ttk.Entry(lf)
        self.ent_txt.insert(0, "text_message.txt")
        self.ent_txt.pack(fill=tk.X)
    """
    Запуск работы
    """
    def start(self):
        lst_data, lst_group_id, text = [], [], []
        self.read_file(lst_data, self.ent_photo.get())
        self.read_file(lst_group_id, self.ent_groups.get())
        self.read_file(text, self.ent_txt.get())
        myVkApi = vk.API(vk.Session(access_token=self.ent_TOKEN.get()))
        for content in lst_data:
            for group in lst_group_id:
                try:
                    Post = myVkApi.wall.post(v=5.131, owner_id=group, message=" ".join(text), attachments=content)  # публикация на стене "hello world"
                    time.sleep(0.2)
                except Exception as err:
                    print(datetime.today().strftime(f"ОШИБКА %H:%M:%S Группа: https://vk.com/club{group.replace('-', '', 1)}\nКод ошибки: {err}\n"))
                    continue

    def read_file(self, name_file, url):
        with open(url, "r", encoding="utf-8") as f:
            name_file.extend(f.read().splitlines())
        return name_file


window = MyTk()
window.mainloop()
