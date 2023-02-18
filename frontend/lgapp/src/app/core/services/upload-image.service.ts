import { UPLOAD } from './../constants/endpoints';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class UploadImageService {
  constructor(private http: HttpClient) {}

  public postImage(file: any): Observable<any> {
    const data: FormData = new FormData();
    data.append('file', file);

    return this.http.post(UPLOAD.IMAGES, data, {});
  }
}
