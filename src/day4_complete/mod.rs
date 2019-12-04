use rayon::prelude::*;
use std::time::Instant;

const MINIMA: u32 = 136760;
const MAXMINA: u32 = 595730;

pub fn run() {
    let now = Instant::now();

    let v = calc_simple(MINIMA, MAXMINA);
    //let v = calc_combined(MINIMA, MAXMINA);
    //let v = calc_rayon_simple(MINIMA, MAXMINA);
    //let v = calc_rayon_new(MINIMA, MAXMINA);

    println!("Part one: {:?}", v.0);
    println!("Part two: {:?}", v.1);
    let elapsed_ns = now.elapsed().as_nanos();
    let iter_x = MAXMINA - MINIMA;
    let ns_per_iter = elapsed_ns / iter_x as u128;
    println!("Calculation took {} ns.", elapsed_ns);
    println!("{} ns per iter [{}]", ns_per_iter, iter_x);

    /*
        Part one: 1873
        Part two: 1264
    */

    //Part 1 sample
    /*
        println!("111111 is valid: {:?}", is_valid_number(111111));
        println!("223450 is valid: {:?}", is_valid_number(223450));
        println!("123789 is valid: {:?}", is_valid_number(123789));
    */

    //Part 2 sample
    /*
        println!("112233 is valid: {:?}", is_valid_number(112233));
        println!("123444 is valid: {:?}", is_valid_number(123444));
        println!("111122 is valid: {:?}", is_valid_number(111122));
    */
}

/*
    Calculation took 34217700 ns.
    74 ns per iter [458970]
*/
fn calc_simple(min: u32, max: u32) -> (u32, u32) {
    let mut valid_part_one: u32 = 0;
    let mut valid_part_two: u32 = 0;
    for i in min..max {
        if is_valid_number_part_one(i) {
            valid_part_one += 1;
        }
        if is_valid_number_part_two(i) {
            valid_part_two += 1;
        }
    }

    return (valid_part_one, valid_part_two);
}

/*
   Calculation took 25848700 ns.
   56 ns per iter [458970]
*/
fn calc_combined(min: u32, max: u32) -> (u32, u32) {
    let mut valid_part_one: u32 = 0;
    let mut valid_part_two: u32 = 0;
    for i in min..max {
        let cv = combined_validity(i);

        if cv.0 {
            valid_part_one += 1;
        }
        if cv.1 {
            valid_part_two += 1;
        }
    }
    return (valid_part_one, valid_part_two);
}

/*
    Calculation took 17604400 ns.
    38 ns per iter [458970]
*/
fn calc_rayon_simple(min: u32, max: u32) -> (u32, u32) {
    let x: Vec<(bool, bool)> = (MINIMA..MAXMINA)
        .into_par_iter()
        .map(|i| combined_validity(i))
        .collect();
    let mut valid_part_one: u32 = 0;
    let mut valid_part_two: u32 = 0;
    for i in x {
        if i.0 {
            valid_part_one += 1;
        }
        if i.1 {
            valid_part_two += 1;
        }
    }
    return (valid_part_one, valid_part_two);
}

/*
    Calculation took 5762200 ns.
    12 ns per iter [458970]
*/
fn calc_rayon_new(min: u32, max: u32) -> (u32, u32) {
    let mut valid_part_one: u32 = 0;
    let mut valid_part_two: u32 = 0;

    /*
        let sums = (min..max).into_par_iter().map(|i| combined_validity(i)).map(|f| {
            (f.0 as u32, f.1 as u32)
        }).reduce(|| (0, 0),
            |a: (u32, u32), b: (u32, u32)| (a.0 + b.0, a.1 + b.1)
        );
    */
    let sums = (min..max)
        .into_iter()
        .map(|i| combined_validity(i))
        .fold((0, 0), |a: (u32, u32), b| {
            (a.0 + b.0 as u32, a.1 + b.1 as u32)
        });

    return sums;
}

fn is_valid_number_part_two(inp: u32) -> bool {
    let num5 = inp % 10;
    let num4 = (inp / 10) % 10;

    if num5 < num4 {
        return false;
    }

    let num3 = (inp / 100) % 10;

    if num4 < num3 {
        return false;
    }

    let num2 = (inp / 1000) % 10;

    if num3 < num2 {
        return false;
    }

    let num1 = (inp / 10000) % 10;

    if num2 < num1 {
        return false;
    }

    let num0 = (inp / 100000) % 10;

    if num1 < num0 {
        return false;
    }

    if num0 == num1 && num1 != num2 {
        return true;
    }

    if num1 == num2 && num2 != num3 && num1 != num0 {
        return true;
    }

    if num2 == num3 && num3 != num4 && num2 != num1 {
        return true;
    }

    if num3 == num4 && num4 != num5 && num3 != num2 {
        return true;
    }

    if num4 == num5 && num4 != num3 {
        return true;
    }

    false
}

fn is_valid_number_part_one(inp: u32) -> bool {
    let num5 = inp % 10;
    let num4 = (inp / 10) % 10;

    if num5 < num4 {
        return false;
    }

    let num3 = (inp / 100) % 10;

    if num4 < num3 {
        return false;
    }

    let num2 = (inp / 1000) % 10;

    if num3 < num2 {
        return false;
    }

    let num1 = (inp / 10000) % 10;

    if num2 < num1 {
        return false;
    }

    let num0 = (inp / 100000) % 10;

    if num1 < num0 {
        return false;
    }

    if num0 == num1 || num1 == num2 || num2 == num3 || num3 == num4 || num4 == num5 {
        return true;
    }

    false
}

fn combined_validity(inp: u32) -> (bool, bool) {
    let num5 = inp % 10;
    let num4 = (inp / 10) % 10;

    if num5 < num4 {
        return (false, false);
    }

    let num3 = (inp / 100) % 10;

    if num4 < num3 {
        return (false, false);
    }

    let num2 = (inp / 1000) % 10;

    if num3 < num2 {
        return (false, false);
    }

    let num1 = (inp / 10000) % 10;

    if num2 < num1 {
        return (false, false);
    }

    let num0 = (inp / 100000) % 10;

    if num1 < num0 {
        return (false, false);
    }

    let mut x1 = false;

    if num0 == num1 {
        x1 = true;
        if num1 != num2 {
            return (x1, true);
        }
    }

    if num1 == num2 {
        x1 = true;
        if num2 != num3 && num1 != num0 {
            return (x1, true);
        }
    }

    if num2 == num3 {
        x1 = true;
        if num3 != num4 && num2 != num1 {
            return (x1, true);
        }
    }

    if num3 == num4 {
        x1 = true;
        if num4 != num5 && num3 != num2 {
            return (x1, true);
        }
    }

    if num4 == num5 {
        x1 = true;
        if num4 != num3 {
            return (x1, true);
        }
    }

    (x1, false)
}
