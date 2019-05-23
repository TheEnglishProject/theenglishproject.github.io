import { NgModule } from '@angular/core';
import {
  MatButtonModule, MatToolbarModule, MatCheckboxModule, MatIconModule
} from '@angular/material';

@NgModule({
  exports: [
    MatButtonModule,
    MatToolbarModule,
    MatCheckboxModule,
    MatIconModule
  ]
})
export class MaterialModule {

}
