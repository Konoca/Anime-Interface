import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AnimeApiService {

  constructor(private httpClient: HttpClient) { }

  getAnime() {
    return this.httpClient.get('http://127.0.0.1:8000/anime');
  }

  openAnime(animeName: string, episode: string) {
    return this.httpClient.get(`http://127.0.0.1:8000/anime?name=${animeName}&episode=${episode}`);
  }

  setWatched(animeName: string, episode: string, watched: boolean) {
    return this.httpClient.request('PUT', `http://127.0.0.1:8000/anime?name=${animeName}&episode=${episode}&watched=${watched}`);
  }

  deleteAnime(animeName: string, episode: string) {
    return this.httpClient.delete(`http://127.0.0.1:8000/anime?name=${animeName}&episode=${episode}`);
  }
}
