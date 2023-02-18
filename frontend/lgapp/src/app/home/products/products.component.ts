import { FeedbackService } from './../../core/services/feedback.service';
import { UploadImageService } from './../../core/services/upload-image.service';

import { ProductService } from './../../core/services/product.service';

import { MatDialog } from '@angular/material/dialog';
import { FormBuilder } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { NewProductModalComponent } from 'src/app/shared/new-product-modal/new-product-modal.component';
import { Product } from 'src/app/core/models/product';
import { UPLOADS } from 'src/app/core/constants/common';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss'],
  providers: [UploadImageService, FeedbackService, ProductService],
})
export class ProductsComponent implements OnInit {
  public loading = false;
  public uploadUrl = UPLOADS;

  public form = this.fb.group({
    products: '',
  });
  constructor(
    private fb: FormBuilder,
    private dialog: MatDialog,
    private productService: ProductService,
    private feedbackService: FeedbackService
  ) {}

  public ngOnInit(): void {
    this.getAllProducts();
  }

  public getAllProducts(): void {
    this.loading = true;
    setTimeout(() => {
      this.productService.getAllProducts().subscribe((result: Product[]) => {
        this.products.setValue(result);
        this.loading = false;
      });
    }, 1000);
  }

  public openCreateProductModal(): void {
    this.dialog
      .open(NewProductModalComponent, {
        disableClose: true,
        height: '550px',
        width: '500px',
      })
      .afterClosed()
      .subscribe((result) => {
        if (result) {
          this.createMovie(result);
        }
      });
  }

  public createMovie(data): void {
    this.productService.createProduct(data).subscribe(
      (result) => {
        this.getAllProducts();
        this.feedbackService.showFeedbackSnack(
          'Produto cadastrado com sucesso!'
        );
      },
      (err) => {
        this.feedbackService.showFeedbackSnack('erro ao cadastrar Produto!');
      }
    );
  }

  public get products(): any {
    return this.form.get('products');
  }
}
