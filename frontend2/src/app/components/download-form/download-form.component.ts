import { Component } from '@angular/core';
import { SoundCloudService } from '../../services/scdl.service';

@Component({
  selector: 'app-download-form',
  templateUrl: './download-form.component.html',
  styleUrls: ['./download-form.component.css'],
  standalone: false,
})
export class DownloadFormComponent {
  soundcloudUrl: string = '';
  isLoading: boolean = false;

  constructor(private soundCloudService: SoundCloudService) {}

  downloadTrack() {
    if (!this.soundcloudUrl.trim()) {
      alert('Please enter a valid URL.');
      return;
    }
    this.isLoading = true;

    this.soundCloudService.downloadTrack(this.soundcloudUrl).subscribe({
      next: () => {
        this.isLoading = false;
        alert('Download started!');
      },
      error: () => {
        this.isLoading = false;
        alert('Error downloading track.');
      },
    });
  }
}
