import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private url = 'https://dummyjson.com/products';

  constructor(private http: HttpClient) { }

  getPosts(id: any = null): Observable<any> {
    if(id) {
      return this.http.get(`${this.url}/${id}`);
    }
    return this.http.get(this.url);
  }

}