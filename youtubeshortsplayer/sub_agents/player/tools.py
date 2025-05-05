from typing import List
import webbrowser
def video_player(urls: List[str]):
    for url in urls:
        print(f"Opening: {url}")
        webbrowser.open(url)