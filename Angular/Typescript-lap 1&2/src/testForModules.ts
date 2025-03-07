export type postsType = {
    userId: number,
    id: number,
    title: string,
    body: string
}

export class Posts<t> {
    private data: t[] = [];
    
    async getPosts() {
        let response = await fetch('https://jsonplaceholder.typicode.com/posts') as Response
        this.data = await response.json() as t[]
    }

    showPosts(): t[] {
        return this.data
    }
}