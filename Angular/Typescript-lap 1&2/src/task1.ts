// A callback function takes two parameters from the user: a function and an array.
// It returns a new array after applying the function to each item in the user-provided array.
let numbers: (number)[] = [10, 20, 30, 40, 50]
function opOnNum(func: Function, array: (any)[]): (any)[] {
    let newArray: (any)[] = [];
    for(let item of array){
        newArray.push(func(item));
    } 
    return newArray;
}
console.log(opOnNum((num: number): number => num * 2, numbers)); 

// A function takes two parameters from the user: the first is an array, and the second is a break type from an enum.
// The function returns the array as a string, separated by the specified break type.
enum breaks {
    space = " ",
    dot = ".",
    comma = ",",
    underscore = "_"
}
function join(array: (any)[], breaks: breaks): string {
    let result: string = ""
    array.forEach(el => {
        result += el + breaks;
    });
    return result;
}
let names: (string|number)[] = ["ziad", "ahmed", "shalaby", 10, 20, 30]
console.log(join(names, breaks.space));
// Ziad Ahmed Mahmoud Shalaby //