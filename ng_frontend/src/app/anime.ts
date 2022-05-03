export interface Anime {
    name: string;
    description: string;
    broadcast: string;
    episodes: number[];
    watched: number[];
}

export interface UpdateAnimeEpData {
    name: string;
    episode: string;
    watched: boolean;
}

export interface UpdateAnimeData {
    name: string;
    broadcast: string;
    description: string;
}

export interface APIMode {
    mode: string;
}

export interface NyaaSearchResult {
    category: string;
    url: string;
    name: string;
    download_url: string;
    magnet: string;
    size: string;
    date: string;
    seeders: string;
    leechers: string;
    completed_downloads: string;
}