from scrapers import genius
from scrapers.config import CONFIG
import yaml
import time

if __name__ == "__main__":

    with open('artists.yaml') as file:
        yaml_data = yaml.load(file, Loader=yaml.FullLoader)
    genius.dataframe_init(filename=CONFIG['FILENAME'])
    for artist in yaml_data['Artists']:
        try:
            genius.get_songs(artist_name = artist, max_songs=CONFIG['COUNT'], filename=CONFIG['FILENAME'])
        except ConnectionError:
            time.sleep(5*60)
