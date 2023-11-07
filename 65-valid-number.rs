impl Solution {
    pub fn is_number(s: String) -> bool {
        #[derive(Copy, Clone, Debug)]
        enum StateMachine {
            StartingState,  // Starting state
            B,  // encountered a + or -
            C,  // A number that can be repeated
            D,  // A decimal point at start or after a sign
            E,  // A decimal point after number or a number after decimal
            F,  // An exponentiation marker
            G,  // Sign of exponent
            H,  // Exponent integer
            Accept,  // Accept state
            Reject,  // Reject state
        }
        impl StateMachine {
            fn pattern_match(&mut self, c: Option<char>) {
                *self = match self {
                    Self::StartingState => {
                        match c {
                            Some(x) => match x {
                                '+' | '-' => Self::B,
                                '0'..='9' => Self::C,
                                '.' =>  Self::D,
                                _   =>  Self::Reject,
                            },
                            None => Self::Reject,
                        }
                    },
                    Self::B => {
                        match c {
                            Some(x) => match x {
                                '0'..='9' => Self::C,
                                '.' =>  Self::D,
                                _   =>  Self::Reject,
                            },
                            None => Self::Reject,
                        }
                    },
                    Self::C => {
                        match c {
                            Some(x) => match x {
                                '0'..='9' => Self::C,
                                'e' | 'E' => Self::F,
                                '.' =>  Self::E,
                                _   =>  Self::Reject,
                            },
                            None => Self::Accept,
                        }
                    },
                    Self::D => {
                        match c {
                            Some(x) => match x {
                                '0'..='9' => Self::E,
                                _   =>  Self::Reject,
                            },
                            None => Self::Reject,
                        }
                    },
                    Self::E => {
                        match c {
                            Some(x) => match x {
                                '0'..='9' => Self::E,
                                'e' | 'E' => Self::F,
                                _   =>  Self::Reject,
                            },
                            None => Self::Accept,
                        }
                    },
                    Self::F => {
                        match c {
                            Some(x) => match x {
                                '+' | '-' => Self::G,
                                '0'..='9' => Self::H,
                                _   =>  Self::Reject,
                            },
                            None => Self::Reject,
                        }
                    },
                    Self::G => {
                        match c {
                            Some(x) => match x {
                                '0'..='9' => Self::H,
                                _   =>  Self::Reject,
                            },
                            None => Self::Reject,
                        }
                    },
                    Self::H => {
                        match c {
                            Some(x) => match x {
                                '0'..='9' => Self::H,
                                _   =>  Self::Reject,
                            },
                            None => Self::Accept,
                        }
                    },
                    _ => Self::Reject,
                };
            }
            fn evaluate(&self) -> Option<bool> {
                match self {
                    Self::Accept => Some(true), // accept
                    Self::Reject => Some(false), // reject
                    _ => None, // Inconclusive
                }
            }
        }
        let mut s = s.chars();
        let mut state = StateMachine::StartingState;

        loop {
            let c = s.next();
            state.pattern_match(c);
            if let Some(evaluation) = state.evaluate() {
                break evaluation;
            }
        }
    }


}

fn main() {
    let cases = [
        "0",
        "e",
        ".",
        ".1",
    ];
    let answers = [
        true,
        false,
        false,
        true,
    ];
    for (case, answer) in cases.iter().zip(answers.iter()) {
        let c = Solution::is_number(case.to_string());
        println!("output is {c:5} : {answer:5} expected for \"{case}\"");
    }
}
struct Solution;