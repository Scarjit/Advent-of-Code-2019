pub fn run() {



    for noun in 0..99 {
        for verb in 0..99 {
            let mut inp_real: Vec<u32> = vec![
                1, noun, verb, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 19, 10, 23, 2, 10, 23, 27,
                1, 27, 6, 31, 1, 13, 31, 35, 1, 13, 35, 39, 1, 39, 10, 43, 2, 43, 13, 47, 1, 47, 9, 51, 2,
                51, 13, 55, 1, 5, 55, 59, 2, 59, 9, 63, 1, 13, 63, 67, 2, 13, 67, 71, 1, 71, 5, 75, 2, 75,
                13, 79, 1, 79, 6, 83, 1, 83, 5, 87, 2, 87, 6, 91, 1, 5, 91, 95, 1, 95, 13, 99, 2, 99, 6,
                103, 1, 5, 103, 107, 1, 107, 9, 111, 2, 6, 111, 115, 1, 5, 115, 119, 1, 119, 2, 123, 1, 6,
                123, 0, 99, 2, 14, 0, 0,
            ];
            let out = calc(&mut inp_real);
            if out[0] == 19690720{
                println!("NOUN: {}", noun);
                println!("VERB: {}", verb);
                println!("Answer: {}", (100u32 * noun) + verb);
                break
            }
        }
    }

    //println!("{:?}", out);

    /*
    let mut inp_test_1: Vec<u32> = vec![1, 0, 0, 0, 99];
    let out_test_1: Vec<u32> = vec![2,0,0,0,99];

    let mut inp_test_2: Vec<u32> = vec![2, 3, 0, 3, 99];
    let out_test_2: Vec<u32> = vec![2,3,0,6,99];

    let mut inp_test_3: Vec<u32> = vec![2, 4, 4, 5, 99, 0];
    let out_test_3: Vec<u32> = vec![2,4,4,5,99,9801];

    let mut inp_test_4: Vec<u32> = vec![1, 1, 1, 4, 99, 5, 6, 0, 99];
    let out_test_4: Vec<u32> = vec![30,1,1,4,2,5,6,0,99];

    let out = calc(&mut inp_test_1);
    println!("{:?}\n{:?}", &out, out_test_1);


    let out = calc(&mut inp_test_2);
    println!("{:?}\n{:?}", &out, out_test_2);

    let out = calc(&mut inp_test_3);
    println!("{:?}\n{:?}", &out, out_test_3);

    let out = calc(&mut inp_test_4);
    println!("{:?}\n{:?}", &out, out_test_4);
    */
}

fn calc(inp: &mut Vec<u32>) -> Vec<u32>{
    let mut programm_counter: usize = 0;
    loop {
        let current_val: u32 = inp[programm_counter];
        //println!("{:?}: {:?}", programm_counter, current_val);
        match current_val {
            1 => {
                //println!("OPCODE 1");
                let pos_1 = inp[programm_counter+1];
                let pos_2 = inp[programm_counter+2];
                let store_pos = inp[programm_counter+3];
                let val_1 = inp[pos_1 as usize];
                let val_2 = inp[pos_2 as usize];
                let store_val = val_1+val_2;
                inp[store_pos as usize] = store_val;

                programm_counter += 3;
            }
            2 => {
                //println!("OPCODE 2");
                let pos_1 = inp[programm_counter+1];
                let pos_2 = inp[programm_counter+2];
                let store_pos = inp[programm_counter+3];
                let val_1 = inp[pos_1 as usize];
                let val_2 = inp[pos_2 as usize];
                let store_val = val_1*val_2;
                inp[store_pos as usize] = store_val;

                programm_counter += 3;
            }
            99 => {
                //println!("OPCODE 99");
                break
            }
            _ => {}
        }
        programm_counter += 1;
    }

    return inp.clone();
}