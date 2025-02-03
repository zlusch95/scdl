import { TestBed } from '@angular/core/testing';

import { SoundCloudService } from './scdl.service';

describe('ScdlService', () => {
  let service: SoundCloudService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SoundCloudService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
