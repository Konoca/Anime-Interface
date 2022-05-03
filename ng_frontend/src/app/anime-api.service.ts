import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AnimeApiService {

  constructor(private httpClient: HttpClient) { }

  url = 'http://127.0.0.1:8000'

  getAnime() {
    return this.httpClient.get(this.url + '/anime');
  }

  getMode() {
    return this.httpClient.get(this.url + '/mode');
  }

  openAnime(animeName: string, episode: string) {
    return this.httpClient.get(this.url + `/watch?name=${animeName}&episode=${episode}`);
  }
  
  deleteAnime(animeName: string, episode: string) {
    return this.httpClient.delete(this.url + `/anime?name=${animeName}&episode=${episode}`);
  }

  updateAnime(data: any) {
    return this.httpClient.put(this.url + '/anime', data)
  }

  searchAnime(data: any) {
    return this.httpClient.put(this.url + '/search', data)
  }

  postAnime(data: any) {
    return this.httpClient.post(this.url + '/anime', data)
  }
}
