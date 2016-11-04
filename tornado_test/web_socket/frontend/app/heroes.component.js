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
var hero_service_1 = require('./hero.service');
var router_1 = require("@angular/router");
var HeroesComponent = (function () {
    function HeroesComponent(hero_service, router) {
        this.hero_service = hero_service;
        this.router = router;
    }
    HeroesComponent.prototype.on_select = function (hero) {
        this.selected_hero = hero;
    };
    HeroesComponent.prototype.get_heroes = function () {
        var _this = this;
        this.hero_service.get_heroes().then(function (heroes) {
            return _this.heroes = heroes;
        });
    };
    HeroesComponent.prototype.goto_detail = function () {
        if (this.selected_hero) {
            var link = ['/detail', this.selected_hero.id];
            this.router.navigate(link);
        }
    };
    HeroesComponent.prototype.ngOnInit = function () {
        this.get_heroes();
    };
    HeroesComponent = __decorate([
        core_1.Component({
            selector: 'my-heroes',
            templateUrl: 'templates/heros.html',
            styleUrls: ['static/heroes.css',]
        }), 
        __metadata('design:paramtypes', [hero_service_1.HeroService, router_1.Router])
    ], HeroesComponent);
    return HeroesComponent;
}());
exports.HeroesComponent = HeroesComponent;
// export class AppComponent {
//   // get data from
//   private banner_url = 'http://api.kitty.live/v1/banner/list?platform=2';
//   public banners = [];
//   constructor (http: Http) {
//     http.get(this.banner_url)
//         .subscribe((res:Response) => this.banners = res.json().banners);
//   }
// }
//# sourceMappingURL=heroes.component.js.map