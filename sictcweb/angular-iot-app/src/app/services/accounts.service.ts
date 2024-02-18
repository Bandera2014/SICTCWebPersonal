import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Account,NewAccount,UpdateAccount } from '../interfaces/accounts';

@Injectable({
  providedIn: 'root'
})

export class AccountsService {
 uri = 'http://localhost:3000';
 constructor(private http: HttpClient) {
}
 
  getAccountById(id: number) {
    console.log("getAccountById ran");
    return this.http.get<Account[]>(`${this.uri}/accounts/${id}`);
  }
  addAccount(data: NewAccount) {
    console.log("addAccount ran");
    return this.http.post<NewAccount>(`${this.uri}/accounts/add`, data);
  }
  getAccounts() {
    return this.http.get(`${this.uri}/accounts`);
  }

  deleteAccount(id: number) {
    return this.http.delete<Account>(`${this.uri}/accounts/delete/${id}`);
  }

  updateAccount(data: UpdateAccount) {
    return this.http.post<UpdateAccount>(`${this.uri}/accounts/update`, data);
  }


}

