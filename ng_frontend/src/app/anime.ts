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
    watched: string;
}

export interface UpdateAnimeData {
    name: string;
    broadcast: string;
    description: string;
}