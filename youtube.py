#!/usr/bin/python3
# Author      : 'JB <officialtech@pm.me>'
# State       : 'Final'
# Created     : 'January 12, 2022'
# Tcl-version : '8.6'

from cgitb import text
import os
from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
from tkinter import ttk
import tkinter

class YoutubeDownloader:
    def __init__(self, master):
        self.intro = ttk.Label(master, text="You can download youtube video(s) from here!")
        self.intro.pack()

        self.website = ttk.Label(master, text="For more, contact us here, http://emotionaldiary.com")
        self.website.pack()

        self.youtube_link_label = ttk.Label(master, text="Paste youtube video link here!")
        self.youtube_link_label.pack(pady=15)

        self.youtube_link_box = ttk.Entry(width=50)
        self.youtube_link_box.insert(0, "Paste Video link here...")
        self.youtube_link_box.focus()
        self.youtube_link_box.pack(ipady=5)

        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=350, maximum=100)
        self.progress_bar.configure(mode="indeterminate")
        self.progress_bar.start()

        
        self.download_btn = ttk.Button(master, text="Download video", command=self.download_one_video)
        self.download_btn.pack(pady=10, padx=20)

        self.download_audio = ttk.Button(master, text="Download audio", command=self.download_audio)
        self.download_audio.pack(side="right", padx=20)

        self.download_playlist = ttk.Button(master, text="Download playlist", command=self.download_play_list)
        self.download_playlist.pack(side="left", pady=10, padx=20)
        

        self.message = ttk.Label(master, text="")
        self.message.pack(pady=20)
    

    def download_one_video(self):
        """Downloading video from given URL pyt the User """
        url = self.youtube_link_box.get()
        try:
            self.progress_bar.pack(pady=20)
            yt = YouTube(url)
        except VideoUnavailable:
            print(f"Video {url} is unavailable, skipping...")
            self.message.configure(text=f"Video {url} is unavailable, skipping...")
        else:
            print(f"Downloading video: {url}")
            os_name = os.name
            if os_name == 'nt':
                self.message.configure(text="Downloading video...")
                self.message.configure(text=str(yt.title))
                yt.streams.get_highest_resolution().download(output_path=f"C:/Users/{os.getlogin()}/Downloads")
            elif os_name == 'posix':
                self.message.configure(text="Downloading video...")
                self.message.configure(text=str(yt.title))
                yt.streams.get_highest_resolution().download(output_path=f"/home/{os.getlogin()}/Downloads")
            else:
                yt.streams.get_highest_resolution().download()

        self.progress_bar.configure(value=100)
        self.message.configure(text="Video downloaded! check your Downloads or current directory!")
        self.progress_bar.stop()

    def download_audio(self):
        """It will download the audio file of given youtube video link """
        url = self.youtube_link_box.get()
        self.message.configure(text="")
        try:
            yt = YouTube(url)
            print(yt.title)
        except VideoUnavailable:
            print(f'Video not available for {url}')
            self.message.configure(text="Audio not available...")
        else:
            os_name = os.name
            if os_name == 'nt':
                self.message.configure(text="Downloading audio...")
                output_file = yt.streams.get_audio_only().download(output_path=f"C:/Users/{os.getlogin()}/Downloads/")
                filename, extention = os.path.splitext(output_file)
                new_file_name = filename + ".mp3"
                os.rename(output_file, new_file_name)
            elif os_name == "posix":
                self.message.configure(text="Downloading audio...")
                output_file = yt.streams.get_audio_only().download(output_path=f"/home/{os.login()}/Downloads/")
                filename, extention = os.path.splitext(output_file)
                new_file_name = filename + ".mp3"
                os.rename(output_file, new_file_name)
            else:
                output_file = yt.streams.get_audio_only().download()
                filename, extention = os.path.splitext(output_file)
                new_file_name = filename + ".mp3"
                os.rename(output_file, new_file_name)
        self.message.configure(text="Audio downloaded! check your current/downloads directory!")

    def download_play_list(self):
        """Download full playlist """
        url = self.youtube_link_box.get()
        try:
            p = Playlist(url)
            print(f'Downloading: {p.title}')
        except VideoUnavailable:
            print(f'Playlist not available for {url}')
            self.message.configure(text="Playlist not available...")
        else:
            os_name = os.name
            if os.name == "nt":
                self.message.configure(text=str(p.title))
                self.message.configure(text="Downloading video...")
                for video in p.videos:
                    video.streams.get_highest_resolution().download(output_path=f"C:/Users/{os.getlogin()}/Downloads/{p.title}/")

            elif os_name == "posix":
                self.message.configure(text=str(p.title))
                self.message.configure(text="Downloading video...")
                for video in p.videos:
                    video.streams.get_highest_resolution().download(output_path=f"C:/Users/{os.getlogin()}/Downloads/{p.title}/")
            else:
                for video in p.videos:
                    video.streams.get_highest_resolution().download()

        self.message.configure(text="Playlist downloaded...")
        self.message.configure(background="green")




def main():
    root = tkinter.Tk()
    root.geometry("620x400")
    root.resizable(False, False)
    root.title("Youtube Downloader by ED")
    app = YoutubeDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()
