import { ReviewService } from './../../../core/services/review.service';
import { Category } from './../../../core/models/category';

import { ActivatedRoute, Router } from '@angular/router';
import { MatDialog } from '@angular/material/dialog';
import { ProductService } from './../../../core/services/product.service';
import { Component, OnInit } from '@angular/core';
import { UPLOADS } from 'src/app/core/constants/common';
import { Product } from 'src/app/core/models/product';
import { NewProductModalComponent } from 'src/app/shared/new-product-modal/new-product-modal.component';
import { FeedbackService } from 'src/app/core/services/feedback.service';

@Component({
  selector: 'app-product-description',
  templateUrl: './product-description.component.html',
  styleUrls: ['./product-description.component.scss'],
  providers: [FeedbackService, ProductService, ReviewService],
})
export class ProductDescriptionComponent implements OnInit {
  public id: number;
  public uploadUrl = UPLOADS;
  public loadingReviews = false;

  constructor(
    private productService: ProductService,
    private dialog: MatDialog,
    private router: ActivatedRoute,
    private fbService: FeedbackService,
    private routerNavigate: Router,
    private reviewService: ReviewService
  ) {}

  public product: Product = null;
  public reviews = [];
  public category: string = null;

  public ngOnInit(): void {
    this.router.params.subscribe((params) => {
      this.id = params.id;
    });
    this.loadingReviews = true;
    this.getProduct();
    this.getReviews();
  }

  public getProduct(): void {
    setTimeout(() => {
      this.productService.getOneProduct(this.id).subscribe(
        (response) => {
          this.loadingReviews = false;
          if (!response) {
            this.routerNavigate.navigate(['/products']);
          }

          this.product = response;
          this.getCategory(this.product.category_id);
        },
        (err) => {
          this.fbService.showFeedbackSnack('aconteceu um erro!');
        }
      );
    });
  }

  public getReviews(): any {
    this.reviewService.getReviews(this.id).subscribe((response) => {
      this.reviews = response;
    });
  }

  public getCategory(id: number): void {
    setTimeout(() => {
      this.productService.getOneCategorie(id).subscribe(
        (response: any | Category) => {
          if (!response) {
            this.routerNavigate.navigate(['/products']);
          }
          this.category = response.name;
        },
        (err) => {
          this.fbService.showFeedbackSnack('aconteceu um erro!');
        }
      );
    });
  }

  public openEditModal(): void {
    this.dialog
      .open(NewProductModalComponent, {
        data: {
          product: this.product,
        },
        disableClose: true,
        height: '550px',
        width: '500px',
      })
      .afterClosed()
      .subscribe((result) => {
        if (result) {
          this.updateProduct(result);
        }
      });
  }

  public updateData(event): void {
    this.getReviews();
  }

  public updateProduct(data): void {
    this.productService.updateProduct(this.id, data).subscribe(
      () => {
        this.fbService.showFeedbackSnack('Produto Atualizado com sucesso!');
        this.getProduct();
      },
      () => {
        this.fbService.showFeedbackSnack('erro ao Atualizar Produto!');
      }
    );
  }

  public deleteMovie(): void {
    this.productService.deleteProduct(this.id).subscribe(
      () => {
        this.fbService.showFeedbackSnack('Produto Removido com sucesso!');
        this.routerNavigate.navigate(['products']);
      },
      () => {
        this.fbService.showFeedbackSnack('erro ao Remover Produto!');
      }
    );
  }
}
