import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { provideHttpClient } from '@angular/common/http';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatProgressSpinner } from '@angular/material/progress-spinner';
import { MatToolbar } from '@angular/material/toolbar';
import { MatIcon } from '@angular/material/icon';

import { AppComponent } from './app.component';
import { DownloadFormComponent } from './components/download-form/download-form.component';
import { SoundCloudService } from './services/scdl.service';

@NgModule({
  declarations: [AppComponent, DownloadFormComponent],
  imports: [
    BrowserModule,
    FormsModule,
    BrowserAnimationsModule,
    MatInputModule,
    MatButtonModule,
    MatCardModule,
    MatProgressBarModule,
    MatProgressSpinner,
    MatToolbar,
    MatIcon,
  ],
  providers: [SoundCloudService, provideHttpClient()],
  bootstrap: [AppComponent],
})
export class AppModule {}
