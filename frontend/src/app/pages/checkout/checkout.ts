import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterModule, ActivatedRoute } from '@angular/router';
import { OrderService } from '../../services/order';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-checkout',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterModule],
  templateUrl: './checkout.html',
  styleUrls: ['./checkout.css']
})
export class CheckoutComponent implements OnInit {

  checkoutForm!: FormGroup;
  productId: string | null = null;
  submitting = false;

  constructor(
    private fb: FormBuilder,
    private orderService: OrderService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.checkoutForm = this.fb.group({
      name: ['', [Validators.required, Validators.pattern("^[A-Za-zÀ-ÿ\u00f1\u00d1 ]+$")]],
      last_name: ['', [Validators.required, Validators.pattern("^[A-Za-zÀ-ÿ\u00f1\u00d1 ]+$")]],
      email: ['', [Validators.required, Validators.email, Validators.pattern("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$")]]
    });

    // Read product_id from query params if provided
    this.productId = this.route.snapshot.queryParamMap.get('product_id');
  }

  onSubmit(): void {
    if (this.checkoutForm.valid && !this.submitting) {
      this.submitting = true;
      const order = {
        ...this.checkoutForm.value,
        product_id: this.productId || 'd0f8f8a0-f8f8-f8f8-f8f8-f8f8f8f8f8f8'
      };
      this.orderService.createOrder(order).subscribe({
        next: () => {
          this.submitting = false;
          this.router.navigate(['/success']);
        },
        error: () => {
          this.submitting = false;
          // simple UX: show an alert and keep user on form so they can retry
          alert('Ocurrió un error al crear la orden. Por favor intenta de nuevo.');
        }
      });
    }
  }
}
