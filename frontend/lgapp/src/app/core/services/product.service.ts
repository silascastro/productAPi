import { Category } from './../models/category';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Product } from '../models/product';
import { CRUDAPP } from './../constants/endpoints';

@Injectable({
  providedIn: 'root',
})
export class ProductService {
  constructor(private http: HttpClient) {}

  public getAllProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(CRUDAPP.PRODUCTS);
  }

  public getOneProduct(id: number): Observable<Product> {
    return this.http.get<Product>(CRUDAPP.PRODUCT(id));
  }

  public createProduct(data): Observable<any> {
    return this.http.post(CRUDAPP.PRODUCTS, data);
  }

  public updateProduct(id: number, data): Observable<any> {
    return this.http.put(CRUDAPP.PRODUCT(id), data);
  }

  public deleteProduct(id: number): Observable<any> {
    return this.http.delete(CRUDAPP.PRODUCT(id));
  }

  public getOneCategorie(id: number): Observable<Category> {
    return this.http.get<Category>(CRUDAPP.CATEGORIE(id));
  }

  public getAllCategories(): Observable<Category[]> {
    return this.http.get<Category[]>(CRUDAPP.CATEGORIES);
  }
}
