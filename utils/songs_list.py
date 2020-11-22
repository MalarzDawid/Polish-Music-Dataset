import os
import pandas as pd
import lyricsgenius

genius_token = ("")


COLUMNS = ["Artist", "Title"]



def get_songs(artist_name, count, filename):
    try:
        genius = lyricsgenius.Genius(genius_token, timeout=10)
        df = pd.DataFrame(columns=COLUMNS)
        if not os.path.isfile(f"./data/{filename}.csv"):
            df.to_csv(f"./data/{filename}.csv")
        try:
            artist = genius.search_artist(artist_name, max_songs=count)
        except ValueError:
            "Problem with search_artist"
        if artist is not None:
            for song in artist.songs:
                try:
                    df = df.append({'Artist': song.artist,
                                    'Title': song.title}, ignore_index=True)
                    df.to_csv(f"./data/{filename}.csv", mode="a", index=False,
                              header=False)
                    df = pd.DataFrame(columns=COLUMNS)
                except ValueError:
                    "Skiping..."
    except ValueError:
        "Disconected..."
