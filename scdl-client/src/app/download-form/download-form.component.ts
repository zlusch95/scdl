import { Component } from '@angular/core';

@Component({
  selector: 'app-download-form',
  standalone: false,
  templateUrl: './download-form.component.html',
  styleUrl: './download-form.component.scss',
})
export class DownloadFormComponent {
  downloadTrack: any;
  soundcloudUrl: any;
  isLoading: any;
}
