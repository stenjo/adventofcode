// --- Day 9: All in a Single Night ---
// Every year, Santa manages to deliver all of his presents in a single night.

// This year, however, he has some new locations to visit; his elves have
// provided him the distances between every pair of locations. He can start
// and end at any two (different) locations he wants, but he must visit each
// location exactly once. What is the shortest distance he can travel to
// achieve this?

// For example, given the following distances:

// London to Dublin = 464
// London to Belfast = 518
// Dublin to Belfast = 141
// The possible routes are therefore:

// Dublin -> London -> Belfast = 982
// London -> Dublin -> Belfast = 605
// London -> Belfast -> Dublin = 659
// Dublin -> Belfast -> London = 659
// Belfast -> Dublin -> London = 605
// Belfast -> London -> Dublin = 982
// The shortest of these is London -> Dublin -> Belfast = 605, and so the
// answer is 605 in this example.

// What is the distance of the shortest route?

class Distance {
    from: string = "";
    to: string = "";
    distance: number = 0;

    constructor(line: string) {
        this.from = line.split(' ')[0];
        this.to = line.split(' ')[2];
        this.distance = parseInt(line.split(' ')[4]);
    }
}

export class Routes {
    
    distances: Distance[] = [];
    cities: string[] = [];

    GetShortestPathLength(): number {
        let totalDistance = 0;
        let city = this.DistinctCities()[0];
        let covered:string[] = [city];

        while (covered.length <= this.DistinctCities().length) {

            let nextCity = this.GetNearestCity(city, covered);
            covered.push(nextCity);
            totalDistance += this.GetDistanceTo(city, nextCity);
            city = nextCity;
        }

        return totalDistance;
    }
    GetNearestCity(city: string, covered: string[]):string {

        let nearest:string = "";
        for (let i = 0; i < this.distances.length; i++) {
            let distanceToCity = 1000000;
            let d = this.distances[i];
            if (
                covered.indexOf(d.from) == -1 
                && d.to == city 
                && d.distance < distanceToCity) {
                nearest = d.from;
                distanceToCity = d.distance;
            } 
            if (
                covered.indexOf(d.to) == -1 
                && d.from == city 
                && d.distance < distanceToCity) {
                nearest = d.to;
                distanceToCity = d.distance;
            }
        }
        return nearest;
    }

    GetDistanceTo(from: string, to: string): number {
        let distance = 0;
        this.distances.forEach(d => {
            if (d.from === from && d.to === to 
                || d.from === to && d.to === from) {
                distance = d.distance;
            }
        })
        return distance;
    }

    DistinctCities():string[] {

        return this.cities.filter(
            (city, i, arr) => arr.findIndex(t => t === city) === i
          );
    }

    constructor(distances: string[]) {
    
        distances.forEach((line) => {
            let d = new Distance(line);
            this.distances.push(d);
            this.cities.push(d.from);
            this.cities.push(d.to);
        })
    }
}