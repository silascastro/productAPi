import { RouterModule } from '@angular/router';
import { SharedModule } from './../../shared/shared.module';
import { ProductsRoutingModule } from './products-routing.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductsComponent } from './products.component';
import { ProductDescriptionComponent } from './product-description/product-description.component';
import { NewReviewComponent } from './product-description/new-review/new-review.component';

@NgModule({
  declarations: [ProductsComponent, ProductDescriptionComponent, NewReviewComponent],
  imports: [CommonModule, ProductsRoutingModule, SharedModule, RouterModule],
})
export class ProductsModule {}
