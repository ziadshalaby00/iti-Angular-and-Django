import { Component } from '@angular/core';
import { ContentItemComponent } from '../content-item/content-item.component';

@Component({
  selector: 'app-content',
  imports: [ContentItemComponent],
  templateUrl: './content.component.html',
  styleUrl: './content.component.css'
})
export class ContentComponent {
  title = 'content'
}
