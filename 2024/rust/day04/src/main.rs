use std::fs;

fn main() {
    let input = fs::read_to_string("../inputs/day04.txt").expect("Failed to read input file");

    part1(&input);
    part2(&input);
}

fn part1(data: &str) {
    let grid: Vec<Vec<char>> = data.trim().lines().map(|line| line.chars().collect()).collect();
    let word = "XMAS";

    let rows = grid.iter().len();
    let cols = grid[0].iter().len();

    let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)];

    let check_word = |x: usize, y: usize, dx: isize, dy: isize| -> bool {
        word.chars().enumerate().all(|(i, ch)| {
            let nx = x as isize + i as isize * dx;
            let ny = y as isize + i as isize * dy;

            nx >= 0 && ny >= 0
                && nx < rows as isize && ny < cols as isize
                && grid[nx as usize][ny as usize] == ch
        })
    };

    let mut res = 0;

    for x in 0..rows {
        for y in 0..cols {
            for dir in dirs {
                if check_word(x, y, dir.0, dir.1) {
                    res += 1;
                }
            }
        }
    }

    println!("Part 1: {}", res);
}

fn part2(data: &str) {
    let grid: Vec<Vec<char>> = data.trim().lines().map(|line| line.chars().collect()).collect();

    let rows = grid.iter().len();
    let cols = grid[0].iter().len();

    let res = (1..rows - 1).flat_map(|i| (1..cols - 1).map(move |j| (i, j))).filter(|&(i, j)| {
        grid[i][j] == 'A' && (
            ( (grid[i-1][j-1] == 'M' && grid[i+1][j+1] == 'S') || (grid[i-1][j-1] == 'S' && grid[i+1][j+1] == 'M') ) &&
                ( (grid[i-1][j+1] == 'M' && grid[i+1][j-1] == 'S') || (grid[i-1][j+1] == 'S' && grid[i+1][j-1] == 'M') )
            )
    }).count();

    println!("Part 2: {}", res);
}
