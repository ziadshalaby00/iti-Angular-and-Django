import { Component } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';

@Component({
  selector: 'app-root',
  imports: [],
  template: ``,
})
export class App {
  name = 'Angular';
}

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes)
  ]
});
