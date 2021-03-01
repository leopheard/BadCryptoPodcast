from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon
plugin = Plugin()
url1 = "https://omny.fm/shows/badcrypto/playlists/podcast.rss"
url2 = "https://omny.fm/shows/cryptochick/playlists/podcast.rss"
url3 = "https://www.omnycontent.com/d/playlist/8edea6b9-fca4-41a1-83ee-aa76002b9dd8/c49b612f-7eb3-48d3-bde6-aa8c00ed740f/c925d231-cd4d-4ab0-9901-aa8c00ed742c/podcast.rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://www.omnycontent.com/d/playlist/8edea6b9-fca4-41a1-83ee-aa76002b9dd8/8f677bef-192a-4471-a50b-abcd002a30ee/5ec27e5e-3d28-4913-b240-abcd002a3106/image.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://podcastaddict.com/cache/artwork/thumb/2314341"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://podcastaddict.com/cache/artwork/thumb/2441877"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
