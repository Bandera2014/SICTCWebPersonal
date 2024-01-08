import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Account } from '../../core/interfaces/accounts';
import { AccountsService } from '../../core/services/accounts.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auth-form',
  templateUrl: './auth-form.component.html',
  styleUrls: ['./auth-form.component.scss']
})
export class AuthFormComponent implements OnInit {

  constructor(
	private accService: AccountsService,
	private router: Router) {
acc: Account = {
    Id: null,
    Name: null,
    Address: '',
    City: '',
    State: '',
    Zip: '',
    CreatedDate: '',
  };

  accounts: Account[]

  formGroup = new FormGroup({
    name: new FormControl('', Validators.required),
    id: new FormControl(-1, Validators.required),
  });

  }

  ngOnInit(): void {
this.accService.getAccounts().subscribe((accounts: Account[]) => {
      this.accounts = accounts;
    })
  }

submitBtn() {
    this.accounts.forEach((account: Account) => {
      if (account.Id === Number(this.acc.Id) && account.Name === this.acc.Name) {
        this.router.navigate(['home']);
      }
    })
  }


}
