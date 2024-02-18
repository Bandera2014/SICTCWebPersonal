import { Component, OnInit } from '@angular/core';
import { Account, UpdateAccount } from '../interfaces/accounts';
import { Router } from '@angular/router';
import { AccountsService } from '../services/accounts.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  failedAtt: boolean = false;
  emptyField: boolean = false;
  updateInfo: boolean = false;
  accounts: Account[];
  acc: Account = null;
  idNum: number;
  name: string;
  address: string;
  city: string;
  state: string;
  zip: string;
  newAcc: UpdateAccount;
 
  constructor(
    private router: Router,
    private accService: AccountsService
  ) { }
 

  ngOnInit(): void {
    this.accService.getAccounts().subscribe((accs: Account[]) => {
      this.accounts = accs;
    })
  }
  deleteBtn(accId: number) {
    console.log("delete button pressed");
    this.accService.deleteAccount(accId).subscribe((acc: Account) => {
      this.acc = acc;
        this.accService.getAccounts().subscribe((accs: Account[]) => {
          this.accounts = accs;
          this.router.navigate(['/home'])
        })
    })
  }
  
  updateBtn(accId: number) {
    this.accService.getAccountById(accId).subscribe((acc: Account[]) => {
      this.acc = acc[0];
      this.idNum = accId;
      this.name = acc[0].Name;
      this.address = acc[0].Address;
      this.city = acc[0].City;
      this.state = acc[0].State;
      this.zip = acc[0].Zip;
  
    })
    this.failedAtt = false;
    this.updateInfo = true;
  }
  
  submitBtn() {
    this.newAcc = {
      Id: this.idNum,
      Name: this.name,
      Address: this.address,
      City: this.city,
      State: this.state,
      Zip: this.zip
    };
    if (this.name.length && this.address.length && this.city.length && this.state.length && this.zip.length) {
      this.emptyField = false;
      this.accService.updateAccount(this.newAcc).subscribe((newAcc: UpdateAccount) => {
        console.log(newAcc);
        if (newAcc.Id !== null) {
          this.router.navigate(['/login']);
        }
      })
    } else {
      this.emptyField = true;
    }

  }
 

}
