import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { ApiService } from '../api.service';

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './products.component.html',
  styleUrl: './products.component.css'
})
export class ProductsComponent {
  products: any = []

  constructor(private apiService: ApiService) {
    this.GetPosts()
  }

  GetPosts() {

    this.apiService.getPosts().subscribe({
      next: (data) => {
        this.products = data;
      },
      error: (error) => console.error(error),
      complete: () => console.log('Completed')
    });

  }

}
