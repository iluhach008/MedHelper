import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainAdminPartComponent } from './admin_part/main-admin-part/main-admin-part.component';
import { CabinetAdminPartComponent } from './admin_part/cabinet-admin-part/cabinet-admin-part.component';

@NgModule({
  declarations: [
    AppComponent,
    MainAdminPartComponent,
    CabinetAdminPartComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
