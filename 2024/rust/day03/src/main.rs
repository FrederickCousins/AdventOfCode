use std::fs;
use regex::Regex;

fn main() {
    let input = fs::read_to_string("../inputs/day03.txt").expect("Failed to read input file");

    part1(&input);
    part2(&input);
}

fn part1(data: &str) {
    println!("Part 1: {}", solve(data));
}

fn part2(data: &str) {
    let mut cropped = String::new();

    let mut switch = true;

    for (i, c) in data.chars().enumerate() {
        switch = if data[i..].starts_with("don't()") {
            false
        }
        else if data[i..].starts_with("do()") {
            true
        } else {
            switch
        };

        if switch {
            cropped.push(c);
        }
    }

    println!("Part 2: {}", solve(&cropped));
}

fn solve(input: &str) -> i32 {
    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    let mut res = 0;

    for (_, [f1, f2]) in re.captures_iter(&input).map(|caps| caps.extract()) {
        res += f1.parse::<i32>().unwrap() * f2.parse::<i32>().unwrap()
    }
    res
}