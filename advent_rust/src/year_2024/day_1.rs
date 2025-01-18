use std::{fs::read_to_string, iter::zip};

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}

pub fn part_1() -> String {
    let lines = read_lines("./src/year_2024/day_1.in");

    let mut left = vec![];
    let mut right = vec![];
    for line in lines {
        let mut parts = line.split_whitespace();
        left.push(parts.next().unwrap().parse::<i32>().unwrap());
        right.push(parts.next().unwrap().parse::<i32>().unwrap());
    }

    left.sort();
    right.sort();

    let result: i32 = zip(left, right).map(|(l, r)| (l - r).abs()).sum();

    result.to_string()
}
