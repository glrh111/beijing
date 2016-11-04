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
/**
 * Created by glrh11 on 16-10-31.
 */
var core_1 = require('@angular/core');
var hero_1 = require('./hero');
var HeroFromComponent = (function () {
    function HeroFromComponent() {
        this.powers = [
            'Really Smart',
            'Super Flexible',
            'Super Hot',
            'Weather Changer'
        ];
        this.model = new hero_1.Hero(18, 'Wang Li', this.powers[0], 'AHaHa');
        this.submitted = false;
        this.active = true;
    }
    HeroFromComponent.prototype.on_submit = function () { this.submitted = true; };
    HeroFromComponent.prototype.new_hero = function () {
        var _this = this;
        this.model = new hero_1.Hero(42, '', '');
        this.active = false;
        setTimeout(function () { return _this.active = true; }, 0);
    };
    Object.defineProperty(HeroFromComponent.prototype, "diagnostic", {
        // todo : remove this when we are done
        get: function () { return JSON.stringify(this.model); },
        enumerable: true,
        configurable: true
    });
    HeroFromComponent = __decorate([
        core_1.Component({
            moduleId: module.id,
            selector: 'hero-form',
            templateUrl: 'hero-form.component.html'
        }), 
        __metadata('design:paramtypes', [])
    ], HeroFromComponent);
    return HeroFromComponent;
}());
exports.HeroFromComponent = HeroFromComponent;
//# sourceMappingURL=hero-form.component.js.map