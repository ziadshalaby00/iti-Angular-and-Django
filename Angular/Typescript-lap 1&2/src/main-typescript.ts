class User {
  u: string;
  s: Number;
  msg: () => string;

  constructor(username: string, salary: number) {
    this.u = username;
    this.s = salary;
    this.msg = () => `welocme ${this.u} your salary is ${this.s}`
  }
  sayMsg(): string {
    return `welocme ${this.u} your salary is ${this.s}`
  }
}

let user1 = new User("ziad", 25000)

console.log(user1.u)
console.log(user1.s)
console.log(user1.msg())
console.log(user1.sayMsg())