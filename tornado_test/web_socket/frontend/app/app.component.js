"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var hero_1 = require('./hero');
var AppComponent = (function () {
    function AppComponent() {
        this.title = 'Heros';
        this.heroes = [
            new hero_1.Hero(1, 'Wang'),
            new hero_1.Hero(2, 'Da'),
            new hero_1.Hero(3, 'Li'),
            new hero_1.Hero(4, 'DeDeDe')
        ];
        this.my_hero = this.heroes[0];
    }
    AppComponent = __decorate([
        core_1.Component({
            selector: 'my-app',
            templateUrl: 'templates/heros.html'
        }), 
        __metadata('design:paramtypes', [])
    ], AppComponent);
    return AppComponent;
}());
exports.AppComponent = AppComponent;
// export class AppComponent {
//   // get data from
//   private banner_url = 'http://api.kitty.live/v1/banner/list?platform=2';
//   public banners = [];
//   constructor (http: Http) {
//     http.get(this.banner_url)
//         .subscribe((res:Response) => this.banners = res.json().banners);
//   }
// }
//# sourceMappingURL=app.component.js.map