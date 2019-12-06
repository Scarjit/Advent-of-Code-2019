import time
import copy

import math


class Day_1:
    def __init__(self, module_mass_str):
        self.module_masses_str = module_mass_str
        self.module_masses = self.module_masses_str.split("\n")
        self.total_fuel = 0
        self.recursive_total_fuel = 0

    def get_fuel_from_mass(self, mass):
        if mass < 0:
            raise Exception("Wrong universe mass may never be negative")
        fuel = int(mass / 3) - 2
        return fuel

    def get_raw_total_fuel(self):
        self.total_fuel = 0
        for m_str in self.module_masses:
            self.total_fuel += self.get_fuel_from_mass(int(m_str))
        return self.total_fuel

    def get_recursive_total_fuel(self):
        self.recursive_total_fuel = 0
        for m_str in self.module_masses:
            self.recursive_total_fuel += self.get_recursive_fuel_from_mass(int(m_str))
        return self.recursive_total_fuel

    def get_recursive_fuel_from_mass(self, module_mass):
        raw_fuel_module = self.get_fuel_from_mass(module_mass)

        def recursive_fuel(mass):
            raw_fuel = int(mass / 3) - 2
            if raw_fuel <= 0:
                return 0
            fuel = raw_fuel + recursive_fuel(raw_fuel)
            return fuel

        return raw_fuel_module + recursive_fuel(raw_fuel_module)


def solve_day_1():
    spaceship = Day_1("129561\n"
                      "125433\n"
                      "97919\n"
                      "93037\n"
                      "73254\n"
                      "96511\n"
                      "115676\n"
                      "95032\n"
                      "69369\n"
                      "145385\n"
                      "111145\n"
                      "64368\n"
                      "83462\n"
                      "95765\n"
                      "133284\n"
                      "136563\n"
                      "67439\n"
                      "69311\n"
                      "147720\n"
                      "92632\n"
                      "142940\n"
                      "100610\n"
                      "106538\n"
                      "80025\n"
                      "121672\n"
                      "125386\n"
                      "126601\n"
                      "67943\n"
                      "120022\n"
                      "95914\n"
                      "132721\n"
                      "105831\n"
                      "138493\n"
                      "57649\n"
                      "72843\n"
                      "81754\n"
                      "103116\n"
                      "148993\n"
                      "139042\n"
                      "145929\n"
                      "61039\n"
                      "126034\n"
                      "74187\n"
                      "60750\n"
                      "99048\n"
                      "131776\n"
                      "123137\n"
                      "113098\n"
                      "107571\n"
                      "117050\n"
                      "108649\n"
                      "117455\n"
                      "147443\n"
                      "121863\n"
                      "104952\n"
                      "103465\n"
                      "128718\n"
                      "61795\n"
                      "121049\n"
                      "112010\n"
                      "74403\n"
                      "56153\n"
                      "136161\n"
                      "76872\n"
                      "94156\n"
                      "131477\n"
                      "91769\n"
                      "90744\n"
                      "118647\n"
                      "135791\n"
                      "98914\n"
                      "104988\n"
                      "62070\n"
                      "82308\n"
                      "71964\n"
                      "91477\n"
                      "63733\n"
                      "84412\n"
                      "127000\n"
                      "65449\n"
                      "67976\n"
                      "51400\n"
                      "56045\n"
                      "82951\n"
                      "101119\n"
                      "143015\n"
                      "99388\n"
                      "51796\n"
                      "93467\n"
                      "63220\n"
                      "124459\n"
                      "136330\n"
                      "130535\n"
                      "144270\n"
                      "88616\n"
                      "63626\n"
                      "139954\n"
                      "92191\n"
                      "117618\n"
                      "110422")

    print("total Fuel = ", spaceship.get_raw_total_fuel())

    print("total Fuel with recursive fuel = ", spaceship.get_recursive_total_fuel())


class Day_2:
    def __init__(self, codes):
        self.codes = codes
        self.initial_codes = copy.deepcopy(codes)

    def reset_codes(self):
        self.codes = copy.deepcopy(self.initial_codes)

    def execute_codes(self):

        def execute_from_position(position):
            operation = self.codes[position]

            if operation == 1:
                self.codes[self.codes[position + 3]] = self.codes[self.codes[position + 1]] + self.codes[
                    self.codes[position + 2]]
                return True, 4
            elif operation == 2:
                self.codes[self.codes[position + 3]] = self.codes[self.codes[position + 1]] * self.codes[
                    self.codes[position + 2]]
                return True, 4
            elif operation == 99:
                return False, 1
            else:
                print("can not execute ", self.codes[position], "at", position)
                raise Exception("Operation can not be executed")

        start_position = 0
        current_position = start_position
        while True:
            continue_execution, increment = execute_from_position(current_position)
            current_position += increment
            if not continue_execution:
                break


def solve_day_2():
    computer = Day_2(
        [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19, 2, 6, 19, 23, 1, 23, 5, 27, 1, 27, 13, 31, 2, 6,
         31, 35, 1, 5, 35, 39, 1, 39, 10, 43, 2, 6, 43, 47, 1, 47, 5, 51, 1, 51, 9, 55, 2, 55, 6, 59, 1, 59, 10, 63, 2,
         63, 9, 67, 1, 67, 5, 71, 1, 71, 5, 75, 2, 75, 6, 79, 1, 5, 79, 83, 1, 10, 83, 87, 2, 13, 87, 91, 1, 10, 91, 95,
         2, 13, 95, 99, 1, 99, 9, 103, 1, 5, 103, 107, 1, 107, 10, 111, 1, 111, 5, 115, 1, 115, 6, 119, 1, 119, 10, 123,
         1, 123, 10, 127, 2, 127, 13, 131, 1, 13, 131, 135, 1, 135, 10, 139, 2, 139, 6, 143, 1, 143, 9, 147, 2, 147, 6,
         151, 1, 5, 151, 155, 1, 9, 155, 159, 2, 159, 6, 163, 1, 163, 2, 167, 1, 10, 167, 0, 99, 2, 14, 0, 0])
    result_found = False
    for noun in range(100):
        for verb in range(100):
            computer.reset_codes()
            computer.codes[1] = noun
            computer.codes[2] = verb
            try:
                computer.execute_codes()
                print("result = ", computer.codes[0], " for inputs ", noun, verb, "Answer = ", 100 * noun + verb)
                if computer.codes[0] == 19690720:
                    result_found = True
                    break
            except Exception as _e:
                if _e.args[0] == "Operation can not be executed":
                    pass
        if result_found:
            break


class Day_3:

    def __init__(self, route1, route2):
        self.route1 = route1.split(",")
        self.route2 = route2.split(",")
        self.grid = {}
        self.origin = (0, 0)
        self.intersections = []

    def add_route_to_grid(self, route, prime):
        def get_full_entry_direction(path_instruction):  # 0 achse = x achse. 1 achse = y achse
            return {"R": lambda v: (int(v), 0),
                    "L": lambda v: (-int(v), 0),
                    "U": lambda v: (0, int(v)),
                    "D": lambda v: (0, -int(v))}[path_instruction[0]](path_instruction[1:])

        current_position = list(copy.deepcopy(self.origin))
        current_step = 0

        def add_position_to_grid(position, identifier, c_step):
            line_step = copy.deepcopy(c_step)
            grid_step = copy.deepcopy(c_step)
            if position not in self.grid:
                self.grid[position] = identifier, grid_step
            else:  # line is in grid
                if self.grid[position][0] % identifier == 0:  # get's triggered when selfe intersection occurs
                    line_step = self.grid[position][1]
                    grid_step = self.grid[position][1]
                else:  # get's triggered when 2 different lines meet for the first time on any tile
                    grid_step = self.grid[position][1] + line_step
                self.grid[position] = self.grid[position][
                                          0] * identifier, grid_step  # TODO maybe Broken  for step length of self intersection
            return line_step

        for segment in route:
            s = list(get_full_entry_direction(segment))
            while s[0] != 0 or s[1] != 0:
                current_step += 1
                if s[0] != 0:
                    current_position[0] += int(s[0] / abs(s[0]))
                    current_step = add_position_to_grid(tuple(current_position), prime, current_step)
                    s[0] -= int(s[0] / abs(s[0]))
                elif s[1] != 0:
                    current_position[1] += int(s[1] / abs(s[1]))
                    current_step = add_position_to_grid(tuple(current_position), prime, current_step)
                    s[1] -= int(s[1] / abs(s[1]))
                else:
                    print(s)

    def check_for_intersections(self, identifiers):
        intersections = []
        for pair in self.grid.items():
            check = True
            for prime in identifiers:
                check = pair[1][0] % prime == 0 and check
            if check:
                intersections.append(pair)
        intersections.sort(key=lambda inter: abs(inter[0][0]) + abs(inter[0][1]))
        self.intersections = intersections

    def get_closest_intersection(self):
        min_distance = 10 ** 10
        closest_intersection = ((0, 0), 0)
        for inter in self.intersections:
            manhattan_distance = abs(inter[0][0]) + abs(inter[0][1])
            if manhattan_distance < min_distance:
                min_distance = manhattan_distance
                closest_intersection = inter
        return min_distance, closest_intersection

    def get_shortest_intersection(self):
        min_distance = 10 ** 10
        shortest_intersection = ((0, 0), (0, 0))
        for inter in self.intersections:
            if inter[1][1] < min_distance:
                min_distance = inter[1][1]
                shortest_intersection = inter
        return min_distance, shortest_intersection


def solve_day_3():
    grid = Day_3("R993,U847,R868,D286,L665,D860,R823,U934,L341,U49,R762,D480,R899,D23,L273,D892,R43,U740,L940,U502,"
                 "L361,U283,L852,D630,R384,D758,R655,D358,L751,U970,R72,D245,L188,D34,R355,U373,L786,U188,L304,D621,"
                 "L956,D839,R607,U279,L459,U340,R412,D901,L929,U256,R495,D462,R369,D138,R926,D551,L343,U237,L434,"
                 "U952,R421,U263,L663,D694,R687,D522,L47,U8,L399,D930,R928,U73,L581,U452,R80,U610,L998,D797,R584,"
                 "U772,L521,U292,L959,U356,L940,D894,R774,U957,L813,D650,L891,U309,L254,D271,R791,D484,L399,U106,"
                 "R463,D39,L210,D154,L380,U86,L136,D228,L284,D267,R195,D727,R739,D393,R395,U703,L385,U483,R433,U222,"
                 "L945,D104,L605,D814,L656,U860,L474,D672,L812,U789,L29,D256,R857,U436,R927,U99,R171,D727,L244,D910,"
                 "L347,U789,R49,U598,L218,D834,L574,U647,L185,U986,L273,D363,R848,U531,R837,U433,L795,U923,L182,D915,"
                 "R367,D347,R867,U789,L776,U568,R969,U923,L765,D589,R772,U715,R38,D968,L845,D327,R721,D928,R267,U94,"
                 "R763,U799,L946,U130,L649,U521,L569,D139,R584,D27,L823,D918,L450,D390,R149,U237,L696,U258,L757,U810,"
                 "L216,U202,L966,U157,R702,D623,R740,D560,R932,D587,L197,D56,R695,U439,R655,U576,R695,D176,L800,D374,"
                 "R806,U969,L664,U216,L170,D415,R485,U188,L444,D613,R728,U508,L644,U289,R831,D978,R711,U973,R3,U551,"
                 "R377,U114,L15,U812,R210,D829,L536,D883,L843,D427,L311,D680,R482,D69,R125,D953,L896,D85,R376,D683,"
                 "R374,U415,L3,U843,L802,D124,R299,U345,L696,D276,L87,D98,R619,D321,R348,D806,L789,U657,R590,D747,"
                 "L477,U251,R854,D351,L82,D982,R906,D94,R285,U756,L737,D377,L951,U126,L852,D751,L946,U696,L44,D709,"
                 "R851,D364,R222", "L1002,D658,L695,U170,L117,U93,R700,D960,L631,U483,L640,D699,R865,U886,L59,D795,"
                                   "R265,U803,R705,D580,R519,U685,R126,D888,R498,U934,L980,U734,L91,D50,R805,U197,"
                                   "R730,U363,R337,U594,L666,U702,L237,D140,L72,U980,L167,U598,L726,U497,L340,D477,"
                                   "L304,U945,R956,U113,L43,D4,R890,D316,R916,D644,R704,D398,L905,U361,R420,U31,L317,"
                                   "U338,R703,D211,R27,D477,L746,U813,R705,U191,L504,D434,R697,D945,R835,D374,L512,"
                                   "U269,L299,U448,R715,U363,R266,U720,L611,U672,L509,D983,L21,U895,L340,D794,R528,"
                                   "U603,R154,D610,L582,U420,L696,U599,R16,U610,L134,D533,R156,D338,L761,U49,L335,"
                                   "D238,R146,U97,L997,U545,L896,D855,L653,D789,R516,D371,L99,D731,R868,D182,R535,"
                                   "D35,R190,D618,R10,D694,L567,D17,R356,U820,R671,D883,R807,U218,L738,U225,L145,"
                                   "D954,R588,U505,R108,U178,R993,D788,R302,D951,R697,D576,L324,U930,R248,D245,R622,"
                                   "U323,R667,U876,L987,D411,L989,U915,R157,D67,L968,U61,R274,D189,L53,D133,R617,"
                                   "D958,L379,U563,L448,D412,R940,U12,R885,U121,R746,U215,R420,U346,L469,D839,R964,"
                                   "D273,R265,D3,L714,D224,L177,U194,L573,U511,L795,U299,L311,U923,R815,U594,L654,"
                                   "U326,L547,U547,R467,D937,L174,U453,R635,D551,L365,U355,R658,U996,R458,D623,R61,"
                                   "U181,R340,U163,L329,D496,L787,D335,L37,D565,R318,U942,R198,U85,R328,D826,R817,"
                                   "D118,R138,D29,L434,D427,R222,D866,L10,D152,R822,D779,L900,D307,R723,D363,L715,"
                                   "D60,R661,U680,R782,U789,R311,D36,R425,U498,L910,D546,R394,D52,R803,D168,L6,U769,"
                                   "R856,D999,L786,U695,R568,U236,R472,U291,L530,U314,L251,D598,R648,D475,L132,D236,"
                                   "L915,D695,L700,U378,L685,D240,R924,D977,R627,U824,L165")

    grid1 = Day_3("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
    grid2 = Day_3("U62,R66,U55,R34,D71,R55,D58,R83", "R75,D30,R83,U83,L12,D49,R71,U7,L72")
    grid3 = Day_3(
        "L1002,D658,L695,U170,L117,U93,R700,D960,L631,U483,L640,D699,R865,U886,L59,D795,R265,U803,R705,D580,R519,U685,R126,D888,R498,U934,L980,U734,L91,D50,R805,U197,R730,U363,R337,U594,L666,U702,L237,D140,L72,U980,L167,U598,L726,U497,L340,D477,L304,U945,R956,U113,L43,D4,R890,D316,R916,D644,R704,D398,L905,U361,R420,U31,L317,U338,R703,D211,R27,D477,L746,U813,R705,U191,L504,D434,R697,D945,R835,D374,L512,U269,L299,U448,R715,U363,R266,U720,L611,U672,L509,D983,L21,U895,L340,D794,R528,U603,R154,D610,L582,U420,L696,U599,R16,U610,L134,D533,R156,D338,L761,U49,L335,D238,R146,U97,L997,U545,L896,D855,L653,D789,R516,D371,L99,D731,R868,D182,R535,D35,R190,D618,R10,D694,L567,D17,R356,U820,R671,D883,R807,U218,L738,U225,L145,D954,R588,U505,R108,U178,R993,D788,R302,D951,R697,D576,L324,U930,R248,D245,R622,U323,R667,U876,L987,D411,L989,U915,R157,D67,L968,U61,R274,D189,L53,D133,R617,D958,L379,U563,L448,D412,R940,U12,R885,U121,R746,U215,R420,U346,L469,D839,R964,D273,R265,D3,L714,D224,L177,U194,L573,U511,L795,U299,L311,U923,R815,U594,L654,U326,L547,U547,R467,D937,L174,U453,R635,D551,L365,U355,R658,U996,R458,D623,R61,U181,R340,U163,L329,D496,L787,D335,L37,D565,R318,U942,R198,U85,R328,D826,R817,D118,R138,D29,L434,D427,R222,D866,L10,D152,R822,D779,L900,D307,R723,D363,L715,D60,R661,U680,R782,U789,R311,D36,R425,U498,L910,D546,R394,D52,R803,D168,L6,U769,R856,D999,L786,U695,R568,U236,R472,U291,L530,U314,L251,D598,R648,D475,L132,D236,L915,D695,L700,U378,L685,D240,R924,D977,R627,U824,L165",
        "R993,U847,R868,D286,L665,D860,R823,U934,L341,U49,R762,D480,R899,D23,L273,D892,R43,U740,L940,U502,L361,U283,L852,D630,R384,D758,R655,D358,L751,U970,R72,D245,L188,D34,R355,U373,L786,U188,L304,D621,L956,D839,R607,U279,L459,U340,R412,D901,L929,U256,R495,D462,R369,D138,R926,D551,L343,U237,L434,U952,R421,U263,L663,D694,R687,D522,L47,U8,L399,D930,R928,U73,L581,U452,R80,U610,L998,D797,R584,U772,L521,U292,L959,U356,L940,D894,R774,U957,L813,D650,L891,U309,L254,D271,R791,D484,L399,U106,R463,D39,L210,D154,L380,U86,L136,D228,L284,D267,R195,D727,R739,D393,R395,U703,L385,U483,R433,U222,L945,D104,L605,D814,L656,U860,L474,D672,L812,U789,L29,D256,R857,U436,R927,U99,R171,D727,L244,D910,L347,U789,R49,U598,L218,D834,L574,U647,L185,U986,L273,D363,R848,U531,R837,U433,L795,U923,L182,D915,R367,D347,R867,U789,L776,U568,R969,U923,L765,D589,R772,U715,R38,D968,L845,D327,R721,D928,R267,U94,R763,U799,L946,U130,L649,U521,L569,D139,R584,D27,L823,D918,L450,D390,R149,U237,L696,U258,L757,U810,L216,U202,L966,U157,R702,D623,R740,D560,R932,D587,L197,D56,R695,U439,R655,U576,R695,D176,L800,D374,R806,U969,L664,U216,L170,D415,R485,U188,L444,D613,R728,U508,L644,U289,R831,D978,R711,U973,R3,U551,R377,U114,L15,U812,R210,D829,L536,D883,L843,D427,L311,D680,R482,D69,R125,D953,L896,D85,R376,D683,R374,U415,L3,U843,L802,D124,R299,U345,L696,D276,L87,D98,R619,D321,R348,D806,L789,U657,R590,D747,L477,U251,R854,D351,L82,D982,R906,D94,R285,U756,L737,D377,L951,U126,L852,D751,L946,U696,L44,D709,R851,D364,R222")
    grid.add_route_to_grid(grid.route1, 3)
    grid.add_route_to_grid(grid.route2, 2)
    grid.check_for_intersections((2, 3))

    grid1.add_route_to_grid(grid1.route1, 3)
    grid1.add_route_to_grid(grid1.route2, 2)
    grid1.check_for_intersections((2, 3))

    grid2.add_route_to_grid(grid2.route1, 3)
    grid2.add_route_to_grid(grid2.route2, 2)
    grid2.check_for_intersections((2, 3))

    grid3.add_route_to_grid(grid3.route1, 3)
    grid3.add_route_to_grid(grid3.route2, 2)
    grid3.check_for_intersections((2, 3))

    print("grid")
    print(grid.get_closest_intersection())
    print(grid.get_shortest_intersection())

    print("testgrid 1 Target 135,410")
    print(grid1.get_closest_intersection())
    print(grid1.get_shortest_intersection())

    print("testgrid 2Target 159,610")
    print(grid2.get_closest_intersection())
    print(grid2.get_shortest_intersection())

    print("testgrid : Target eqaul to grid")
    print(grid3.get_closest_intersection())
    print(grid3.get_shortest_intersection())


class Day_4:
    def __init__(self, lower, upper):
        if lower > upper:
            _x = upper
            upper = lower
            lower = _x
        self.lower_boundary = lower
        self.upper_boundary = upper
        self.possibilities = range(lower, upper + 1)
        self.valid_options = set()
        self.valid_options_found = 0
        self.digits = self.digit_detector()

    def digit_detector(self):
        current_digits = 1
        while True:
            if 0 == math.floor(self.upper_boundary / (10 ** current_digits)):
                break
            current_digits += 1
        return current_digits

    def filter_options(self):
        for option in self.possibilities:
            if self.check_option(option):
                self.valid_options.add(option)
                self.valid_options_found += 1

    def filter_options_no_set(self):
        for option in self.possibilities:
            if self.check_option(option):
                self.valid_options_found += 1

    def filter_options_no_set_stage_2(self):
        for option in self.possibilities:
            if self.check_option_stage_2(option):
                self.valid_options_found += 1

    def filter_options_stage_2(self):
        for option in self.possibilities:
            if self.check_option_stage_2(option):
                self.valid_options.add(option)
                self.valid_options_found += 1

    def check_option_stage_2(self, option):
        def get_digits(number):
            """

            :param number:
            :return: list(int) list with digits, dominant digit in first position
            """
            digits = []
            for _i in range(self.digits):
                power = self.digits - _i - 1
                digit = (math.trunc(number / (10 ** power)))
                number = number - digit * 10 ** power
                digits.append(digit)
            return digits

        def raise_check(_digits):
            """

            :param _digits:
            :return:bool true if no declining digits
            """
            for _i in range(1, len(_digits)):
                if _digits[_i] < _digits[_i - 1]:
                    return False
            return True

        def dubs_check(_digits):
            """

            :param _digits:
            :return:bool True if dubs in number
            """
            dubs = False
            earlydubs = False
            current_row = 1
            for _i in range(len(_digits) - 1):
                if _digits[_i] == _digits[_i + 1]:
                    current_row += 1
                    dubs = True
                    if current_row > 2:
                        dubs = False
                else:
                    if dubs:
                        earlydubs = True
                    current_row = 1
            return dubs or earlydubs

        digits = get_digits(option)
        if raise_check(digits):
            if dubs_check(digits):
                return True
        return False

    def check_option(self, option):
        def get_digits(number):
            """

            :param number:
            :return: list(int) list with digits, dominant digit in first position
            """
            digits = []
            for _i in range(self.digits):
                power = self.digits - _i - 1
                digit = (math.trunc(number / (10 ** power)))
                number = number - digit * 10 ** power
                if digit != 0:
                    digits.append(digit)
            return digits

        def raise_check(_digits):
            """

            :param _digits:
            :return:bool true if no declining digits
            """
            for _i in range(1, len(_digits)):
                if _digits[_i] < _digits[_i - 1]:
                    return False
            return True

        def dubs_check(_digits):
            """

            :param _digits:
            :return:bool True if dubs in number
            """
            for _i in range(len(_digits) - 1):
                if _digits[_i] == _digits[_i + 1]:
                    return True
            return False

        digits = get_digits(option)
        if raise_check(digits):
            if dubs_check(digits):
                return True
        return False


def solve_day_4():
    start = time.time()
    l = 1
    u = 10000000
    test1 = Day_4(l, u)
    test2 = Day_4(l, u)

    print("calculating stage 1")
    start_filter_1 = time.time()
    test1.filter_options_no_set()
    end_filter_1 = time.time()
    print("completed filter in ", end_filter_1 - start_filter_1, " s")
    print("calculating stage 2")
    start_filter_2 = time.time()
    test2.filter_options_no_set_stage_2()
    end_filter_2 = time.time()
    print("completed filter in ", end_filter_2 - start_filter_2, " s")
    print("Test stage 1 options : ", test1.valid_options_found)
    print("Test stage 2 options : ", test2.valid_options_found)


class Day_5(Day_2):

    def execute_codes(self):
        def execute_from_position(position):
            def get_operation(full_operation_code):
                _operation = full_operation_code % 100
                _op_code = int(full_operation_code / 100)
                return _op_code, _operation

            def addition(input_1, input_2, output_index):
                self.codes[output_index] = input_1 + input_2
                return True, 4

            def multiplication(input_1, input_2, output_index):
                # print("output index", output_index)
                self.codes[output_index] = input_1 * input_2
                return True, 4

            def my_in(index_for_input):
                self.codes[index_for_input] = int(input("enter input\n"))
                return True, 2

            def my_out(output):
                print("output = ", output)
                return True, 2

            def jump_if_true(boolean, target):
                if boolean != 0:
                    return False, target
                else:
                    return True, 3

            def jump_if_false(boolean, target):
                if boolean == 0:
                    return False, target
                else:
                    return True, 3

            def less_than(first_input, second_input, output_index):
                if first_input < second_input:
                    self.codes[output_index] = 1
                else:
                    self.codes[output_index] = 0
                return True, 4

            def equal(first_input, second_input, output_index):
                if first_input == second_input:
                    self.codes[output_index] = 1
                else:
                    self.codes[output_index] = 0
                return True, 4

            def halt():
                return False, -1

            op_code, operation = get_operation(self.codes[position])
            # print(op_code, operation)
            input_params = {1: 2,
                            2: 2,
                            3: 0,
                            4: 1,
                            5: 2,
                            6: 2,
                            7: 2,
                            8: 2,
                            99: 0}
            output_params = {1: 1,
                             2: 1,
                             3: 1,
                             4: 0,
                             5: 0,
                             6: 0,
                             7: 1,
                             8: 1,
                             99: 0}
            n_params = input_params[operation] + output_params[operation]
            modes = [0] * input_params[operation]
            for _i in range(input_params[operation]):
                digit = int(op_code / (10 ** _i)) % 10
                if not (digit == 1 or digit == 0):
                    raise Exception("invalid opcode")
                modes[_i] = digit
            params = [0] * n_params
            for _i in range(input_params[operation]):  # input parameters
                # print("input param ", _i, "of", input_params[operation])
                if modes[_i] == 0:  # adds value of register to params
                    # print(self.codes[position+1 + _i], self.codes[position + _i])
                    params[_i] = self.codes[self.codes[position + _i + 1]]
                elif modes[_i] == 1:
                    params[_i] = self.codes[position + _i + 1]
                else:
                    raise Exception("invalid opcode", op_code, operation, "at", position)
            for _i in range(output_params[operation]):
                params[input_params[operation] + _i] = self.codes[position + input_params[operation] + _i + 1]
            # print("modes = ",modes," operation = ", operation," parameters = ", params)
            return {1: addition,
                    2: multiplication,
                    3: my_in,
                    4: my_out,
                    5: jump_if_true,
                    6: jump_if_false,
                    7: less_than,
                    8: equal,
                    99: halt}[operation](*params)

        start_position = 0
        current_position = start_position

        while True:
            # print(self.codes)
            continue_execution, increment = execute_from_position(current_position)
            current_position += increment
            # print(continue_execution, increment,current_position)
            # print(current_position)
            # print(self.codes)
            if not continue_execution:
                if increment == -1:
                    break
                else:
                    current_position = increment


def solve_day_5():
    test_programm = Day_5([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                           1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                           999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99])
    test_programm = Day_5(
        [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1002, 43, 69, 224, 101, -483, 224, 224, 4, 224, 1002, 223, 8,
         223, 1001, 224, 5, 224, 1, 224, 223, 223, 1101, 67, 60, 225, 1102, 5, 59, 225, 1101, 7, 16, 225, 1102, 49, 72,
         225, 101, 93, 39, 224, 101, -98, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 6, 224, 1, 224, 223, 223, 1102,
         35, 82, 225, 2, 166, 36, 224, 101, -4260, 224, 224, 4, 224, 102, 8, 223, 223, 101, 5, 224, 224, 1, 223, 224,
         223, 102, 66, 48, 224, 1001, 224, -4752, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 2, 224, 1, 223, 224, 223,
         1001, 73, 20, 224, 1001, 224, -55, 224, 4, 224, 102, 8, 223, 223, 101, 7, 224, 224, 1, 223, 224, 223, 1102, 18,
         41, 224, 1001, 224, -738, 224, 4, 224, 102, 8, 223, 223, 101, 6, 224, 224, 1, 224, 223, 223, 1101, 68, 71, 225,
         1102, 5, 66, 225, 1101, 27, 5, 225, 1101, 54, 63, 224, 1001, 224, -117, 224, 4, 224, 102, 8, 223, 223, 1001,
         224, 2, 224, 1, 223, 224, 223, 1, 170, 174, 224, 101, -71, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 4,
         224, 1, 223, 224, 223, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227,
         247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1,
         99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101,
         294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0,
         0, 1105, 1, 99999, 1007, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 329, 1001, 223, 1, 223, 1007, 226, 677,
         224, 102, 2, 223, 223, 1006, 224, 344, 1001, 223, 1, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 359,
         1001, 223, 1, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 374, 101, 1, 223, 223, 8, 677, 226, 224,
         1002, 223, 2, 223, 1006, 224, 389, 101, 1, 223, 223, 7, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 404, 101,
         1, 223, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 419, 1001, 223, 1, 223, 8, 226, 677, 224, 1002,
         223, 2, 223, 1005, 224, 434, 101, 1, 223, 223, 1008, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 449, 1001,
         223, 1, 223, 7, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 464, 1001, 223, 1, 223, 108, 677, 226, 224, 102,
         2, 223, 223, 1005, 224, 479, 101, 1, 223, 223, 108, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 494, 101, 1,
         223, 223, 8, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 509, 1001, 223, 1, 223, 1107, 677, 226, 224, 102, 2,
         223, 223, 1005, 224, 524, 1001, 223, 1, 223, 1107, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 539, 1001, 223,
         1, 223, 1108, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 554, 101, 1, 223, 223, 107, 226, 677, 224, 102, 2,
         223, 223, 1005, 224, 569, 1001, 223, 1, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 584, 1001, 223,
         1, 223, 1107, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 599, 1001, 223, 1, 223, 1008, 226, 226, 224, 1002,
         223, 2, 223, 1005, 224, 614, 101, 1, 223, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 629, 1001, 223,
         1, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 644, 101, 1, 223, 223, 107, 677, 677, 224, 1002,
         223, 2, 223, 1005, 224, 659, 101, 1, 223, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 674, 1001,
         223, 1, 223, 4, 223, 99, 226])

    test_programm.execute_codes()
    if len(test_programm.codes) < 15:
        print(test_programm.codes)


class Day_6():
    def __init__(self, gravity_map):
        self.gravity_map_str: str = gravity_map
        self.gravity_map_dict: dict = {}

    def create_dict(self):
        strings = self.gravity_map_str.split("\n")
        for orbit in strings:
            center, astroid = orbit.split(")")
            if not astroid in self.gravity_map_dict:
                self.gravity_map_dict[astroid] = set((center,))
            else:
                self.gravity_map_dict[astroid].add(center)

    def number_off_suborbits(self):
        number = 0
        for _, orbits in self.gravity_map_dict.items():
            number += len(orbits)
        return number

    def add_dependencies_to_gravitymap(self):
        last_number = -1
        while True:
            print("starting iteration with ", self.number_off_suborbits(), " orbits")
            for _k in self.gravity_map_dict.keys():
                try:
                    for center in self.gravity_map_dict[_k]:
                        self.gravity_map_dict[_k] = self.gravity_map_dict[_k].union(self.gravity_map_dict[center])
                except KeyError:
                    pass
            if last_number == self.number_off_suborbits():
                break
            else:
                last_number = self.number_off_suborbits()

    def get_distance(self):
        santa_orbit: set = self.gravity_map_dict["SAN"]
        you_orbit: set = self.gravity_map_dict["YOU"]
        return you_orbit.difference(santa_orbit).union(santa_orbit.difference(you_orbit))


def solve_day_6():
    starmap = Day_6("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""")
    starmap = Day_6("""MQD)G37
MPH)V45
SWV)KGL
M5T)SG3
M69)788
MQG)RBF
YVM)J5B
GHH)G3Y
VS2)6L4
86J)15R
WB3)4F5
LVM)4P4
HZW)CBG
Q7S)1YX
3F1)8XQ
YLR)Q7J
9WV)JN4
7SN)4TX
6HC)P24
VJR)J3L
CMN)ZCT
S7C)TC3
JTK)ZDR
ZVF)49D
TY1)3HB
W6Z)PXP
K7H)C4J
LVH)XPC
6ZP)Q94
GTR)YG3
LHS)PWC
5NN)T17
JYL)5Y1
8HQ)8H6
RTZ)C6F
8NK)PS2
W5F)SSL
1SW)GQB
ZVR)GCP
GMM)ZCJ
QGD)K7X
363)KQY
VP9)NP3
8B7)H18
S1N)1LG
C3Z)XPX
VQ8)8T5
1GR)H9S
J6H)SCK
8FB)YR2
TJ9)BTV
LK7)DQB
SJC)DS3
NT9)RTR
PVD)WCP
Z55)YVM
N5X)1W8
QBL)X2B
SZ6)8Z8
1MY)YHS
74K)1R7
SK5)CVW
LW8)KB4
3YJ)F48
B1F)H5F
3J6)LDP
Z11)657
TZX)556
92M)DJ5
BC3)PJH
CDX)74K
D88)GTR
QNP)MV2
YYQ)X6B
DXC)NGZ
L7M)NRL
M9V)XQT
Z6P)S96
G9P)8FB
27V)MFP
994)WJV
B4F)WMF
LDG)1V2
8Y1)G7S
32W)LCB
KXM)9HP
QS9)G6H
FBK)H5Y
FRK)5V6
VN1)KZD
PH4)18P
RL4)7S8
5XJ)JSB
J6Z)7ZC
2YF)MMQ
6VM)M58
7S8)XNS
JTL)T9L
PT1)LZ3
D4M)5TD
TSP)PT4
PNF)6S7
5TV)WDP
SQ2)71W
DYV)CX2
RX7)9JF
NRW)6B3
2CZ)B23
PD7)T19
25H)RBY
YPX)38C
FDD)NRW
FBN)ZK4
9HP)T5B
K18)YSC
7BC)SZV
SRX)PWR
SXG)YWF
Z21)3L5
Z2H)8VK
B5X)S1Z
7Q9)11X
1F3)6H6
P7S)D6H
YVH)1LW
GGJ)FFG
BM2)L21
ZSK)92M
CML)3L7
XZ5)ZKZ
1HH)WS8
D1C)2KJ
GHM)SJX
1XZ)D63
XKN)KHM
2R9)2B7
VCV)JYL
5LN)R15
14J)1CC
5Y1)BD6
5P3)67Y
B1N)HZC
SCR)YDY
9FX)TTN
LWQ)18X
Q1M)HPX
17G)223
H8Y)W6S
FL1)76F
3LR)97C
H4B)LZR
PPD)DZB
VJY)WP2
WV8)HBY
MN7)WHS
Y1G)PL4
WL5)TYM
RQ3)4R6
52F)7WL
RJR)MK6
7BT)P6J
5FP)PVD
657)YR4
9CX)9PB
15R)QJ4
2KJ)SDN
G3Q)MS6
SDN)986
1J5)DHB
V4M)JL3
WGM)Q9F
DV4)BCM
9WS)GT5
3W4)SGG
7NP)GLP
R2V)D88
WQ8)58Q
8XB)RJD
QQT)9HW
5ST)PS8
4YT)J3P
FGX)GHN
S29)3TM
31M)F34
34H)CZG
R7M)414
KJ8)VQ8
BPB)65P
66X)VGS
44N)2W3
WRR)7MS
VXH)RRJ
PBK)N7R
GDM)44N
1HX)WKD
3YQ)S97
ZTH)ZQC
QF8)RZL
SJB)6R6
72D)R5M
41V)L12
23D)JLJ
D4R)K7V
2VV)YPX
NKC)4T6
7KQ)JFB
QBR)5G9
2FY)99T
C12)8PL
WCM)SVZ
3TQ)C7G
1F3)JCJ
Z3P)YYQ
RBF)5NN
WQ4)9DV
SSX)X4D
YR2)8G6
KLT)PT2
P7R)J5Y
78R)568
Z8C)5T7
P91)9H6
CNN)ZDS
JZN)DQC
211)M69
KXJ)B9B
VLJ)YQR
8WB)YTN
3TM)Z8K
N64)LY3
GKC)429
GTV)JT2
5W5)7BT
VGG)L5P
K7B)X2D
WRZ)5P1
RBG)PT1
JV1)LCT
PSV)ZKX
H1J)55C
35M)KXM
HTT)TJ9
ZG8)75V
6V7)FC3
GRV)39S
Y72)YXZ
VM4)QS5
95L)C5D
5P1)5XS
QQ4)6LL
WRK)N1N
XT5)6VZ
TRT)783
RQC)95N
769)XZM
QLQ)4QL
H5S)25Z
9W7)M48
568)5LK
Q3D)GD3
PRT)QCQ
WCS)FBB
X43)SJC
4QH)KGQ
F82)Z65
RJD)BBQ
BNN)4PD
3HD)7YY
BXC)2LN
2TS)MYR
K6V)LK7
551)XK6
9GF)WK2
VH8)4KM
3C4)HNV
619)8YZ
HF2)SWP
BJS)XCX
LR1)KSX
GCY)NP6
TC6)9RZ
JKP)V5N
3SK)FJY
CQX)HSW
DFB)Y82
HLS)JJ3
BM6)WL5
SFW)4JQ
YXZ)5SX
W49)27V
MYG)2LV
2NK)RL4
556)55P
MYT)CXJ
HW6)93R
HMZ)HPF
S95)54V
5LK)YF4
D42)T71
86W)BDY
HRN)ZX9
K9S)95D
NHQ)X5W
LYF)75B
WYK)NBT
YL2)SXG
GBV)LJD
JBP)Y72
LN2)G6G
6DG)BR9
C6Y)VKX
KYS)B3V
59B)1KZ
4RC)6J5
CWP)W5D
5FP)D44
9SF)9PN
1ND)Q1P
ZYC)D6K
6S7)GTP
K5R)S1W
RYX)PBK
JFB)F9C
P3J)7MQ
S29)8FC
924)T26
QB1)9F9
4ZM)G3Q
HGP)PD9
9C4)4KK
JR4)Q11
SLL)KW6
2W3)LJC
Y7C)PH4
KFV)T8K
4KM)G76
CZW)FPK
YYL)17J
H55)R71
QB1)R5D
KQH)WWN
F2R)D1K
WZB)T8G
9LK)M9T
PVW)ZBQ
V5N)BQ8
Z63)Z6X
QLH)SCR
7VS)TRT
NP6)4J9
YGN)TZX
G23)BC9
23S)PXY
QFK)CWP
WS5)PXV
KFL)CHV
X5V)C17
XBV)17L
783)S3S
GD3)YPL
K9L)9S7
48B)TGG
BKP)29M
FYB)BHM
YDY)7SC
7K1)XHR
GV3)B3H
QJV)XQQ
758)F4G
YJK)PNF
4MQ)7V7
ZVD)YTZ
COM)FJH
51M)NNL
JR4)LW1
X5W)PX5
P3F)BB9
5KT)MF4
GSH)YZN
CXW)SB3
N35)F3M
LHC)KLT
72K)LR9
F3M)F7M
ZBQ)934
SG3)NKC
ZVM)6R1
H97)C3Z
2YN)CML
QS5)25H
RZL)NQ5
DL6)9QZ
LR9)D29
Y7C)75G
BQ8)DK3
7CW)NHF
2D6)9GW
CMW)6QY
F4L)KKM
FJY)S1H
W45)6CG
9L8)TSG
2MQ)NMH
3BB)5TM
1LW)MQD
HZC)273
TZF)GXT
38C)4QS
XQ7)662
5N6)2JQ
7QN)9KH
5TM)5C9
PTC)27Y
K3H)5X8
FDM)N5X
LWF)SPT
8VK)R7Q
1C3)VJP
25B)YQV
S75)F44
DRX)Q93
B23)X41
B6L)DS2
VP4)K1V
C6F)ZMV
ZCT)VLJ
3MP)1DZ
889)MVK
MDR)4ZM
H6W)4S5
JR3)KFH
6RN)Y6T
V8W)7ZS
4QK)TZ5
7GW)Z11
H9Y)4SF
PWR)GHV
V2C)TDM
PWB)QPL
7CT)6G7
M2S)PD2
DN2)VGG
9CD)SNF
4S4)KGC
P5B)GRV
R15)BM9
7FC)LZN
JN4)31X
8Z8)TBM
DS3)QY3
NLS)W11
KQZ)XJF
7H3)N3H
QY3)QS9
LD6)4YT
6YT)9H4
H93)D1N
KL7)DPC
4QJ)8YV
75B)V2C
VCN)42S
4BN)3DC
7C5)CR5
FR3)FTC
RTX)ZSP
QJD)SJB
2XF)Q5S
63Z)HK8
R5M)CJQ
6V3)VLS
33W)73Q
ZV7)SR1
4N8)6K9
1CC)GCY
T19)6ZB
B5N)JMH
54Y)Z6P
P6J)YZ4
XNH)KPC
9D7)7SJ
FJF)CF2
SMN)8F5
7T4)PPB
BDH)RD4
PL4)7QW
CS5)51M
XFB)X98
9JF)MQG
XZM)H5S
KN1)M2P
XBV)XGN
X41)73K
DDK)WV8
TBX)BNF
1G1)P5T
V4Z)2HM
3CY)ZWR
N88)ZR2
XK6)XWK
BRN)DQJ
GKG)YZS
RL5)FS4
ZDS)WQ8
84S)FZM
HK8)9C4
NCY)9W7
D1N)WNS
XCB)RSL
P5N)NWH
S9T)KVG
RRD)XJP
6R1)VP4
GWV)K8G
DZ4)C3K
7T6)VPY
WZV)RLL
KT3)HRN
5L6)NF6
416)V2Y
YPJ)GZ3
DXR)GMM
MN9)CWH
DXC)Z6C
ZB6)15Z
61N)54Q
WNS)KYY
CMN)9ZD
8YG)K5R
L92)FGK
SJX)34C
P5C)BYB
DT6)ZPS
R1J)3MP
18X)CJY
2MM)CHY
VGL)KK7
V4D)H1J
6NT)GSN
65P)RP7
ZFY)LSX
G6H)1G1
939)R1J
PHK)V1Y
JCB)7L2
8N1)BF9
Y9R)WCM
LDX)2YR
LYC)JRH
9YK)9SF
ZK4)RWD
5BG)GZZ
3DC)31K
TB1)Z5Y
73Q)HDR
PD2)RTX
Z94)79F
HVW)BXP
745)FYB
WQB)JWH
VBP)SPH
3QR)3GG
4R1)TZF
DS3)HY6
1P2)LGZ
QT5)WZB
TRZ)BJZ
KTT)681
LJP)Q1H
848)M6H
L93)7J4
XLG)MCK
1KZ)DWJ
8M7)PKW
WKD)WWR
G73)CBL
863)DBQ
3Q8)CFY
PRH)5D1
CBG)9L8
Q6N)CFT
HC7)B9L
TG9)B4Y
82P)SFW
X5K)R76
9MH)CMW
G7S)47G
VKG)C61
9CX)S6N
3H8)VZX
95M)24G
P4F)QJK
81R)5LN
C4J)19Y
P5T)HFV
LTX)JR4
62P)C7M
K11)KJ6
KZR)1BJ
DNP)RBG
TT1)VFB
JNP)M3V
395)WZV
MM2)91G
3N9)Z5W
J5L)H9Y
W5N)J6H
CFR)QJB
YP3)6V7
FVL)M2Y
VXP)B4R
YW8)K7H
66W)RDP
PPF)2MM
QX1)6NT
H45)11W
JKK)9J1
MT1)WDY
LN9)BTK
JT4)YW6
BYB)YB5
YM1)HMZ
Z2L)L2Z
CST)14J
X9P)1BD
RTB)WRR
FZ6)Z1S
HQ5)63T
R15)M2S
XGQ)K6L
Y55)QFB
T1X)JTL
HRB)NGV
HPV)3RG
6ZP)GHH
QS9)74W
H8N)9Y6
14C)8NN
YJZ)YDW
CJS)WZ4
2PD)RH4
5T7)L5Q
5WW)12D
SDL)SWV
ZM4)HYL
TQG)QC7
N35)W45
GZ4)MM2
R7F)FBK
SBN)RRD
GXT)WF3
D3V)LG2
S7R)LN9
GC3)3VP
X4T)2D9
M9Z)Z44
6VZ)54P
CVW)WZF
LZ3)CLC
15P)6RN
7FF)Q7N
7VL)243
JYK)QP2
YMN)LJW
FH8)BFN
7SJ)B8Q
KJ6)LYD
BXJ)FMH
TKW)75J
D7Q)DRN
CBB)3H6
SGG)BNN
8Z8)9S3
8LV)QC1
CJY)RYX
LQ2)Y9T
NCY)SQF
DJ5)H6W
57Z)7SN
XPX)KNW
Y5H)RF8
MYT)RL5
FLY)6QV
62P)2R9
2Y7)QQT
K9D)HC7
6DN)716
DV7)7G5
V1M)Q3P
TJB)TXH
5XC)49P
QTD)CWF
821)1J4
TTN)D86
T41)FHL
Q93)GPP
R5R)4BS
PXY)N64
CQR)YCT
NYW)7RZ
X3C)BW5
5XB)QFK
5FQ)3TG
1LG)4FH
TB5)RCY
YSC)7ZB
MSK)W5F
WRK)KYS
YHS)1HH
7ZB)3YQ
WCL)QGD
P1S)SKR
S3S)GN3
SYT)S29
BBQ)FH6
TH7)86W
LVM)266
XGN)J11
HK8)L2B
DVW)1T7
9GW)NHG
1Q2)HMW
BF9)L32
J4N)L8P
ZZH)H2L
662)7NC
XK8)HLJ
L33)1ZW
1W8)4P9
9PR)H1F
1V2)YX3
KZF)SBQ
KYY)DS5
W2X)GTV
CQM)CL2
TBX)XQ5
JDJ)SQB
DGG)96S
VWX)MS5
X8P)WQ4
S1W)JFT
9S3)HVW
9D6)78R
BW5)KBJ
K1V)13J
SNF)X43
TTD)VGL
Q7J)N5R
1BJ)WK3
11W)HXZ
Y82)WKB
W6N)W8T
85V)WV9
WMF)F1Y
SK1)HP1
TVC)NSV
KGC)66W
T1V)SK1
HKF)SXS
95L)GBV
7CL)W49
YTZ)8R6
FJ7)HN9
2NB)GTN
SSL)M3H
JV8)SQL
D7N)TSQ
XTL)QPX
JYL)956
W6S)XZ5
V1G)6ZY
HC2)MM1
6QP)3CY
7KW)DDK
4HV)Z2J
GHV)KTT
829)32W
5R9)X4F
7J5)Y8W
9F9)GTT
49P)ZL4
D2V)SAN
L2W)DYV
6H6)TZM
HVJ)K9R
KPJ)BC3
25Z)JZY
5V6)5R4
JZY)5ST
1F1)CS5
N53)ZDN
9G8)181
DPC)PB4
1SP)48B
95F)XMT
Q8W)HBM
J4H)R7F
D7T)TXM
CQR)X3C
7C6)FHH
1V2)CP6
X7L)9PS
F3F)Z8X
HNM)NB7
GW7)X69
D1K)4XP
F7D)HNM
SDX)2ZR
HHS)BY3
NK9)52X
1C5)CJS
GBQ)JV9
7SL)KY3
6CG)2XQ
7YY)X85
7B7)DT6
JCJ)72D
KSX)K9D
2ZL)T5Q
4BQ)QBR
9H5)SBN
5PV)L56
7WW)745
5W8)JZN
JRH)VK3
D6K)T7Q
SWF)J7T
5TD)S1N
6GM)2Q2
FJH)XLG
XWK)Q1M
NN2)8SY
7DP)FLB
QFB)YLR
MVK)K3L
F1Y)Z93
VP6)359
KVG)93K
YTN)2Q9
S11)FJF
1K3)R6H
8DD)D4R
H5F)Z94
4YC)QMW
NYQ)NLQ
YPJ)KPJ
93R)ZVR
5SX)31Z
V2H)9PR
D8L)T4F
FGB)343
Q79)9WS
Y76)BGD
97S)NLS
MQG)ZTH
D29)T1V
575)QLQ
WDY)LDG
2RM)926
BNF)S11
X59)6C4
CPN)GDY
WYL)3HR
XGS)4R1
Q6G)LVV
RTZ)M5T
VDQ)QZ9
278)3RV
VG2)CCD
Q3P)HW6
B2P)7BD
LSX)MKF
LZN)2Y7
6TV)7CL
9YP)BJS
HN9)T91
QBW)XZ8
9GN)9SV
JLF)ZY1
6ZS)1BY
RWD)TZQ
MMQ)WXH
7MR)GHM
WV9)W4Z
3J9)XSB
Q11)QBW
63T)GV3
X2B)K2G
MN7)BPJ
RF8)52F
4QL)H4B
JMM)2G4
B9B)Z7P
4JQ)XFX
V17)ZB6
YJM)95F
WYF)V9Z
Z6X)JBK
GCP)B9P
S8H)XXK
ZCJ)P7R
1NV)V4D
Y3N)5TV
CHY)84S
LTK)96G
MY2)PKT
JDP)Z8C
3L7)GQL
JT2)BDV
GK8)5PV
PK8)F2R
XGQ)GMN
DL2)NYQ
JWH)D7Q
MK7)QHJ
NTX)HC1
KW6)VX3
LW1)6FK
8H6)JDP
YL8)1LR
B4Z)P98
54K)J4H
QSQ)ZFY
Z71)FDM
KGQ)D7T
FFG)T6N
2GT)DQ8
W5N)C51
BWM)DNQ
2TL)YQ9
MTJ)645
7HX)VSC
V45)XN6
GMN)54Y
ZK4)G9F
4XP)C76
Z1Y)RLQ
DB4)T4N
88L)YJM
KC3)WQP
T79)L93
5JS)GFF
C3K)8F6
D5W)B5X
1ZW)WGM
39S)517
ZL4)4RC
JLB)JYY
B68)RBC
CM2)SL7
T8G)YVF
DFB)PGM
GPP)9CX
S2Z)55L
T56)8GW
3RV)JDJ
DD2)Z21
YZ4)MN9
55L)ZJL
WLT)M84
1Q2)P5C
SMB)T79
514)841
C94)S4Z
BR9)XQ7
B3V)B1F
YCN)7VZ
FB7)TH8
YZ2)THZ
X2Q)6V3
D8G)95L
D1N)Q1J
LFX)YYL
SVZ)Y76
RCY)DWD
BTK)PGN
VC4)8VQ
2RD)PYH
JMH)JQL
SQF)LVM
CBY)GS5
G7Z)NN2
VLL)CBY
LHS)XQF
8GW)QM5
4TH)LW5
7SC)7C6
YG3)Z1Y
3TK)8KS
RBY)NZJ
CQ7)1F3
2R5)7XG
RPL)HF2
71W)S9T
ZQC)YYD
PKW)17T
QPL)HTT
KMB)GS4
LDP)Q9J
S3J)25B
K6Q)3MD
Z42)VCV
956)9V8
4NH)DFB
GJ6)2CZ
J11)C6V
4PD)3YJ
QNG)GW7
67P)NM7
QZL)G1M
J33)Q28
XFX)CDC
QP2)TRZ
ZPJ)8QG
KHM)WLD
FHH)JKV
VGV)46M
5X8)XBV
55P)ZFF
1DX)LK3
861)4QH
5D1)MK7
6LL)NWC
F4G)GHY
FRN)QDD
4MT)9H5
65P)4GS
GQL)QTD
LDL)H8T
CXJ)VHG
FTC)591
VV6)QZ1
1J4)TJL
1DM)FL1
FL1)NNT
JFD)9FX
XVS)TTD
Q1P)X5K
429)CXF
75V)D8L
XQT)5W8
5ZR)LVY
WK4)7B7
C7Z)BB7
QHJ)LHS
PJH)JD3
17J)WRK
J5B)JMM
MF4)CRF
QT6)JV8
XCD)2XD
WD6)389
DFV)L9D
FYP)C55
KRP)8M7
ZFZ)LVD
LTK)MSK
MPT)D8G
QJB)T25
HCP)BSM
DQ8)W12
H18)ZVM
M7P)R2P
NM7)CXR
GJW)9MH
VPY)22Q
THZ)TY1
4JQ)W69
GV4)MD5
4F6)XYV
YR4)6JT
5MN)NGY
4K2)7H3
WZB)YYB
8YV)Q6N
XN6)FH8
DQB)3FB
HBM)J8R
223)WBH
1M4)KT3
CCD)ZRN
Y8M)5BW
FS4)WB3
YVF)XH5
PB4)H7X
9J1)PF1
X6B)MZX
XQ5)6WM
57Z)P7S
V49)P91
8LV)TJB
N5R)ZVF
WS8)XRT
X4K)8KZ
YQ9)SZS
Y6T)Z2L
2HP)1BS
ZTH)5W5
PSX)P32
WWT)8WB
QV9)QBL
986)3RY
MQT)CQX
C51)HGP
DQJ)7JW
QL3)DFV
Q9M)Y7Z
QZ1)YMN
P1Y)584
T91)83M
FH6)FGX
QLJ)N53
R5D)VM4
8SY)67P
N3F)363
HBY)SK5
V1Y)X8P
Y31)63Z
3JF)1F1
6G7)9B8
3JF)6QP
KB4)3SC
95D)RTB
591)S7R
5P1)9YK
H9F)P3F
6QV)LR7
WQN)7BC
R5H)K5P
JJ3)CMY
25M)QQ4
NP3)DL2
KDY)TKC
QMN)B85
R7W)YOU
Q9J)YNH
Q2G)SXK
C5M)GKG
XQQ)KLM
W4Z)BDH
X3T)QF8
7ZV)939
PS2)5XB
PX5)4QK
R6H)351
5HH)5JS
9MH)848
235)D2V
VJP)WWT
TG7)7CT
9M3)PPF
GQM)29Z
CZG)SNW
DQ1)66N
PK9)GKW
B4R)QZL
256)WTQ
645)H8H
G1G)29X
8BZ)TG6
YCZ)N1J
N88)G9P
VQR)DQ1
VC4)Y31
FH8)WYK
66N)4MF
CJY)Y8T
9PB)LDL
882)JNX
58Q)89M
2MQ)FJ5
V5X)DV7
XNH)76D
RDP)1T2
31Z)S95
4J9)KQ3
LCT)C6J
K9L)R3P
9B7)8LV
7FT)77G
7ZC)SNP
HP1)HWZ
S4Z)4WP
M58)TQ5
P6L)4N8
SNW)FKT
56J)J5D
ZQC)VN1
X69)882
8D4)155
3Y1)8M4
M5L)4TH
M48)V1G
WK2)M6B
18X)XR6
QJK)RLK
W12)Q2G
7RZ)4Y3
KPC)5S8
NNL)7NV
X8Y)4G8
6QY)XZG
NMH)SYT
9KH)SKB
BKW)Y5H
XJF)VKG
8M4)WT2
T8K)SMB
BY5)994
BB9)L38
QVT)SCX
4T6)2SZ
9D3)KFL
584)6ZP
PPM)S8H
19K)NYZ
W8Z)RJR
ZMV)7KW
45T)YK9
KY3)Q2N
Z6C)9LK
CLC)7FC
CRF)N44
GMN)C5M
XQ5)R8G
9Y6)HMX
Z7X)JY5
79G)2YN
B79)F8D
CD2)S2Z
DN1)FR3
K8G)D9R
LGH)WYL
1DZ)DD2
11X)3JX
WF3)FB7
273)V49
5BW)HT2
3VQ)FGB
8BZ)1K3
JXV)ZG8
QQK)KJ8
PZC)YZ2
WLD)P5N
QKT)619
JL3)DPG
6J8)CMN
72K)LDB
R1W)V8W
T4F)6VM
ZKX)QZ2
CVJ)CRK
B85)8SZ
DH3)P5B
WLT)9SH
N7R)DPR
T9L)1P2
4R6)PD7
TMV)X5V
MS5)PHK
1GP)CP8
3SC)M4K
DRW)6JS
9PN)2NK
LVV)BCH
CML)23S
4SF)WCL
L7M)Q27
9PS)7C5
JL3)VWC
1BD)7WW
NGY)QSY
M91)CM2
V24)DV4
S97)TKW
HLJ)4T9
WTG)P1S
JV9)J2B
KKM)2XF
R2P)3C4
4P4)2GT
M9C)3J6
94G)HKF
KQ7)GFY
5WW)6ZS
DPG)85V
SZ6)QNP
JFJ)6XD
T19)HRB
RYS)6GD
2Q2)DH3
MZX)Z7X
5H5)QX2
PXP)FJ7
V52)X8F
Y6C)S7C
H81)KB9
BDY)6YT
B9P)3CQ
KGD)M9Z
8Y1)4MT
GW2)KD2
4HV)CQR
VG8)6NW
PGN)M6Y
LTH)MB4
FT1)PPD
XH5)GSH
SCK)ZSK
9B8)YW8
HLX)JNP
YF4)VH8
4S5)KRP
W37)TB1
5YT)D3V
6ZH)CPN
4LF)9RX
L56)1SP
CXR)3RN
Q1J)F4D
KFH)R7W
BPJ)JLF
D86)XVS
GF9)5ZR
H1F)TD9
74W)V2H
M3V)842
9S7)Z55
M4K)8Y1
TTM)79G
97C)WXR
PWN)VV6
SZV)1CJ
3LH)S59
T2J)W44
5XS)SJN
YVK)BJF
R5K)FW2
395)2TL
GSN)M8S
MQT)H9F
842)TH7
PXY)QHG
DL2)1YF
5Q2)X59
V15)JV1
X9K)YQK
MFN)HWF
Q94)QVM
GTP)32S
BJN)CFR
6JT)FSF
JDK)X7L
SZS)FBN
15R)R1W
DDK)59B
681)7FM
Z72)PH5
5GD)BXJ
B4Y)GV4
5G9)X44
S64)7MR
JHS)821
YHS)T7J
KD2)KMB
PXV)4HV
DK3)4YC
S79)823
F4D)2RM
MD5)DGG
3H6)FT1
17L)KXJ
NLZ)N35
ZWR)X8Y
HMW)K9S
W8Z)M2T
38C)NK9
GKW)1VV
P98)LD6
WBH)3WV
QLQ)H16
WXH)7TR
J7T)5H2
TXH)VLQ
HXZ)QW2
NT6)94P
YW9)R5H
VK3)QKT
SN2)QDS
JXM)QT5
76D)MN7
7L2)PRT
99Y)BKP
3W4)YY3
46M)15C
JLJ)15P
CDC)MYT
BM9)LYF
GZZ)SDX
X1K)V81
TYH)9CD
2JQ)GC3
HJ2)X9D
QJ4)4KR
8SZ)ZTV
3MX)3KX
K3Q)278
GHH)TBX
3WV)SN2
JKV)ZQF
C12)Z8N
1YX)79V
WTQ)SQV
L21)TXC
59B)56J
S1H)Y9D
Y73)BM2
BC9)M7N
QM5)LWQ
PKT)L2W
5W8)8GJ
6L4)5XC
Z88)7NP
7X1)P4F
N73)5KT
4QH)VWX
23G)PZC
X8F)KM8
42S)YW5
QCQ)8QV
7ZR)CQM
H94)X9J
S1Z)MYG
4T9)NYW
P2J)PK9
L1H)7FT
4GS)YW9
ZX9)928
RD4)423
SY7)NHQ
NJ7)T41
T71)Q79
H6X)Y7C
7ZX)B5N
CMT)J6C
4P9)RYS
DS2)XPP
V2Y)8D4
GWY)XS8
Z8N)6GM
NSR)5WW
RH4)LGH
PH8)Z42
SQL)GQM
MZG)GW2
C76)MFN
C6J)F2V
6NQ)DN1
XPC)3H7
XQF)NT6
VCQ)5KL
YQR)XT5
JKD)FDD
1BS)7VS
K7X)1GP
KGL)W5N
BH3)26W
W8T)W3Y
4G8)1S2
2YR)YCD
VSL)LN2
7JW)KGD
SPT)PWN
8T5)G2W
55C)6BG
D95)B6L
GN3)769
PPB)XFB
Y8W)VDQ
WWR)7T6
YQ7)SDL
1D2)XNH
BFG)3TK
7T3)5N6
MK6)GZ6
8F5)VJR
VLS)DVL
WKK)FYP
F6C)KQ7
VLQ)ZPJ
3MD)Q7S
TJ6)JFD
SGY)H45
16V)42V
J5Y)F82
QT6)M5L
W45)RQ3
PW5)8NK
V9Z)NHZ
LR1)7ZV
G37)G23
BD6)NTX
PL9)PSV
TB5)BRN
LJC)ZQN
Q5S)PN8
CB7)7ZR
GGS)V1R
ZSP)R3L
H8H)GKC
3BR)1D2
NWN)NCY
NR7)WCT
TXC)S2T
PZC)GF9
47G)TNB
G6G)YWP
N1J)HV8
6ZB)M9V
R76)WYF
QPX)51Q
ZRP)WHX
ZBM)L5G
C6V)K9L
N28)JKP
3VP)W6Z
BTV)XK8
PN8)4SN
838)6L9
87D)H3B
BZK)VJY
TKC)FTY
CXF)4LF
WZS)416
XR6)MZG
YCD)S64
N44)89S
4SF)V52
T4N)WQB
GTN)5W9
RK3)72K
94P)JT4
2HM)1PN
C5D)Z2X
MFP)N3F
9YP)BM6
N7H)BY5
YDW)9M3
D44)L1H
HRN)XGS
YTP)X9K
QKT)QT7
W69)H8Y
XJP)7VL
STJ)JVH
QT7)H8N
Z42)BFG
NQ5)VXP
14F)LFX
J8R)YTP
9Y6)L8K
GZ6)2NB
QJ4)DXR
89S)QQK
WXR)CQ7
LVD)DB4
Y55)19K
NGR)FRN
9MT)XCD
F9X)M9C
7FF)92Q
PN7)21G
8KZ)JH4
SB3)3LH
77G)3VQ
2ZR)GGJ
QT7)C7Z
7P7)4K2
S6N)STX
M84)TG9
QH8)QVT
QX1)63X
T7J)SKF
BHM)HJ2
12D)5NY
Q1H)68X
Q3K)Z72
B8Q)9YQ
HYL)P9T
QR6)62P
CF2)JXV
YZS)M91
9B7)9SX
9SH)LYC
K9R)2D6
8R6)X6F
GLP)G9H
34Y)YPJ
NTZ)4TC
389)ZPY
517)N73
DQ1)Y3N
HNV)8YG
KZF)2ZL
1RK)PN2
H8T)R7M
3Y2)WK4
4QS)2WC
NX9)VCN
KTD)GW6
NKW)VSL
C7M)6DN
HMX)X2Q
X4F)X6P
6FC)31M
4FH)256
51F)6NQ
L2B)PL9
J2B)3V5
YYB)RPL
5BW)M8X
CJQ)VG8
Z5W)ZWH
8JZ)Q3K
RF8)NT9
G1M)2PD
JD3)JXM
KZD)86J
WY2)BPB
KSN)QJD
ZP1)TC6
YY3)X9P
JY5)C6Y
54Q)5XJ
32S)GKK
6JS)BWM
72M)QBH
54V)W6N
W11)7T4
YB5)5GS
BJF)WKV
P2X)QJV
Z2J)MSD
M7N)L33
8RZ)57Z
CBL)95M
WCL)8HQ
8QV)35M
TSQ)72M
VGS)4LJ
PT2)235
9SV)HVJ
1YF)9D7
BDV)DBN
13J)ZVD
ZCH)9YP
KB9)25M
LQ3)Q7H
BCH)VG2
DRN)VLL
6GD)34Y
54Y)7KQ
DJ5)GJW
X6F)5BG
5RJ)QV9
C6J)S3V
8N1)S79
HSW)33W
841)4QJ
18P)R1D
PGM)DN2
L9D)NLZ
LDG)WRH
QY3)1M3
WC9)14C
9HW)ZPK
NHF)YQ7
KGZ)X73
889)HHS
42V)M9Y
Q6P)V24
48M)DZT
DZ4)5MN
2Q9)LVH
SBQ)WC9
MZH)59N
7XG)KVN
6DN)57K
22Q)8M2
CXX)6FC
MK7)YM1
TNB)Y4Z
S7C)41V
GS5)7K9
CX2)SMN
1LR)395
QQX)GD7
FLB)16V
TD9)6CK
TKC)97S
6XD)X1K
5W5)9G8
J4H)LW8
SKR)N7H
7H3)WKK
WYD)NJ7
7J4)5YT
181)Y6C
TGG)RHD
4TC)B4J
M6Y)B4Z
WRH)F8N
BGD)3MX
GHV)YJK
GNQ)WH8
VSC)45T
2XD)62Z
JRW)JDK
TCH)D4M
WQP)ZFZ
K5P)PH8
8KS)2HP
3L5)DZ4
YSC)B7X
1S2)GGS
LDB)CDX
9CD)S9W
YQK)R5K
L8K)1ND
4MF)TQG
VHG)SQ2
F34)CDS
91G)GNQ
5S8)JHS
KXL)DTY
BFN)GK8
M6H)54K
79F)W7D
JH4)MZH
99T)V1M
KGD)23G
W5D)JTK
3RN)D1C
KJL)7GW
9KY)5NB
RPV)14F
GKK)X4T
BPM)M85
2NB)LQ3
M3H)94G
J92)7QN
Z93)B1N
NRL)VCQ
31X)Y1G
5CB)8XB
9H6)9MD
24G)NHX
DNQ)SST
ZWH)5GD
DS5)453
Q28)BXC
934)6TV
YX3)6DG
9V8)QB1
M2P)KXL
TXM)K9K
H9S)8JZ
YBG)HFM
3TG)TCH
NYZ)3F1
3V5)KJL
MB4)NX9
DPR)9TX
MSK)6ZH
7K9)5FQ
S9W)NTZ
GFF)Y73
S7R)468
T6N)BJ4
M2P)R8M
PYH)HZ1
GZ3)6HC
CP6)QQH
STX)7SL
4Y3)K11
SQF)CNN
JFT)LJP
FPK)5P3
X44)MQT
G3Y)2RD
QZ2)9DL
54P)VXH
DTY)XZS
C94)P6L
SQV)3SK
QSY)SRX
DZT)F4L
YW5)KFV
2G4)W2X
1W8)HC2
RN6)Q4M
VB9)BH3
Q9F)YL8
GHC)23D
5H2)V47
8F6)QNG
15C)2GK
3K5)413
13J)WZS
GT5)DYX
YTP)924
926)5L6
3RG)48M
K3L)2CX
XKN)8DD
3P9)Y8M
Z7P)RN6
T5Q)YGN
67Y)4BN
FMH)4BQ
Q3C)QH8
51Q)LQ2
PF1)CXX
ZQN)63G
MKF)D7N
CWF)V17
G2W)T56
TC3)99Y
KM6)51L
SR1)1C3
SYT)DNP
NWC)JFJ
YZN)W8X
X36)TM3
NGZ)W37
Z8K)88L
T36)GZ4
P3J)9D3
SNP)MDR
PS8)SY7
49D)LTH
R5R)KR5
WX2)829
2LN)9M7
Z8X)ZV7
9ZD)3BB
2YK)TQ7
KM8)YBG
WTQ)DRX
WHX)K7B
L2Z)ZZH
K7X)5F6
P32)Q3G
TBM)KTD
MM1)514
H16)HH6
DBN)NR7
F5C)863
PWC)K86
R8C)1RK
R8G)CB7
F8N)G55
PN2)752
9GN)BKW
68X)LHC
HFM)81R
968)QQX
DQC)ZM4
32W)PVW
4J4)4F6
788)CM5
SCX)MYN
ZPY)7DP
453)QMN
4WP)Q6G
WGM)N88
LCZ)N28
KBJ)J5L
BCM)QL3
6QJ)838
T7Q)V4X
HY6)H93
YR2)MY2
M8X)RK3
7TR)ZQS
6L9)VBP
4R1)D95
WK3)XT6
ZZH)5RJ
KLM)S75
VH8)1DM
Z44)TSP
RLQ)WTG
VFB)9B7
DQJ)SBF
YCT)STJ
QJK)3K5
ZWQ)V4M
M8S)1XZ
15Z)DMM
C61)2VC
F2V)Y9R
SKF)PN7
TYM)F7D
413)WS5
G6D)PTC
HH6)W8Z
6J5)TYH
1T7)T2J
2WC)K3Q
8PL)RFZ
LW5)QLJ
7WL)82P
HFV)ZWQ
6K5)Z82
GWT)HLX
Z63)BRV
XZS)C94
QC7)4J4
82P)SGY
6ZY)HCP
XZM)C12
8PQ)LWF
9FX)NWN
PKT)9GF
5MN)K3H
F7M)Z2H
Y9T)Q3C
M9T)Z3P
D95)F51
266)LDX
LK3)JBP
G3Y)TMV
TJL)H81
TG1)NFT
343)9WV
YYD)XTL
3JX)51F
XQT)JRW
WCP)XCB
7MQ)NGR
SY7)KS8
8YZ)7J5
RSF)ZC5
R3L)P1Y
GDY)KSN
BB7)X3T
8XQ)2YK
WKV)Y55
XTL)PK8
WHS)HPV
CMY)BZK
5F6)JYK
YY3)K6V
75G)7ZX
57K)H6X
4LJ)S3J
63G)CHN
XSB)K4R
2YF)J33
HT2)1C5
SGC)PSX
FGK)QLH
89M)JS1
QZ2)4MQ
CGD)3Y2
SJN)G1G
4KK)2MQ
5R4)YVK
ZQF)WY2
DHB)DVW
V67)5H5
RSL)P2J
LYD)3BR
S3V)FVL
B3H)15X
7V7)Q3D
PD9)XGQ
WWN)LTX
B9L)R8C
YCW)1MY
DWJ)H94
XCX)LR1
TZ5)TG1
G9F)GHC
L38)RGM
S96)HZW
8GJ)V4Z
JMH)9D6
L54)D42
5DG)VP9
3RY)BPM
M2T)TT1
X4D)8RZ
6VZ)GJ6
MS6)KQH
8VQ)RQC
2HM)X4K
8NB)P3T
3T5)551
PN8)1GR
JYY)1KY
G55)1DX
JJ8)B4F
J5D)WCS
1CJ)JLB
YMN)1NV
G76)578
QVM)ZRP
XNS)FZ6
LZ3)8N1
F8D)NJC
CP8)TJ6
MCK)VS2
7NC)WXL
RLK)F5C
5W9)FWB
LHC)TG7
CHV)CMT
QC1)K18
NLQ)HQ5
C17)SGC
4SN)V67
9WV)FLY
DBQ)5HH
L5P)5R9
16M)3Q8
D9R)J92
27Y)ZYC
6PG)FD3
WCM)NKW
FD3)G73
8G6)FCB
FFG)X3Q
QX2)VQR
7ZS)VP6
KQY)DRW
V45)JP2
BHM)6PG
3FB)Z71
9SX)5Q2
6WM)VC4
6FK)66X
SBF)7CW
QLT)KC3
GHY)PWB
HGC)7X1
6K9)TB5
2DY)XT4
TZM)J4N
76F)JCB
X2Q)V5X
MV2)PPM
JS1)G99
1HX)5CB
P3T)VPQ
H56)87D
TQ5)JR3
7KQ)1HX
ZC5)34H
NSV)SSX
DF1)936
WWN)TTM
JP2)9MT
7BD)YCN
M9Y)G6D
PHK)2DY
Y8T)2YF
Z1Y)BFL
LR9)17G
4BS)XKN
8GW)JJ8
LCB)5WC
63X)9GN
NWH)YCZ
3H7)QLT
X6P)1M4
K11)MT1
L5P)861
96G)7K1
NHX)Q9M
3KX)8NB
T26)KL7
YK9)V15
D63)R2V
T25)968
3HB)G7Z
F51)6J8
N3H)GKF
YW6)8BZ
1PN)KZR
X2D)MTJ
LJD)HLS
PT4)81Z
WZF)SWF
92Q)7P7
Q6G)NSR
SGG)WD6
DVL)6M4
XRT)3N9
ZR2)Z88
HPX)YCW
DWD)6K5
PH5)D9L
G9H)HGC
LG2)J6Z
2CX)WQN
HZ1)7FF
NNL)B68
TDL)69K
VHG)3W4
B4J)QZZ
GKF)CXW
RL3)TGN
Z2J)RTZ
VN1)4PC
ZPK)GWT
W8X)D45
XZG)7T3
4KR)VB9
6R6)QR6
KS8)X36
GTT)L54
ZRN)RL3
D6H)F9X
VKX)ZCH
Q28)Q6P
PSX)K6Q
MT1)CGD
739)X74
W44)758
BXP)1SW
VWC)LTK
7G5)L7M
WKB)2VV
R8M)T1X
XT6)PRH
389)F6C
CRK)WLT
1K3)RSF
RFZ)BJN
X3Q)ZBM
NGV)7Q9
81Z)KGZ
29X)4NH
X74)B32
LZR)739
K7V)3H8
D45)J9V
JBK)P3J
RP7)1Q2
C7G)CD2
2B7)9KY
V81)8B7
4LJ)VGV
FSF)Z63
6B3)ZP1
L5Q)T36
2GK)NQG
FWB)D5W
6QJ)KDY
55W)3J9
KVN)KQZ
6BG)B79
Q7N)HWW
5KL)6QJ
CHN)1J5
FBB)3TQ
575)Q8W
4F5)BW9
K4R)YVH
Z82)KM6
LVY)TDL
X9D)55W
L32)211
RBC)3Y1
QMW)2TS
9TX)GBQ
R71)GWY
69K)R5R
SL7)LCZ
1KY)5FP
CR5)8PQ
ZDN)YL2
K9K)YJZ
716)5DG
FZM)M7P
MB4)TVC
JVH)DF1
XWK)3LR
FKT)H56
578)B2P
BJ4)WRZ
TGN)FRK
SWP)Q4Y
1M3)2FY
9DV)YP3
TQ7)KZF
SBF)2R5
351)16M
RTR)GWV
Z5Y)MPT
1BY)RX7
CL2)H97
L5G)DL6
RRJ)1DK
9MD)BS9
NNT)889
T17)3JF
9YQ)WYD
ZJL)JKD
6RN)3QR
ZVD)P2X
21G)NLF
B7X)61N
LY3)RPV
WS8)MPH
67P)Q8F
83M)F3F
XFB)QSQ
FJ5)JKK
K86)575
MSD)CBB
5WC)PW5
NLF)7HX
QZ9)CST
29M)1LB
BY3)4S4
1DK)H55
SPH)WX2
GPP)DXC
FCB)CZW
3HR)KN1
8XQ)3HD
4T6)3P9
XZ8)L92
7GW)GDM
7FM)QX1
K6L)SLL
QF8)3T5
1R7)QT6
3CQ)CVJ
5NY)SZ6""")

    '''starmap = Day_6("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""")'''

    starmap.create_dict()

    starmap.add_dependencies_to_gravitymap()
    print(starmap.gravity_map_dict["YOU"])
    print(starmap.gravity_map_dict["SAN"])
    print(len(starmap.get_distance()))


if __name__ == '__main__':
    solve_day_6()
