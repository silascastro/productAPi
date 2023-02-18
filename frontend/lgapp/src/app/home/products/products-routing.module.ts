import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductDescriptionComponent } from './product-description/product-description.component';
import { ProductsComponent } from './products.component';

const routes: Routes = [
  {
    path: '',
    component: ProductsComponent,
  },

  {
    path: 'description/:id',
    component: ProductDescriptionComponent,
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ProductsRoutingModule {}
