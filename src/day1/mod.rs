use std::fs::File;
use std::io::{Read, BufReader, BufRead};

pub fn run(){

    let mut file = File::open("src\\day1\\inp.txt").unwrap();
    let reader = BufReader::new(file);

    let mut fuel_req:f32 = 0f32;
    for line in reader.lines() {
        let mass :f32 = line.unwrap().parse::<f32>().unwrap();
        fuel_req += (mass / 3f32).floor() - 2f32;
    }

    println!("{:?}", fuel_req);
    println!("End: {:?}", fuel_calc_init(fuel_req));
    println!("End: {:?}", fuel_calc_init(100756f32));
    println!("End: {:?}", fuel_calc_init(1969f32));
    println!("End: {:?}", fuel_calc_init(14f32));
}

fn fuel_calc_init(inp: f32) -> f32 {
    let freq = (inp / 3f32).floor() - 2f32;

    return fuel_calc(freq) + freq;
}

fn fuel_calc(inp: f32) -> f32{
    let freq = (inp / 3f32).floor() - 2f32;
    if freq > 0f32 {
        return freq + fuel_calc(freq);
    }else{
        return 0f32
    }
}