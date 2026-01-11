from gtts import gTTS
import os

# Folder tempat file teks cowok
cowok_folder = "pantun"

# --------- Generate MP3 dari folder cowok ---------
if os.path.exists(cowok_folder):
    for filename in os.listdir(cowok_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(cowok_folder, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read().strip()

            if text:
                tts = gTTS(text=text, lang="id", slow=False)
                mp3_name = filename.replace(".txt", ".mp3")
                tts.save(mp3_name)
                print(f"Generated {mp3_name}")
            else:
                print(f"File {filename} kosong, dilewati.")
else:
    print(f"Folder '{cowok_folder}' tidak ditemukan!")

# --------- Generate MP3 dari root repo (cewek) ---------
for filename in os.listdir("."):
    if filename.endswith(".txt") and not filename.startswith(cowok_folder):
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read().strip()

        if text:
            tts = gTTS(text=text, lang="id", slow=False)
            mp3_name = filename.replace(".txt", ".mp3")
            tts.save(mp3_name)
            print(f"Generated {mp3_name}")
        else:
            print(f"File {filename} kosong, dilewati.")
