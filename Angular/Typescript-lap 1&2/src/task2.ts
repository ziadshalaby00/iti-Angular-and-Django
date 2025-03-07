// => ===========================================================================================
class point2D {
    protected x: number;
    protected y: number;
    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    }
    getLength(x: number, y:number) {
        return Math.sqrt(Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2))
    }
}
let test1 = new point2D(10, 20) as point2D
console.log(test1.getLength(20, 40))

class point3D extends point2D {
    private z: number;
    constructor(x: number, y: number, z: number) {
        super(x, y);
        this.z = z;
    }
    getLength(x:number, y:number, z?:number) {
        if(!z) {
            return super.getLength(x, y)
        }else {
            return Math.sqrt(Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2) + Math.pow(this.z - z, 2))
        }
    }
}
let test2 = new point3D(10, 20, 30) as point3D
console.log(test2.getLength(20, 40, 60))

// => ===========================================================================================
import { postsType, Posts, } from './testForModules'

let posts = new Posts<postsType>() as Posts<postsType>

async function start() {
    await posts.getPosts()
    console.log(posts.showPosts())
}
start()