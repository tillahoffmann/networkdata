from pathlib import Path
import requests
from tqdm import tqdm


root = Path('addhealth/raw')
root.mkdir(exist_ok=True)

for i in tqdm(range(1, 85)):
    for filename in [f'comm{i}.dat', f'comm{i}_att.dat']:
        # Only fetch the file if we haven't already downloaded it.
        path = root / filename
        if path.is_file():
            continue

        # Get the data file from Linton Freeman's webpage via the web archive as he's deceased.
        try:
            url = f'https://web.archive.org/web/0if_/http://moreno.ss.uci.edu/{filename}'
            response = requests.get(url)
            response.raise_for_status()
            with open(path, 'w') as fp:
                fp.write(response.text)
        except Exception as ex:
            # We expect that the download will fail for community 48 as it's not archived.
            print(f'failed to retrieve {url}: {ex}')
