from NyaaPy import nyaa
from subprocess import call

def search(query: str):
    nyaa_search = nyaa.Nyaa()

    results = nyaa_search.search(query, filters=2)

    new_results = []
    for result in results:
        new_results.append({
            'category': result.category,
            'url': result.url,
            'name': result.name,
            'download_url': result.download_url,
            'magnet': result.magnet,
            'size': result.size,
            'date': result.date,
            'seeders': result.seeders,
            'leechers': result.leechers,
            'completed_downloads': result.completed_downloads
        })

    return new_results


def download(url: str):
    call(['qbittorrent-nox', url])

