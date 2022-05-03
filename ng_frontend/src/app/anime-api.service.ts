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

  getMode() {
    return this.httpClient.get('http://127.0.0.1:8000/mode');
  }

  openAnime(animeName: string, episode: string) {
    return this.httpClient.get(`http://127.0.0.1:8000/watch?name=${animeName}&episode=${episode}`);
  }
  
  deleteAnime(animeName: string, episode: string) {
    return this.httpClient.delete(`http://127.0.0.1:8000/anime?name=${animeName}&episode=${episode}`);
  }

  updateAnime(data: any) {
    return this.httpClient.put('http://127.0.0.1:8000/anime', data)
  }
}
