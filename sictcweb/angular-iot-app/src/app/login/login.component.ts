import { Account,NewAccount } from '../interfaces/accounts';
import { AccountsService } from '../services/accounts.service';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  idNum: number;
  username?: string;
  accName?: string;
  failedAtt?:  boolean;

  constructor(
	private accService: AccountsService,
	private router: Router
  ) { }

  ngOnInit(): void {
  }

   loginBtn() {
       this.username = this.username.toUpperCase();
       this.accService.getAccountById(this.idNum).subscribe((accounts: Account[]) => {
       this.accName = accounts[0].Name.toUpperCase();
       if (this.username === this.accName) {
           this.router.navigate(['/home']);
           this.failedAtt = false;
       } else {
           this.failedAtt = true;
       }
   })
 }


}
