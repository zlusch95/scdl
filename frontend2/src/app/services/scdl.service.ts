import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class SoundCloudService {
  private apiUrl = 'http://localhost:8000/download';

  constructor(private http: HttpClient) {}

  downloadTrack(url: string): Observable<any> {
    return this.http.post(this.apiUrl, { url });
  }
}
