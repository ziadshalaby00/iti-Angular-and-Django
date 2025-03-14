import { Component,Input } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {FormsModule} from '@angular/forms';
import {MatIconModule} from '@angular/material/icon';

@Component({  
  selector: 'app-tasks',
  imports: [MatCardModule, MatCheckboxModule, FormsModule, MatIconModule],
  templateUrl: './tasks.component.html',
  styleUrl: './tasks.component.css'
})
export class TasksComponent {
  saveOnLocal(tasks: any) {
    localStorage.setItem("tasks", JSON.stringify(tasks))
  }

  getFromLocal() {
    if (typeof window !== 'undefined' && localStorage.getItem("tasks")) {
      return JSON.parse(localStorage.getItem("tasks") || '');
    }
    return [];
  }

  tasks: any = this.getFromLocal(); 

  changeState(id: number) {
    const task: any = this.tasks.find((t: any) => t.id === id);
    if (task) {
      task.isDone = !task.isDone;
      this.saveOnLocal(this.tasks);
    }
  }

  @Input() dataFromParent!: string;

  ngOnChanges() {
    if(this.dataFromParent) {
      this.tasks.unshift({
        "id": Date.now(),
        "des": this.dataFromParent,
        "isDone": false
      })
      this.saveOnLocal(this.tasks);
    }
  }

  deleteTask(id: number) {
      const task: any = this.tasks.find((t: any) => t.id === id);
      let wdelete: boolean = confirm(`you sure you want to delete\n${task.des}`)
      if(wdelete) {
        this.tasks = this.tasks.filter((t: any) => t.id !== id);
        this.saveOnLocal(this.tasks);
      }
  }
}