// --- Day 2: 

import fs from 'fs';
import path from 'path';

export class RPSGame {
    getStrategyScore(): any {
        let score = 0;
        this.lines.forEach(line => {
            score += this.Strategy(line.trim());
        })
        return score;
    }

    lines: string[];
    getScore(): any {
        let score = 0;
        this.lines.forEach(line => {
            score += this.Play(line.trim());
        })
        return score;
    }
    Play(gameRound: string): number {
        // A for Rock, B for Paper, and C for Scissors.
        // X for Rock, Y for Paper, and Z for Scissors
        // Score = choice + win/draw/loss
        let scoreMap:{round:string, score:number}[] = [
            {round:'A X', score: 3+1}, // draw(3) + rock(1)
            {round:'A Y', score: 8},   // win(6) + paper(2)
            {round:'A Z', score: 3},   // loss(0) + scissor(3)
            {round:'B X', score: 1},   // loss(0) + rock(1)
            {round:'B Y', score: 3+2}, // draw(3) + paper(2)
            {round:'B Z', score: 9},   // win(6) + scissor(3)
            {round:'C X', score: 7},   // win(6) + rock(1)
            {round:'C Y', score: 2},   // loss(0) + paper(2)
            {round:'C Z', score: 3+3}, // draw(3) + scissor(3)
        ];
        let score = 0;

        scoreMap.forEach(o => {
            if (o.round == gameRound) {
                score = o.score;
            }
        });

        return score;

    }
    Strategy(gameRound: string): number {
        // A for Rock, B for Paper, and C for Scissors.
        // X for Loose, Y for Draw, and Z for Win
        // Score = choice + win/draw/loss
        let scoreMap:{round:string, score:number}[] = [
            {round:'A X', score: 3},   // loss(0) + scisso(3)
            {round:'A Y', score: 4},   // draw(3) + rock(1)
            {round:'A Z', score: 8},   // win(6) + paper(2)
            {round:'B X', score: 1},   // loss(0) + rock(1)
            {round:'B Y', score: 3+2}, // draw(3) + paper(2)
            {round:'B Z', score: 6+3},   // win(6) + scissor(3)
            {round:'C X', score: 2},   // loss(0) + paper(2)
            {round:'C Y', score: 3+3},   // draw(3) + scissor(3)
            {round:'C Z', score: 6+1}, // win(6) + rock(1)
        ];
        let score = 0;

        scoreMap.forEach(o => {
            if (o.round == gameRound) {
                score = o.score;
            }
        });

        return score;

    }

    constructor(fname: string) {
        let filename = path.join(__dirname, fname);
        this.lines = fs.readFileSync(filename, 'utf8').trim().split('\n');
    }
}