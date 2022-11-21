"use strict";
// --- Day 1: Not Quite Lisp ---
// Santa is trying to deliver presents in a large apartment building, but he
// can't find the right floor - the directions he got are a little confusing.
// He starts on the ground floor (floor 0) and then follows the instructions
// one character at a time.
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.part1 = exports.findFloor = void 0;
// An opening parenthesis, (, means he should go up one floor, and a closing
// parenthesis, ), means he should go down one floor.
// The apartment building is very tall, and the basement is very deep; he will
// never find the top or bottom floors.
// For example:
// (()) and ()() both result in floor 0.
// ((( and (()(()( both result in floor 3.
// ))((((( also results in floor 3.
// ()) and ))( both result in floor -1 (the first basement level).
// ))) and )())()) both result in floor -3.
// To what floor do the instructions take Santa?
function findFloor(directions) {
    let floor = 0;
    for (let i = 0; i < directions.length; i++) {
        if (directions[i] == '(') {
            floor += 1;
        }
        if (directions[i] == ')') {
            floor -= 1;
        }
    }
    return floor;
}
exports.findFloor = findFloor;
function part1() {
    return findFloor(getInput());
}
exports.part1 = part1;
const fs = __importStar(require("fs"));
const path = __importStar(require("path"));
function getInput() {
    let filename = path.dirname + '../../data01.txt';
    let input = fs.readFileSync(filename, 'utf8').trim();
    return input;
}
