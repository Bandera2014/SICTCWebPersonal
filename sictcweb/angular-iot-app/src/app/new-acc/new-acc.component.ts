import { Component, OnInit } from '@angular/core';
import { Account, NewAccount } from '../interfaces/accounts';
import { AccountsService } from '../services/accounts.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-new-acc',
  templateUrl: './new-acc.component.html',
  styleUrls: ['./new-acc.component.scss']
})
export class NewAccComponent implements OnInit {
  name: string;
  address: string;
  city: string;
  state: string;
  zip: string;
  newAcc: NewAccount;
 
  constructor(
    private accService: AccountsService,
    private router: Router
    ) { } 

  ngOnInit(): void {
  }

  newAccBtn() {
    this.newAcc = {
        Name: this.name.toUpperCase(),
        Address: this.address,
        City: this.city,
        State: this.state,
        Zip: this.zip
    }
    this.accService.addAccount(this.newAcc).subscribe((newAcc: NewAccount) => {
        this.router.navigate(['/login']);
    });
 }
 

}
