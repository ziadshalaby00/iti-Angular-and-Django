import { Component } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {FormsModule} from '@angular/forms';

@Component({  
  selector: 'app-tasks',
  imports: [MatCardModule, MatCheckboxModule, FormsModule],
  templateUrl: './tasks.component.html',
  styleUrl: './tasks.component.css'
})
export class TasksComponent {
  tasks: any = [
    {
      "id": 1, 
      "des": "one",
      "isDone": true 
    },
    {
      "id": 2,
      "des": "two", 
      "isDone": false
    },
    {
      "id": 3,
      "des": "three",
      "isDone": false
    },
    {
      "id": 4,
      "des": "four",
      "isDone": true
    },
  ] 

  changeState(id: number) {
    const task = this.tasks.find((t: any) => t.id === id);
    if (task) {
      task.isDone = !task.isDone;
    }
  }
}
