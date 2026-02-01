import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-success',
  standalone: true,
  imports: [],
  templateUrl: './success.html',
  styleUrls: ['./success.css']
})
export class SuccessComponent {
  constructor(private router: Router) {}

  goHome(){
    this.router.navigate(['/']);
  }
}
