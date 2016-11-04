/**
 * Created by glrh11 on 16-10-31.
 */
import { Component } from '@angular/core';

import { Hero } from './hero';

@Component({
    moduleId: module.id,
    selector: 'hero-form',
    templateUrl: 'hero-form.component.html'
})

export class HeroFromComponent {
    powers = [
        'Really Smart',
        'Super Flexible',
        'Super Hot',
        'Weather Changer'
    ];

    model = new Hero(18, 'Wang Li', this.powers[0], 'AHaHa');

    submitted = false;

    on_submit() { this.submitted = true; }

    active = true;

    new_hero() {
        this.model = new Hero(42, '', '');
        this.active = false;
        setTimeout(() => this.active = true, 0);
    }

    // todo : remove this when we are done
    get diagnostic() { return JSON.stringify(this.model); }
}