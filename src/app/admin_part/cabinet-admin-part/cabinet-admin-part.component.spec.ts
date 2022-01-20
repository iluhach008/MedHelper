import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CabinetAdminPartComponent } from './cabinet-admin-part.component';

describe('CabinetAdminPartComponent', () => {
  let component: CabinetAdminPartComponent;
  let fixture: ComponentFixture<CabinetAdminPartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CabinetAdminPartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CabinetAdminPartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
