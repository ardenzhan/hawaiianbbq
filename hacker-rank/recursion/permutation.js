// function p(n, y = n, tree = [], branch = []){
//     branch.push(n);
//     for (let i = y-1; i > 0; i--){
//         branch.push(i);
//     }
//     tree.push(branch);
//     console.log(y);
//     if (y-1 > 0) { tree = p(n, y-1, tree); }
//     return tree;
// }

// console.log(p(4));


class Node {
    constructor(value){
        this.value = value;
        this.branches = [];
        for (let i = this.value - 1; i > 0; i--){
            this.branches.push(i);
        }
        if (value-1 > 0) this.next = new Node(value - 1);
    }

    skipNode(n){
        if (n==0) return this.next;
        if (this.next != undefined) return this.next.skipNode(n-1);
    }
}

start = new Node(4);
// console.log(start.skipNode(1));

let i = 0;
while (start.skipNode(i) != undefined){
    let j = i;
    while (start.skipNode(j).branches != undefined){
        console.log(start.value, start.skipNode(i).value, start.skipNode(j).branches);
        j++;
        if (start.skipNode(j+1) == undefined) {
            break;
        }
    }
    i++;
}


