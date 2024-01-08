import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthFormComponent } from './auth-form.component'; 
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [AuthFormComponent],
  imports: [
    CommonModule,
    ReactiveFormsModule
  ],
  exports: [
    AuthFormComponent,
    FormsModule,
    ReactiveFormsModule
  ]
})
export class AuthFormModule { }

