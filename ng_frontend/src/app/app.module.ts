import { Input, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HttpClientModule } from '@angular/common/http';

import { TableModule } from 'primeng/table'
import { DataViewModule } from 'primeng/dataview'
import { ButtonModule } from 'primeng/button';
import { RippleModule } from 'primeng/ripple';
import { InputTextModule } from 'primeng/inputtext';
import { DialogModule } from 'primeng/dialog';
import { CheckboxModule } from 'primeng/checkbox';
import { FormsModule } from '@angular/forms'
import { InputNumberModule } from 'primeng/inputnumber';
import { FilterService } from 'primeng/api';
import { PaginatorModule } from 'primeng/paginator';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    TableModule,
    DataViewModule,
    ButtonModule,
    RippleModule,
    InputTextModule,
    DialogModule,
    CheckboxModule,
    FormsModule,
    InputNumberModule,
    PaginatorModule
  ],
  providers: [
    FilterService
  ],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
