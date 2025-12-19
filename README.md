# ⚠️ Disclaimer
**This tool is for educational purposes only.**
Please respect YouTube's Terms of Service. Only download content if you have permission from the creator or if your usage falls under Fair Use guidelines. The creator of this tool is not responsible for any misuse. works on 1000+ websites

---

# 📹 Karanja's High-Quality YouTube Downloader

A robust Python command-line tool that downloads YouTube videos in the best available quality (1080p, 4K, etc.). It automatically merges video and audio streams to ensure you get a perfect, playable `.mp4` file every time.

## 🚀 Features
- **High Resolution Support:** Downloads 1080p/4K video (bypassing YouTube's separate stream limitations).
- **Data Saver:** Calculates and displays the estimated file size (MB) *before* you download.
- **Smart Formatting:** Uses `FFmpeg` to seamlessly merge video and audio.
- **Continuous Mode:** Download multiple videos in a row without restarting the program.

---

## 🛠️ Installation & Setup

### 1. Install Python
If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).
> **Important:** During installation, make sure to check the box that says **"Add Python to PATH"**.

### 2. Download this Code
1.  Click the green **Code** button at the top of this GitHub page.
2.  Select **Download ZIP**.
3.  Extract the folder to your Desktop.

### 3. Install FFmpeg (Crucial Step)
This tool requires **FFmpeg** to merge the high-quality video and audio streams. Choose the method that fits your skill level:

#### 🟢 Option A: Newbie Level (Easiest)
*Use this if you don't know what "System Environment Variables" are.*

1.  Download FFmpeg from this safe link: [ffmpeg-release-essentials.zip](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)
2.  Unzip the downloaded file (Right-click > Extract All).
3.  Open the extracted folder until you find a folder named `bin`.
4.  Inside `bin`, find the file named `ffmpeg.exe`.
5.  **Copy** `ffmpeg.exe` and **Paste** it into the **SAME FOLDER** as `downloader.py`.
    * *Your folder should look like this:*
      ```text
      📁 Youtube_Downloader
       ├── downloader.py
       ├── README.md
       └── ffmpeg.exe
      ```

#### 🔴 Option B: Developer Level (Cleanest)
*Use this if you are comfortable editing System Paths.*

1.  Download and extract FFmpeg to a permanent location (e.g., `C:\ffmpeg`).
2.  Add `C:\ffmpeg\bin` to your Windows **System Path** Environment Variables.
3.  Verify installation by typing `ffmpeg -version` in a new terminal.
4.  You do *not* need to copy any files into the script folder.

### 4. Install the Python Library
1.  Open the folder containing the script.
2.  Type `cmd` in the folder's address bar and press **Enter**.
3.  Run this command:
    ```bash
    pip install yt-dlp
    ```

---

## ▶️ How to Use

1.  Open your command prompt in the project folder.
2.  Run the script:
    ```bash
    python downloader.py
    ```
3.  **Paste the YouTube URL** when prompted.
4.  **Select your quality** (e.g., Type `1` for 1080p).
5.  Wait for the "Download complete!" message.
6.  The video will be saved in the same folder.

## 🤝 Contributing
Feel free to fork this repository and submit pull requests.

## 📄 License
This project is open-source and available for personal use.

