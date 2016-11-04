import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms'

import { HeroFromComponent } from './hero-form.component';
import { AppComponent } from "./app.component";

@NgModule({
    imports: [
        BrowserModule,
        FormsModule
    ],
    declarations: [
        AppComponent,
        HeroFromComponent
    ],
    bootstrap: [
        AppComponent
    ]
})

export class AppModule {}

