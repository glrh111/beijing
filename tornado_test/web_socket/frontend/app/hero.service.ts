/**
 * Created by glrh11 on 16-11-3.
 */
import { Injectable } from '@angular/core';

import { Hero } from './hero'
import {Http, Headers} from "@angular/http";

import 'rxjs/add/operator/toPromise';

@Injectable()
export class HeroService {
    // URL to web api
    private heroes_url = 'app/heroes';

    constructor(
        private http: Http
    ){}

    get_heroes(): Promise<Hero[]> {
        return this.http.get(this.heroes_url)
            .toPromise()
            .then(response=>response.json().data as Hero[]) // i change ES5 to ES 6
            .catch(this.handleError);
    }

    private handleError(error: any): Promise<any> {
        console.error('An error occurred', error);
        return Promise.reject(error.message || error);
    }

    get_hero(id: number): Promise<Hero> {
        return this.get_heroes()
            .then(heroes=>
                heroes.find(hero=>
                    hero.id === id
                )
            );
    }
}