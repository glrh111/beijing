/**
 * Created by glrh11 on 16-11-3.
 */
import {Component, OnInit} from "@angular/core";
import { Router } from '@angular/router'

import {Hero} from "./hero";
import {HeroService} from "./hero.service";

@Component({
    // moduleId: module.id,
    selector: 'my-dashboard',
    templateUrl: 'templates/dashboard.html',
    styleUrls: [
        'static/dashboard.component.css'
    ]
})

export class DashboardComponent implements OnInit {

    heroes: Hero[] = [];

    constructor(
        private hero_service: HeroService,
        private router: Router,
    ){}

    ngOnInit(): void {
        this.hero_service.get_heroes()
            .then(
                heroes=>
                this.heroes = heroes.slice(1, 5)
            );
    }

    goto_detail(hero: Hero): void {
        let link = ['/detail', hero.id];
        this.router.navigate(link);
    }
}