#!/usr/bin/python
##-------------------------------##
## [Tabletop Simulator]Pokemon   ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
import asyncio
import sys
from pathlib import Path

import aiohttp
import bs4

from tts import Card, Deck


## Functions
async def parse_pokemon_urls(urls: list[str]) -> list[Card]:
    """Parses list of urls and returns a list of TTS Cards"""
    # -Internal Functions
    async def fetch_html_and_parse(url: str) -> Card:
        '''Generate TTS Card from HTML parsing'''
        async with session.get(url, raise_for_status=True) as resp:
            html: bs4.BeautifulSoup = bs4.BeautifulSoup(
                await resp.text(), 'html.parser'
            )
            name: str = html.find('span', class_='name').find('a').text
            img: str = html.find('div', class_='card-image-area').find('a').get('href')
            return Card(
                name=name, front_image=img,
                back_image=("http://cloud-3.steamusercontent.com/ugc/1768195981"
                            "648309989/9ABD9158841F1167D295FD1295D7A597E03A7487/"),
            )
    # -Body
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_html_and_parse(url))
        return await asyncio.gather(*tasks)


async def generate_deck_images(urls: dict[Path, str]) -> None:
    """Generates TTS images for saved objects"""
    # -Internal Functions
    async def download_image(file: Path, url: str) -> None:
        with open(file, 'wb') as f:
            async with session.get(url, raise_for_status=True) as resp:
                async for data in resp.content:
                    f.write(data)
    # -Body
    async with aiohttp.ClientSession() as session:
        tasks = []
        for file, url in urls.items():
            tasks.append(download_image(file.with_suffix('.png'), url))
        await asyncio.gather(*tasks)


## Body
urls: list[str] = []
decks: list[list[int]] = []
# -Parse Decks
for file in sys.argv[1:]:
    deck: list[int] = []
    with open(file, 'r') as f:
        for url in f.readlines():
            url = url.strip()
            if url not in urls:
                urls.append(url)
            deck.append(urls.index(url))
    decks.append(deck)
cards: list[Card] = asyncio.run(parse_pokemon_urls(urls))
# -Generate Deck Files
images: dict[Path, str] = {}
for i, deck in enumerate(decks):
    path = Path(sys.argv[i + 1]).with_suffix('.json')
    deck = Deck(*[cards[id_] for id_ in deck])
    deck.to_file(path)
    images[path] = deck.cards[0].front_image
# -Generate Deck Images
asyncio.run(generate_deck_images(images))
