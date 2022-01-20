import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MainAdminPartComponent } from './main-admin-part.component';

describe('MainAdminPartComponent', () => {
  let component: MainAdminPartComponent;
  let fixture: ComponentFixture<MainAdminPartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MainAdminPartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MainAdminPartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
