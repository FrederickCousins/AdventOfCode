use std::collections::HashMap;
use std::fs;

fn main() {
    let input = fs::read_to_string("../inputs/day01.txt").expect("Failed to read input file");

    part1(&input);
    part2(&input);
}

fn part1(data: &str) {
    let (mut vec1, mut vec2): (Vec<i32>, Vec<i32>) = data
        .lines()
        .filter_map(|line| {
            let mut nums = line
                .split_whitespace()
                .filter_map(|num| num.parse::<i32>().ok());
            match (nums.next(), nums.next()) {
                (Some(a), Some(b)) => Some((a, b)),
                _ => None,
            }
        })
        .unzip();

    vec1.sort();
    vec2.sort();

    let res: i32 = vec1.iter().zip(vec2.iter())
        .map(|(a, b)| (a - b).abs())
        .sum();

    println!("Part 1: {res}");
}

fn part2(data: &str) {
    let (vec1, vec2): (Vec<i32>, Vec<i32>) = data
        .lines()
        .filter_map(|line| {
            let mut nums = line
                .split_whitespace()
                .filter_map(|num| num.parse::<i32>().ok());
            match (nums.next(), nums.next()) {
                (Some(a), Some(b)) => Some((a, b)),
                _ => None,
            }
        })
        .unzip();

    let freq_map = vec2.iter()
        .fold(HashMap::new(), |mut acc, &m| {
            *acc.entry(m).or_insert(0) += 1;
        acc
    });

    let res: i32 = vec1.iter()
        .filter_map(|n| freq_map.get(n).map(|&count| n * count))
        .sum();

    println!("Part 2: {res}");
}