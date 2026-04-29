from business import *

class VideoApp:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap("./img/loopinf_logo.ico")
        self.root.title("LoopInf - Видео загрузчик")
        self.root.geometry("500x250")

        self.min_sequence = 20
        self.threshold = 1
        self.step = 2

        self.video_path = None

        self.btn_cnf = tk.Button(self.root, text="Настройки", command=self._open_config)
        self.btn_cnf.pack(pady=5, anchor="nw")

        self.label = tk.Label(root, text="Выберите видео", font=("Arial", 12))
        self.label.pack(pady=20)

        self.btn_open = tk.Button(root, text="Открыть видео", command=self._open_file)
        self.btn_open.pack(pady=5)

        self.btn_play = tk.Button(root, text="Запустить поиск циклов", command=self._play_video)
        self.btn_play.pack(pady=5)

        self.btn_dwn = tk.Button(self.root, text="Скачать видео", command=self._download_video)
        self.btn_dwn.pack(pady=5)
        self.btn_dwn.config(state="disabled")

        self.start_time = 0.0
        self.end_time = 0.0

    def _open_file(self):
        open_file(self)

    def _play_video(self):
        play_video(self)

    def _download_video(self):
        download_video(self)

    def _open_config(self):
        open_config(self)