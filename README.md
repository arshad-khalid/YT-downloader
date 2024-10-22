# YouTube Video Downloader 🎥

This is a simple Python application to download YouTube videos with a graphical interface built using Tkinter. The app allows users to fetch the video thumbnail, choose the desired resolution, and download the video to their chosen location.

## Features
- Fetches video thumbnail from the provided YouTube link.
- Allows you to choose the resolution of the video (1080p, 720p, 480p, 360p).
- Choose the file name and save location.
- Provides a progress bar to track download progress.
- Multi-threaded to prevent freezing during downloads.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arshadkhalid/YT-downloader.git
   ```
2.	**Install the required dependencies:**
Make sure you have Python 3.x installed. Then install the following packages using pip:
   ```bash
 pip install tkinter
pip install pytube
pip install pillow
pip install requests
   ```
## How to Use
1.	Run the Python script:
   ```bash
   python yt_downloader.py
   ```
2.	Paste the YouTube video link into the provided field.
3.	Choose the desired resolution, save location, and file name (optional).
4.	Click Fetch Thumbnail to preview the video thumbnail.
5.	Once the thumbnail is fetched, the Download button will be enabled.
6.	Click Download to start downloading the video.

## Project Structure
```bash
youtube-video-downloader/
│
├── yt-downloader.py       # Main Python script
├── README.md              # Project documentation
└── screenshot.png         # Screenshot of the app
```

## Dependencies

	•	tkinter: For creating the GUI.
	•	pytube: For downloading YouTube videos.
	•	Pillow: For handling image processing (e.g., fetching thumbnails).
	•	requests: For making HTTP requests to fetch the video thumbnail.
	•	threading: For handling downloads in a separate thread to keep the UI responsive.

## Future Improvements

	•	Add support for playlist downloads.
	•	Add more resolution options.

## License

This project is licensed under the MIT License.

Happy downloading! 😎
