import { Component, OnInit } from '@angular/core';
import { Product, ProductService } from '../../services/product';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './home.html',
  styleUrls: ['./home.css']
})
export class HomeComponent implements OnInit {

  products: Product[] = [];
  currentIndex = 0;

  constructor(private productService: ProductService) { }

  ngOnInit(): void {
    this.productService.getProducts().subscribe({
      next: (products) => this.products = products,
      error: () => alert('No se pudieron cargar los productos. Intenta más tarde.')
    });
  }

  prev(){
    if(this.products.length===0) return;
    this.currentIndex = (this.currentIndex -1 + this.products.length) % this.products.length;
  }

  next(){
    if(this.products.length===0) return;
    this.currentIndex = (this.currentIndex +1) % this.products.length;
  }
}
