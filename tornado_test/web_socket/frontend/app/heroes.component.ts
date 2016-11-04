import {Component, OnInit} from '@angular/core';
import {Http, Response} from '@angular/http';

import { Hero } from './hero';
import { HeroService } from './hero.service'
import { Router } from "@angular/router";

@Component({
    selector: 'my-heroes',
    templateUrl: 'templates/heros.html',
    styleUrls: ['static/heroes.css',]
})
export class HeroesComponent implements OnInit {

    constructor (
        private hero_service: HeroService,
        private router: Router
    ) {}

    heroes: Hero[];
    selected_hero: Hero;

    on_select(hero: Hero):void {
        this.selected_hero = hero;
    }

    get_heroes(): void {
        this.hero_service.get_heroes().then(
            heroes =>
            this.heroes = heroes
        );
    }

    goto_detail(): void {
        if (this.selected_hero) {
            let link = ['/detail', this.selected_hero.id];
            this.router.navigate(link);
        }
    }

    ngOnInit(): void {
        this.get_heroes();
    }

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
