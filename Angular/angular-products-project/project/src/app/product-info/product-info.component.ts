import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

import { ApiService } from '../api.service';

@Component({
  selector: 'app-product-info',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-info.component.html',
  styleUrl: './product-info.component.css'
})
export class ProductInfoComponent {
  product: any = {}

  constructor(private route: ActivatedRoute, private apiService: ApiService){
    let id: number = Number(this.route.snapshot.params['id']);
    this.GetPosts(id)
  }
  
  GetPosts(id: number) {

    this.apiService.getPosts(id).subscribe({
      next: (data) => {
        this.product = data;
      },
      error: (error) => console.error(error),
      complete: () => console.log('Completed')
    });

  }
}
