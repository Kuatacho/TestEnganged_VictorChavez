import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home';
import { ProductComponent } from './pages/product/product';
import { CheckoutComponent } from './pages/checkout/checkout';
import { SuccessComponent } from './pages/success/success';

export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'product/:id', component: ProductComponent },
    { path: 'checkout', component: CheckoutComponent },
    { path: 'success', component: SuccessComponent },
];


