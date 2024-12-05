use std::collections::{HashMap, HashSet};

fn main() {
    let data = std::fs::read_to_string("../inputs/day05.txt").expect("Failed to read input file");
    let (keys, sequences) = data.split_once("\n\n").unwrap();

    let mut orderings = HashMap::<u32, HashSet<u32>>::new();
    for line in keys.lines() {
        let (x, y) = line.split_once('|').unwrap();
        orderings.entry(y.parse().unwrap())
            .or_default()
            .insert(x.parse().unwrap());
    }

    let sequences = sequences.lines().map(|line| {
        line.split(',').map(|num| num.parse::<u32>().unwrap()).collect::<Vec<_>>()
    });

    let (mut part1, mut part2) = (0, 0);
    for mut seq in sequences {
        if seq.is_sorted_by(|a, b| orderings[b].contains(a)) {
            part1 += seq[seq.len() / 2];
        } else {
            seq.sort_by(|a, b| orderings[b].contains(a).cmp(&true));
            part2 += seq[seq.len() / 2];
        }
    }

    println!("Part 1: {part1}");
    println!("Part 2: {part2}");
}