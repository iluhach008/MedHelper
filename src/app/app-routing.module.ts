import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CabinetAdminPartComponent } from './admin_part/cabinet-admin-part/cabinet-admin-part.component';
import { MainAdminPartComponent } from './admin_part/main-admin-part/main-admin-part.component';


const routes: Routes = [
  { path: '', component: MainAdminPartComponent },
  { path: 'cabinets', component: CabinetAdminPartComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
