use std::fs;

fn main() {
    let input = fs::read_to_string("../inputs/day02.txt").expect("Failed to read input file");

    part1(&input);
    part2(&input);
}

fn part1(data: &str) {
    let mut res = 0;
    
    for line in data.lines() {
        let nums: Vec<i32> = line
            .split_whitespace()
            .filter_map(|n| n.parse::<i32>().ok())
            .collect();

        if nums.len() == 0 {
            continue
        }

        if check_run(&nums) {
            res += 1
        }
    }
    println!("Part 1: {res}")
}

fn part2(data: &str) {
    let mut res = 0;

    for line in data.lines() {
        let nums: Vec<i32> = line
            .split_whitespace()
            .filter_map(|n| n.parse::<i32>().ok())
            .collect();

        if nums.len() == 0 {
            continue
        }

        if check_run(&nums) {
            res += 1
        } else {
            for i in 0..nums.len() {
                if check_run(&[&nums[0..i], &nums[i+1..]].concat()) {
                    res += 1;
                    break
                }
            }
        }
    }
    println!("Part 2: {res}")
}

fn check_run(nums: &[i32]) -> bool {
    let diffs: Vec<i32> = nums
        .windows(2)
        .map(|n| n[1] - n[0])
        .collect();

    let first
    let same_sign = diffs
        .iter()
        .map(|d| d.signum())
        .all(|d| d == 1) || diffs
        .iter()
        .map(|d| d.signum())
        .all(|d| d == -1);

    if !same_sign {
        return false;
    }

    diffs.iter().all(|d| d.abs() <= 3)
}
