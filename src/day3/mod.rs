use crate::day3::Direction::UP;
use std::cmp::{max, min};
use std::fs::File;
use std::io::Write;

pub fn run() {
    let line_one = vec![
        "R1005", "U563", "R417", "U509", "L237", "U555", "R397", "U414", "L490", "U336", "L697",
        "D682", "L180", "U951", "L189", "D547", "R697", "U583", "L172", "D859", "L370", "D114",
        "L519", "U829", "R389", "U608", "R66", "D634", "L320", "D49", "L931", "U137", "L349",
        "D689", "L351", "D829", "R819", "D138", "L118", "D849", "R230", "U858", "L509", "D311",
        "R815", "U217", "R359", "U840", "R77", "U230", "R361", "U322", "R300", "D646", "R348",
        "U815", "R793", "D752", "R967", "U128", "R948", "D499", "R359", "U572", "L566", "U815",
        "R630", "D290", "L829", "D736", "R358", "U778", "R891", "U941", "R544", "U889", "L920",
        "U913", "L447", "D604", "R538", "U818", "L215", "D437", "R447", "U576", "R452", "D794",
        "R864", "U269", "L325", "D35", "L268", "D639", "L101", "U777", "L776", "U958", "R105",
        "U517", "R667", "D423", "R603", "U469", "L125", "D919", "R879", "U994", "R665", "D377",
        "R456", "D570", "L685", "U291", "R261", "U846", "R840", "U418", "L974", "D270", "L312",
        "D426", "R621", "D334", "L855", "D378", "R694", "U845", "R481", "U895", "L362", "D840",
        "L712", "U57", "R276", "D643", "R566", "U348", "R361", "D144", "L287", "D864", "L556",
        "U610", "L927", "U322", "R271", "D90", "L741", "U446", "R181", "D527", "R56", "U805",
        "L907", "D406", "L286", "U873", "L79", "D280", "L153", "D377", "R253", "D61", "R475",
        "D804", "R788", "U393", "L660", "U314", "R489", "D491", "L234", "D712", "L253", "U651",
        "L777", "D726", "R146", "U47", "R630", "U517", "R226", "U624", "L834", "D153", "L513",
        "U799", "R287", "D868", "R982", "U390", "L296", "D373", "R9", "U994", "R105", "D673",
        "L657", "D868", "R738", "D277", "R374", "U828", "R860", "U247", "R484", "U986", "L723",
        "D847", "L578", "U487", "L51", "D865", "L328", "D199", "R812", "D726", "R355", "D463",
        "R761", "U69", "R508", "D753", "L81", "D50", "L345", "D66", "L764", "D466", "L975", "U619",
        "R59", "D788", "L737", "D360", "R14", "D253", "L512", "D417", "R828", "D188", "L394",
        "U212", "R658", "U369", "R920", "U927", "L339", "U552", "R856", "D458", "R407", "U41",
        "L930", "D460", "R809", "U467", "L410", "D800", "L135", "D596", "R678", "D4", "L771",
        "D637", "L876", "U192", "L406", "D136", "R666", "U730", "R711", "D291", "L586", "U845",
        "R606", "U2", "L228", "D759", "R244", "U946", "R948", "U160", "R397", "U134", "R188",
        "U850", "R623", "D315", "L219", "D450", "R489", "U374", "R299", "D474", "L767", "D679",
        "L160", "D403", "L708",
    ];
    let line_two = vec![
        "L1003", "D878", "R937", "D979", "R921", "U572", "R4", "D959", "L884", "U394", "R221",
        "U206", "R806", "U912", "R345", "D290", "R65", "D996", "L411", "D157", "R590", "D557",
        "L32", "D360", "L691", "D861", "L156", "D603", "R733", "U444", "L433", "U144", "L238",
        "U213", "R827", "U949", "R384", "D409", "L727", "U923", "L98", "U781", "L201", "D200",
        "R749", "U288", "L486", "U158", "L494", "D522", "R636", "D330", "L507", "U691", "R918",
        "D706", "R163", "U609", "R559", "U674", "R784", "D87", "R670", "U401", "L85", "U981",
        "R848", "D579", "L882", "U777", "R671", "D385", "R913", "D899", "R92", "D780", "L795",
        "U821", "R956", "U446", "L109", "D955", "L570", "D874", "R499", "U845", "R769", "U88",
        "L529", "U657", "R553", "D357", "L83", "D324", "L273", "U689", "L715", "U933", "R161",
        "U561", "L603", "U349", "L445", "U781", "R299", "U26", "L212", "U429", "R763", "U116",
        "R961", "D258", "L518", "D668", "L767", "U587", "L654", "D24", "R318", "U35", "L9", "D199",
        "L161", "U419", "R6", "D707", "R944", "U499", "R207", "D349", "L727", "D637", "R735",
        "D137", "R18", "D214", "L531", "D327", "L916", "U440", "R859", "U483", "R952", "D631",
        "L96", "D320", "L192", "D985", "R330", "D196", "L345", "D575", "L535", "D868", "R376",
        "D126", "R903", "D619", "L126", "D624", "L990", "D67", "L927", "U685", "L200", "D759",
        "L157", "D816", "L585", "U910", "R587", "D598", "L398", "U706", "R847", "U682", "L919",
        "D291", "L932", "D54", "L314", "U430", "L60", "U206", "L997", "D487", "L874", "U957",
        "L753", "U999", "R156", "U102", "L826", "U923", "L204", "U293", "L244", "U787", "L273",
        "D687", "R134", "D167", "L287", "D459", "R875", "D32", "R635", "D400", "L179", "D19",
        "L576", "U60", "L182", "D409", "R114", "U329", "R207", "U525", "L295", "U305", "L861",
        "U280", "R531", "D49", "L890", "U521", "L283", "U37", "R344", "D867", "L474", "U893",
        "R140", "U289", "L67", "U490", "R121", "D34", "L696", "U902", "R288", "U249", "R107",
        "D750", "R389", "U125", "L406", "U950", "R932", "U795", "R205", "U583", "L665", "U214",
        "R806", "D409", "R832", "D39", "R207", "D977", "L873", "U645", "L762", "U847", "L725",
        "U397", "R414", "D558", "L669", "D736", "R897", "U464", "R207", "U359", "R257", "U304",
        "L932", "U240", "L582", "U409", "L493", "D481", "R48", "D537", "R893", "U48", "R707",
        "U630", "L70", "D289", "L769", "U98", "L679", "U504", "L337", "U117", "L343", "D574",
        "R595", "U168", "R498",
    ];

    let test_line_one = vec!["R8", "U5", "L5", "D3"];
    let test_line_two = vec!["U7", "R6", "D4", "L4"];

    let test_x_line_one = vec!["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"];
    let test_x_line_two = vec!["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"];

    let test_x2_line_one = vec![
        "R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51",
    ];
    let test_x2_line_two = vec![
        "U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7",
    ];

    let length: u32 = compute(test_line_one, test_line_two);
    println!("{:?}", length);
    let length: u32 = compute(test_x_line_one, test_x_line_two);
    println!("{:?}", length);
    let length: u32 = compute(test_x2_line_one, test_x2_line_two);
    println!("{:?}", length);

    let length: u32 = compute(line_one, line_two);
    println!("{:?}", length);
}

#[derive(Debug)]
enum Direction {
    UP(u32),
    DOWN(u32),
    LEFT(u32),
    RIGHT(u32),
}

#[derive(Debug, Copy, Clone, PartialOrd, PartialEq)]
enum GridPoints {
    START,
    EMPTY,
    CROSS(u8),
    CROSSOTHER,
    INSTRORIGIN(u8),
    INSTR(u8),
}

fn compute(lone: Vec<&str>, ltwo: Vec<&str>) -> u32 {
    let instr_vec_one = get_instruction_vector(&lone);
    let instr_vec_two = get_instruction_vector(&ltwo);

    let max_dim = get_max_dim(&instr_vec_one, &instr_vec_two);
    println!("Max dim: {:?}", &max_dim);

    let mut grid = vec![
        vec![GridPoints::EMPTY; (max_dim.1 + max_dim.3 + 256) as usize];
        (max_dim.0 + max_dim.2 + 256) as usize
    ];

    let start_x = max_dim.3 + 128;
    let start_y = max_dim.2 + 128;

    println!("APPLY INSTR 0");
    apply_instr(&mut grid, instr_vec_one, start_x, start_y, 0);
    println!("APPLY INSTR 1");
    apply_instr(&mut grid, instr_vec_two, start_x, start_y, 1);

    //grid_print(&grid);

    println!("CALC MANNHEIM");
    calc_mannheim(&grid, start_x, start_y)
}

fn calc_mannheim(grid: &Vec<Vec<GridPoints>>, start_x: u32, start_y: u32) -> u32 {
    let mut min_dist: u32 = std::u32::MAX;

    for row in grid.iter().enumerate() {
        for col in row.1.iter().enumerate() {
            if col.1 == &GridPoints::CROSSOTHER {
                let r = row.0 as u32;
                let c = col.0 as u32;

                let dst_row = (r as i32 - start_x as i32).abs();
                let dst_col = (c as i32 - start_y as i32).abs();

                let dst = (dst_row + dst_col) as u32;

                if dst < min_dist {
                    min_dist = dst;
                }
            }
        }
    }

    min_dist
}

fn apply_instr(
    grid: &mut Vec<Vec<GridPoints>>,
    instr_vec: Vec<Direction>,
    start_x: u32,
    start_y: u32,
    id: u8,
) {
    let mut curr_x = start_x.clone();
    let mut curr_y = start_y.clone();
    let mut ic = 0u32;

    for instr in instr_vec {
        println!("{:?}", instr);
        //grid_print(&grid);
        if ic == 0 {
            grid[curr_x as usize][curr_y as usize] = GridPoints::START;
        } else {
            grid[curr_x as usize][curr_y as usize] = GridPoints::INSTRORIGIN(id);
        }

        match instr {
            UP(v) => {
                for i in 0..v {
                    curr_x += 1;

                    let current = grid[curr_x as usize][curr_y as usize];
                    match current {
                        GridPoints::CROSS(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::INSTRORIGIN(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::INSTR(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::EMPTY => {
                            grid[curr_x as usize][curr_y as usize] = GridPoints::INSTR(id);
                        }
                        _ => {}
                    }
                }
            }
            Direction::DOWN(v) => {
                for i in 0..v {
                    curr_x -= 1;

                    let current = grid[curr_x as usize][curr_y as usize];
                    match current {
                        GridPoints::CROSS(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::INSTRORIGIN(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::INSTR(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::EMPTY => {
                            grid[curr_x as usize][curr_y as usize] = GridPoints::INSTR(id);
                        }
                        _ => {}
                    }
                }
            }
            Direction::LEFT(v) => {
                for i in 0..v {
                    curr_y -= 1;

                    let current = grid[curr_x as usize][curr_y as usize];
                    match current {
                        GridPoints::CROSS(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::INSTRORIGIN(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::INSTR(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::EMPTY => {
                            grid[curr_x as usize][curr_y as usize] = GridPoints::INSTR(id);
                        }
                        _ => {}
                    }
                }
            }
            Direction::RIGHT(v) => {
                for i in 0..v {
                    curr_y += 1;

                    let current = grid[curr_x as usize][curr_y as usize];
                    match current {
                        GridPoints::CROSS(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::INSTRORIGIN(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::INSTR(cid) => {
                            if cid == id {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSS(id);
                            } else {
                                grid[curr_x as usize][curr_y as usize] = GridPoints::CROSSOTHER;
                            }
                        }
                        GridPoints::EMPTY => {
                            grid[curr_x as usize][curr_y as usize] = GridPoints::INSTR(id);
                        }
                        _ => {}
                    }
                }
            }
        }
        ic += 1;
    }
}

fn grid_print(grid: &Vec<Vec<GridPoints>>) {
    let mut x = grid.clone();
    //x.reverse();

    let mut f = File::create("grid.txt").unwrap();

    let mut b_buff: Vec<u8> = vec![];
    for row in x {
        for col in row {
            match col {
                GridPoints::START => {
                    //print!("O ");
                    b_buff.append(&mut "O".as_bytes().to_vec());
                }
                GridPoints::EMPTY => {
                    //print!(". ");
                    b_buff.append(&mut ".".as_bytes().to_vec());
                }
                GridPoints::CROSS(v) => {
                    //print!("X ");
                    b_buff.append(&mut "*".as_bytes().to_vec());
                }
                GridPoints::INSTRORIGIN(v) => {
                    //print!("+ ");
                    b_buff.append(&mut "+".as_bytes().to_vec());
                }
                GridPoints::INSTR(v) => {
                    //print!("* ");
                    //b_buff.append(&mut "* ".as_bytes().to_vec());
                    b_buff.append(&mut format!("{}", v).as_bytes().to_vec());
                }
                GridPoints::CROSSOTHER => {
                    b_buff.append(&mut "X".as_bytes().to_vec());
                }
            }
        }
        //println!();
        b_buff.append(&mut "\n".as_bytes().to_vec());
    }

    f.write_all(&b_buff);
}

//height, width, height neg, width neg
fn get_max_dim(lone: &Vec<Direction>, ltwo: &Vec<Direction>) -> (u32, u32, u32, u32) {
    let mut max_w = 0;
    let mut max_h = 0;

    let mut max_w_neg = 0;
    let mut max_h_neg = 0;

    let mut t_g_w = 0;
    let mut t_g_h = 0;

    let mut t_g_w_neg = 0;
    let mut t_g_h_neg = 0;

    for s in lone {
        match s {
            UP(v) => {
                t_g_h += v.clone();
                if t_g_h > max_h {
                    max_h = t_g_h;
                }
            }
            Direction::DOWN(v) => {
                t_g_h_neg += v.clone();
                if t_g_h_neg > max_h_neg {
                    max_h_neg = t_g_h_neg;
                }
            }
            Direction::LEFT(v) => {
                t_g_w_neg += v.clone();
                if t_g_w_neg > max_w_neg {
                    max_w_neg = t_g_w_neg;
                }
            }
            Direction::RIGHT(v) => {
                t_g_w += v.clone();
                if t_g_w > max_w {
                    max_w = t_g_w;
                }
            }
        }
    }

    t_g_w = 0;
    t_g_h = 0;
    t_g_w_neg = 0;
    t_g_h_neg = 0;
    for s in ltwo {
        match s {
            UP(v) => {
                t_g_h += v.clone();
                if t_g_h > max_h {
                    max_h = t_g_h;
                }
            }
            Direction::DOWN(v) => {
                t_g_h_neg += v.clone();
                if t_g_h_neg > max_h_neg {
                    max_h_neg = t_g_h_neg;
                }
            }
            Direction::LEFT(v) => {
                t_g_w_neg += v.clone();
                if t_g_w_neg > max_w_neg {
                    max_w_neg = t_g_w_neg;
                }
            }
            Direction::RIGHT(v) => {
                t_g_w += v.clone();
                if t_g_w > max_w {
                    max_w = t_g_w;
                }
            }
        }
    }

    return (max_h, max_w, max_h_neg, max_w_neg);
}

fn get_instruction_vector(v: &Vec<&str>) -> Vec<Direction> {
    let mut ret_vec = vec![];
    for s in v {
        ret_vec.push(instr_parse(s));
    }
    return ret_vec;
}

fn instr_parse(s: &str) -> Direction {
    let splits = s.split_at(1);

    return match splits.0 {
        "R" => Direction::RIGHT(splits.1.parse::<u32>().unwrap()),
        "U" => Direction::UP(splits.1.parse::<u32>().unwrap()),
        "D" => Direction::DOWN(splits.1.parse::<u32>().unwrap()),
        "L" => Direction::LEFT(splits.1.parse::<u32>().unwrap()),
        _ => panic!("Invalid direction"),
    };
}
