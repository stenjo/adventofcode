import fetch from 'node-fetch';

export class AoCData {

    url = ''
    data: string;

    constructor(day: number) { 
        this.url = 'https://adventofcode.com/2022/day/'+day+'/input'
        this.data = ''
    }

    async GetString() {
        this.data = await getData(this.url);
    }
}
export async function getData(url: string):Promise<any> {
    let body: string = ''
        const response = await fetch(url, {
            method: 'GET',
            headers: { 
                'Content-Type': 'application/text',
                'Cookie': 'session=53616c7465645f5f4cabcf0b5ce7cb0a65272e4986565c64590e60731a70c59c529dc19b9fc43c3dc5df4bfd09dfa4c198f0c6caebd2c316b87000d307df6088'
            },
        }).then((data) => {

            body = data.text() as unknown as string;      
        });
    return body;
}
let g = new AoCData(4);

// console.log(g.GetString())
let d = getData('https://adventofcode.com/2022/day/3/input')

console.log(d);