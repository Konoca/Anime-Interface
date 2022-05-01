import { Component } from '@angular/core';
import { Anime, UpdateAnimeData, UpdateAnimeEpData } from './anime';
import { AnimeApiService } from './anime-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  rows: Anime[] = []

  displayDialog: boolean = false;
  selectedAnime: any = {name: ""};

  constructor(
    private animeApi: AnimeApiService
  ) { }

  ngOnInit() {
    this.getData();
  }

  getData() {
    this.rows = [];
    this.animeApi.getAnime().subscribe((data: any) => {
      let animes: Anime[] = [];
      for (let anime in data) {
        const animeData = data[anime];
        animes.push(animeData);
      }
      this.rows = animes;
    })
  }

  selectAnime(anime: Anime) {
    this.selectedAnime = anime;
    this.displayDialog = true;
  }

  isEpWatched(ep: any) {
    return this.selectedAnime.watched.includes(ep);
  }

  watchEp(ep: any) {
    this.animeApi.openAnime(this.selectedAnime.name, ep).subscribe((r) => {});
  }

  markEpWatched(ep: any) {
    const isWatched = this.isEpWatched(ep);
    const ep_data: UpdateAnimeEpData = {name: this.selectedAnime.name, episode: ep, watched: isWatched};

    this.animeApi.updateAnime(ep_data).subscribe((r) => {
      this.getData();
    })

    // this.animeApi.setWatched(this.selectedAnime.name, ep, isWatched).subscribe((r) => {
    //   this.getData();
    // })
  }

  deleteEp(ep: any) {
    this.animeApi.deleteAnime(this.selectedAnime.name, ep).subscribe((r) => {
      this.getData();
    });
  }

  onEditComplete(event: any) { 
    const anime = event.data;
    const anime_data: UpdateAnimeData = {name: anime.name, broadcast: anime.broadcast, description: anime.description};

    this.animeApi.updateAnime(anime_data).subscribe((r) => {
      this.getData();
    })
  }
}
