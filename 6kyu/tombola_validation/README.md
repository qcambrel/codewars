# Tombola - Validation

[URL](https://www.codewars.com/kata/5898a751b2edc082f60005f4)

## SHORT INTRO

"Tombola" is an Italian raffle/bingo-like game, mostly played during Christmas holidays; you have a sheet with 15 numbers and win increasing prizes while you complete it. Wikipedia link.

## SHEET SAMPLES

![tombola](http://i46.servimg.com/u/f46/13/76/83/45/cartel11.jpg)

## THE KATA

In this kata you have to validate the correctness of a tombola sheet. More specifically:

- check if the sheet is made of 3 x 9 squares;
- check if there is a total of 15 unique numbers (> 0) over the squares (empty spaces will be represented with zeros);
- check if each of the 3 rows has 5 of the 15 numbers;
- check if each column has from 1 to 3 numbers in increasing order from top to bottom row;
- check if each column is divided in this way (inclusive, from first column to last): 1-9, 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-90 (<- careful here! 90 is included in the last range!).

## TESTS

To make the kata more challenging, I will not tell you why the input sheet is not valid.