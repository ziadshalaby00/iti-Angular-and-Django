import { Component } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';

import { provideHttpClient } from '@angular/common/http'; // استيراد HttpClientModule

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [],
  template: ``,
})
export class App {
  name = 'Angular';
}

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    provideHttpClient()
  ]
}).catch(err => console.error(err));