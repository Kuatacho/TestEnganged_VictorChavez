import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';

export interface Product {
  id: string;
  name: string;
  description: string;
  price: number;
  image_url: string;
}

@Injectable({
  providedIn: 'root',
})
export class ProductService {

  private apiBase = 'http://localhost:5000/api';

  constructor(private http: HttpClient) { }

  getProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(`${this.apiBase}/products`);
  }

  getProductById(id: string): Observable<Product | undefined> {
    return this.http.get<Product>(`${this.apiBase}/products/${id}`);
  }
}
