#[cfg(test)]
mod tests {
    use Advent_of_code::day2_complete;
    use Advent_of_code::day4_complete;
    use Advent_of_code::{day1, day3_complete};

    #[test]
    fn dy1() {
        day1::run();
    }

    #[test]
    fn dy2() {
        day2_complete::run();
    }

    #[test]
    fn dy3() {
        day3_complete::run();
    }
    #[test]
    fn dy4() {
        day4_complete::run();
    }
}
