import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {
  public formData: any
  constructor(private fp:FormBuilder) {
    this.formData = this.fp.group({
      "username": ['', Validators.required],
      "psw": ['', Validators.required],
      "pswrepeat": ['', Validators.required]
    })
  }
  submitData() {
    console.log(this.formData.value)
  }
  get username() {
    return this.formData.controls.username
  }
  get psw() {
    return this.formData.controls.psw
  }
  get pswrepeat() {
    return this.formData.controls.pswrepeat
  }
}
