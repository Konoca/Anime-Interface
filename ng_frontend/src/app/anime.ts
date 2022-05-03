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