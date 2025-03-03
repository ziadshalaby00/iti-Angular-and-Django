"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
// => ===========================================================================================
class point2D {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    getLength(x, y) {
        return Math.sqrt(Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2));
    }
}
let test1 = new point2D(10, 20);
console.log(test1.getLength(20, 40));
class point3D extends point2D {
    constructor(x, y, z) {
        super(x, y);
        this.z = z;
    }
    getLength(x, y, z) {
        if (!z) {
            return super.getLength(x, y);
        }
        else {
            return Math.sqrt(Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2) + Math.pow(this.z - z, 2));
        }
    }
}
let test2 = new point3D(10, 20, 30);
console.log(test2.getLength(20, 40, 60));
// => ===========================================================================================
const testForModules_1 = require("./testForModules");
let posts = new testForModules_1.Posts();
function start() {
    return __awaiter(this, void 0, void 0, function* () {
        yield posts.getPosts();
        console.log(posts.showPosts());
    });
}
start();
//# sourceMappingURL=task2.js.map