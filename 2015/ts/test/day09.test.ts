import { Routes } from '../src/day09'

const distances = ['London to Dublin = 464', 'London to Belfast = 518','Dublin to Belfast = 141']
const r = new Routes(distances);

describe('All in a Single Night', ()=>{

    it('Route London -> Dublin should be 464', ()=>{

        let routes = new Routes(['London to Dublin = 464']);
        
        expect(routes.GetShortestPathLength()).toBe(464);
    })

    it('GetDistance should return "London to Belfast = 518" ', () => {
        expect(r.GetDistanceTo("London", "Belfast")).toBe(518)
    })

    it('Route thriugh all should be 605', () => {
        expect(r.GetShortestPathLength()).toBe(605);
    })

})