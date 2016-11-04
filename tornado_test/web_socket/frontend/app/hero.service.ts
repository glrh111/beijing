/**
 * Created by glrh11 on 16-11-3.
 */
import { Injectable } from '@angular/core';

import { Hero } from './hero'
import { HEROES } from './mock-heroes';

@Injectable()
export class HeroService {
    get_heroes(): Promise<Hero[]> {
        return Promise.resolve(HEROES);
    }

    get_heroes_slowly(): Promise<Hero[]> {
        return new Promise<Hero[]>(resolve =>
            setTimeout(resolve, 2000))
            .then(
                ()=>
                this.get_heroes()
            );
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