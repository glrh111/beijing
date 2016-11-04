/**
 * Created by glrh11 on 16-11-3.
 */
import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';

import { Hero } from './hero';
import { HeroService } from './hero.service';

@Component({
    selector: 'my-hero-detail',
    templateUrl: 'templates/hero-detail.html',
    styleUrls: ['static/hero-detail.component.css']
})
export class HeroDetailComponent implements OnInit {

    constructor(
        private hero_service: HeroService,
        private route: ActivatedRoute,
        private location: Location,
        public hero: Hero
    ){}

    ngOnInit(): void {
        this.route.params.forEach(
            (params: Params)=>
            {
                let id = +params['id'];
                this.hero_service.get_hero(id)
                    .then(hero=>
                        this.hero=hero
                    );
            }
        );
    }

    go_back(): void {
        this.location.back();
    }

}
