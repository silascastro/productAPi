import { Review } from './../models/review';

import { CRUDAPP } from './../constants/endpoints';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ReviewService {
  constructor(private http: HttpClient) {}

  public getReviews(id: number): Observable<Review[]> {
    return this.http.get<Review[]>(CRUDAPP.REVIEW(id));
  }

  public postReview(data: object): Observable<Review[]> {
    return this.http.post<Review[]>(CRUDAPP.REVIEWS, data);
  }
}
