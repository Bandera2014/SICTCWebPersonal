import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Account } from '../interfaces/accounts';

@Injectable({
  providedIn: 'root'
})

export class AccountsService {
  uri = 'http://your-raspberry-pi-ip:3000';
  constructor(private http: HttpClient) {
  }
  getAccounts() {
    return this.http.get<Account[]>(`${this.uri}/accounts`);
  }
  getAccountById(id: number) {
    return this.http.get<Account>(`${this.uri}/accounts/${id}`);
  }
  addAccount(data: Account) {
    return this.http.post<Account>(`${this.uri}/accounts/add`, data);
  }
  updateAccount(data: Account) {
    return this.http.post<Account>(`${this.uri}/accounts/update`, data);
  }
  deleteAccount(id: number) {
    return this.http.delete<Account>(`${this.uri}/accounts/delete/${id}`);
  }
}
