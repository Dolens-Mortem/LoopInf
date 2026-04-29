from tkinter import filedialog, messagebox
import tkinter as tk
import cv2
from PIL import Image
import imagehash



def open_file(video_app):
    file_path = filedialog.askopenfilename(
        filetypes=[("Видео файлы", "*.mp4 *.avi *.mov *.mkv")]
    )
    file_name = file_path.split("/")[-1]
    if file_path:
        video_app.video_path = file_path
        video_app.label.config(text=f"Выбрано:\n{file_name}")




def play_video(video_app):
    if not video_app.video_path:
        messagebox.showerror("Ошибка", "Сначала выбери видео")
        return
    cap = cv2.VideoCapture(video_app.video_path)
    hashes = []
    times = []
    success_lines = [[-1, -1, -1]]
    frame_index = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_index % video_app.step == 0:
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            h = imagehash.phash(img)
            hashes.append(h)
            times.append(frame_index)  # / fps
        frame_index += 1
    cap.release()

    for i in range(len(hashes)):
        for j in range(i + video_app.min_sequence, len(hashes)):

            match_count = 0
            for k in range(video_app.min_sequence):
                if j + k >= len(hashes) - 1:
                    break
                diff_threshold = hashes[i + k] - hashes[j + k]
                if diff_threshold < video_app.threshold:
                    match_count += 1
                else:
                    break

            end_i = i + match_count - 1
            end_j = j + match_count - 1

            if end_i >= len(times) or end_j >= len(times):
                continue

            if match_count >= video_app.min_sequence:
                print(
                    f"Повтор сцены: "
                    f"{times[i]:.2f}s - {times[i + match_count]:.2f}s "
                    f"≈ {times[j]:.2f}s - {times[j + match_count]:.2f}s"
                )

                if success_lines[-1][0] < times[j + match_count] - times[i]:
                    start = times[i]
                    end = times[j]
                    success_lines.append([end - start, start, end])

    video_app.start_time = success_lines[-1][1]
    video_app.end_time = success_lines[-1][2]
    print(success_lines)

    if video_app.start_time < 1 or video_app.end_time < 1:
        messagebox.showerror("Не найдено совподений!", "Попробуйте понизить интервал или точность!")
        return
    video_app.btn_dwn.config(state="normal")



def open_config(video_app):
    config_window = tk.Toplevel(video_app.root)
    config_window.title("Настройки")
    config_window.geometry("240x137")

    min_sequence_ent = tk.Entry(config_window)
    min_sequence_ent.grid(row=1, column=1, padx=5)

    min_sequence_ent.insert(0, str(video_app.min_sequence))
    label_min = tk.Label(config_window, text="Интервал: ")
    label_min.grid(row=1, column=0)


    threshold_ent = tk.Entry(config_window)
    threshold_ent.grid(row=2, column=1, padx=5)
    threshold_ent.insert(0, str(video_app.threshold))

    label_thr = tk.Label(config_window, text="Точность: ")
    label_thr.grid(row=2, column=0)


    step_ent = tk.Entry(config_window)
    step_ent.grid(row=3, column=1, padx=5)

    step_ent.insert(0, str(video_app.step))
    label_stp = tk.Label(config_window, text="Шаг: ")
    label_stp.grid(row=3, column=0)


    btn_accept = tk.Button(config_window, text="Подтвердить", command=lambda: accept_config(video_app, config_window, min_sequence_ent.get(), threshold_ent.get(), step_ent.get()))
    btn_accept.grid(row=4, column=1, padx=5)



def accept_config(video_app, config_window, min_sequence_ent, threshold_ent, step_ent):
    config_window.destroy()
    video_app.min_sequence = int(min_sequence_ent)
    video_app.threshold = int(threshold_ent)
    video_app.step = int(step_ent)



def download_video(video_app):
    file_path_for_dwnld = filedialog.askdirectory()
    cap = cv2.VideoCapture(video_app.video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    print(file_path_for_dwnld)
    out = cv2.VideoWriter(file_path_for_dwnld + "/loopinf_video.mp4", fourcc, fps, (width, height))

    start_frame = video_app.start_time
    end_frame = video_app.end_time

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    current_frame = start_frame

    while current_frame <= end_frame:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        current_frame += 1
    cap.release()
    out.release()