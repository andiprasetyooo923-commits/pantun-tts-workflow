from gtts import gTTS
import os

# Folder tempat file teks pantun
folder = "pantun"

# Pastikan folder ada
if not os.path.exists(folder):
    print(f"Folder '{folder}' tidak ditemukan!")
    exit(1)

# Loop semua file .txt di folder
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().strip()

        if text:  # pastikan teks tidak kosong
            # Generate MP3
            tts = gTTS(text=text, lang="id", slow=False)
            mp3_name = filename.replace(".txt", ".mp3")
            tts.save(mp3_name)
            print(f"Generated {mp3_name}")
        else:
            print(f"File {filename} kosong, dilewati.")
