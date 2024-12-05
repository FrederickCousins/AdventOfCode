use std::cmp::Ordering;
use std::collections::HashMap;
use std::fs;

fn main() {
    let data = fs::read_to_string("../inputs/day05.txt").expect("Failed to read input file");
    let (keys, sequences) = parse(&data);
    let comparisons = build_comparisons(&keys);

    part1(&comparisons, &sequences);
    part2(&comparisons, &sequences);
}

fn parse(data: &str) -> (Vec<(u32, u32)>, Vec<Vec<u32>>) {
    let parts: Vec<&str> = data.split("\n\n").collect();

    let keys: Vec<(u32, u32)> = parts[0]
        .lines()
        .filter_map(|line| {
            let nums: Vec<u32> = line.split("|").filter_map(|num| num.parse::<u32>().ok()).collect();
            if nums.len() == 2 { Some((nums[0], nums[1])) } else { None }
        })
        .collect();

    let sequences: Vec<Vec<u32>> = parts[1]
        .lines()
        .map(|line| line.split(",").filter_map(|num| num.parse::<u32>().ok()).collect())
        .collect();

    (keys, sequences)
}

fn build_comparisons(keys: &[(u32, u32)]) -> HashMap<(u32, u32), Ordering> {
    let mut comparisons = HashMap::new();
    for &(l, r) in keys {
        comparisons.insert((l, r), Ordering::Less);
        comparisons.insert((r, l), Ordering::Greater);
    }
    comparisons
}

fn sort_and_filter<F>(comparisons: &HashMap<(u32, u32), Ordering>, sequences: &[Vec<u32>], filter_fn: F) -> u32
where
    F: Fn(&Vec<u32>, &Vec<u32>) -> bool,
{
    let compare = |a: &u32, b: &u32| {
        comparisons.get(&(*a, *b)).copied().unwrap_or(Ordering::Equal)
    };

    sequences
        .iter()
        .filter_map(|seq| {
            let mut sorted = seq.clone();
            sorted.sort_by(compare);
            if filter_fn(seq, &sorted) {
                Some(sorted[sorted.len() / 2])
            } else {
                None
            }
        })
        .sum()
}

fn part1(comparisons: &HashMap<(u32, u32), Ordering>, sequences: &[Vec<u32>]) {
    let res = sort_and_filter(comparisons, sequences, |seq, sorted| seq == sorted);
    println!("Part 1: {res}");
}

fn part2(comparisons: &HashMap<(u32, u32), Ordering>, sequences: &[Vec<u32>]) {
    let res = sort_and_filter(comparisons, sequences, |seq, sorted| seq != sorted);
    println!("Part 2: {res}");
}