import { Component } from '@angular/core';
import {Http, Response} from '@angular/http'

import { Hero } from './hero'
@Component({
  selector: 'my-app',
  templateUrl: 'templates/heros.html'
})

export class AppComponent {
  title = 'Heros';
  heroes = [
      new Hero(1, 'Wang'),
      new Hero(2, 'Da'),
      new Hero(3, 'Li'),
      new Hero(4, 'DeDeDe')
  ];
  my_hero = this.heroes[0];
}

// export class AppComponent {
//   // get data from
//   private banner_url = 'http://api.kitty.live/v1/banner/list?platform=2';
//   public banners = [];
//   constructor (http: Http) {
//     http.get(this.banner_url)
//         .subscribe((res:Response) => this.banners = res.json().banners);
//   }
// }
