import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { NewAccComponent } from './new-acc/new-acc.component';

const routes: Routes = [
	{ path: '', component: HomeComponent },
	{ path: 'new-acc', component: NewAccComponent },
	{ path: 'login', component: LoginComponent },
	{ path: 'home', component: HomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
