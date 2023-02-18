import { UploadImageService } from './../../../assets/app/core/services/upload-image.service';
import { ProductService } from './../../core/services/product.service';
import { Product } from './../../core/models/product';
import { Component, Inject, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-new-product-modal',
  templateUrl: './new-product-modal.component.html',
  styleUrls: ['./new-product-modal.component.scss'],
  providers: [ProductService, UploadImageService],
})
export class NewProductModalComponent implements OnInit {
  constructor(
    private dialogRef: MatDialogRef<NewProductModalComponent>,
    @Inject(MAT_DIALOG_DATA) private data: any,
    private fb: FormBuilder,
    private productService: ProductService,
    private uploadImageService: UploadImageService
  ) {}

  public fileUploaded = false;
  public productData: Product;
  public categories = [];

  public form = this.fb.group({
    name: ['', Validators.required],
    price: ['', Validators.required],
    category: ['', Validators.required],
    serie: ['', Validators.required],
    file: ['', Validators.required],
  });

  public ngOnInit(): void {
    const data = this.data;
    this.productData = data?.product;

    if (this.data) {
      this.name.setValue(this.productData.name);
      this.category.setValue(this.productData.category_id);
      this.serie.setValue(this.productData.serie);
      this.price.setValue(this.productData.price);
      this.file.setValidators(null);
    }

    this.productService.getAllCategories().subscribe((categories) => {
      this.categories = categories;
    });
  }

  public close(data?: any): void {
    this.dialogRef.close(data);
  }

  public setNewImage(event): void {
    const [file] = event.target.files;
    this.validationInputFile(file);
  }

  public validationInputFile(file): void {
    if (file) {
      if (this.isFileTypeCorrect(file)) {
        this.file.patchValue(file);
        this.fileUploaded = true;
      } else {
        this.file.setErrors({ fileIncorrect: true });
      }
    } else {
      this.fileUploaded = false;
    }

    this.form.markAsPristine({ onlySelf: true });
  }

  public isFileTypeCorrect(file: File): boolean {
    const acceptFileType = ['image/jpeg', 'image/jpg', 'image/png'];
    return acceptFileType.includes(file.type);
  }

  public clearFile(): void {
    this.fileUploaded = false;
    this.file.setValue(null);
  }

  public handlerCadastrar(): void {
    if (this.productData && !this.file.value) {
      const data = {
        name: this.name.value,
        category_id: this.category.value,
        serie: this.serie.value,
        price: this.price.value,
      };

      this.close(data);
    } else {
      this.uploadImage();
    }
  }

  public uploadImage(): void {
    const image = this.file.value;

    this.uploadImageService.postImage(image).subscribe(
      (response: any) => {
        const { filename } = response;
        const data = {
          name: this.name.value,
          category_id: this.category.value,
          serie: this.serie.value,
          price: this.price.value,
          image: filename,
        };

        this.close(data);
        this.fileUploaded = true;
      },
      ({ error }) => {
        this.fileUploaded = false;
        this.file.reset();
      }
    );
  }

  public get name(): any {
    return this.form.get('name');
  }

  public get category(): any {
    return this.form.get('category');
  }

  public get serie(): any {
    return this.form.get('serie');
  }

  public get price(): any {
    return this.form.get('price');
  }

  public get file(): any {
    return this.form.get('file');
  }
}
