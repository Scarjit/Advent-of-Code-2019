use std::time::Instant;

const MINIMA: u32 = 136760;
const MAXMINA: u32 = 595730;

pub fn run(){
    let now = Instant::now();

    let mut valid_part_one: u32 = 0;
    let mut valid_part_two: u32 = 0;
    for i in MINIMA..MAXMINA {
        if is_valid_number_part_one(i) {
            valid_part_one += 1;
        }
        if is_valid_number_part_two(i) {
            valid_part_two += 1;
        }
    }

    println!("Part one: {:?}", valid_part_one);
    println!("Part two: {:?}", valid_part_two);
    println!("Calculation took {:?}", now.elapsed())

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

fn is_valid_number_part_two(inp: u32) -> bool{
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

    if num1 == num2 && num2 != num3 && num1 != num0{
        return true;
    }

    if num2 == num3 && num3 != num4 && num2 != num1{
        return true;
    }

    if num3 == num4 && num4 != num5 && num3 != num2{
        return true;
    }

    if num4 == num5 && num4 != num3{
        return true;
    }

    false
}


fn is_valid_number_part_one(inp: u32) -> bool{
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