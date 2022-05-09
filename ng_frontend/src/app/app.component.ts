import { Component, ViewChild } from '@angular/core';
import { Anime, NyaaSearchResult, UpdateAnimeData, UpdateAnimeEpData } from './anime';
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

  db_mode: boolean = false;
  title: string = "Anime Interface"

  addDialog: boolean = false;
  newAnime: any = {};
  
  searchAnimeDialog: boolean = false;
  searchAnimeValue: string = "";
  searchResults: NyaaSearchResult[] = [];

  @ViewChild('dt') dt: any;
  @ViewChild('dt2') dt2: any;

  constructor(
    private animeApi: AnimeApiService
  ) { }

  ngOnInit() {
    this.refresh()
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

  getMode() {
    this.animeApi.getMode().subscribe((data: any) => {
      if (data.Mode == 'DB') {
        this.db_mode = true;
        this.title = "Anime Database"
      }
      else {
        this.db_mode = false;
        this.title = "Anime Interface"
      }
    })
  }

  refresh() {
    this.getData();
    this.getMode();
  }

  selectAnime(anime: Anime) {
    this.selectedAnime = anime;
    this.displayDialog = true;
    this.dt2.first = 0
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
  }

  deleteEp(ep: any) {
    this.animeApi.deleteAnime(this.selectedAnime.name, ep).subscribe((r) => {
      this.getData();
      this.selectedAnime.episodes = this.selectedAnime.episodes.filter(function(e: any) { return e !== ep });
    });
  }

  onEditComplete(event: any) { 
    const anime = event.data;
    const anime_data: UpdateAnimeData = {name: anime.name, broadcast: anime.broadcast, description: anime.description};

    this.animeApi.updateAnime(anime_data).subscribe((r) => {
      this.getData();
    })
  }

  add() {
    if (this.db_mode) {
      this.newAnime = {};
      this.addDialog = true;
    }
    else {
      this.searchAnimeValue = "";
      this.searchResults = [];
      this.searchAnimeDialog = true;
    }
  }

  searchAnime() {
    this.animeApi.searchAnime({query: this.searchAnimeValue}).subscribe((r: any) => {
      this.searchResults = r
    })
  }

  downloadAnime(anime: NyaaSearchResult) {
    const wind = window.open(anime.magnet)
    setTimeout(function(){
      wind?.close()
    }, 1000);
  }

  findAnime(anime: Anime) {
    this.searchAnimeValue = anime.name;
    this.searchAnime()
    this.searchAnimeDialog = true;
  }

  addAnime() {
    if (this.newAnime.name == undefined)
      return

    let newAnime: Anime = {
      name: this.newAnime.name,
      description: this.newAnime.description || '',
      broadcast: this.newAnime.broadcast || '',
      episodes: [],
      watched: []
    }

    if (this.newAnime.episodeCount != null) {
      for (let i = 1; i <= this.newAnime.episodeCount; i++) {
        newAnime.episodes.push(i);
      }
    }
    if (this.newAnime.watchedCount != undefined) {
      for (let i = 1; i <= this.newAnime.watchedCount; i++) {
        newAnime.watched.push(i);
      }
    }

    this.animeApi.postAnime(newAnime).subscribe((r) => {
      this.addDialog = false;
      this.newAnime = {};
      this.getData();
    })
  }

  applyFilterGlobal($event: any, stringVal: any) {
    this.dt!.filterGlobal($event.target.value, stringVal);
  }
}
