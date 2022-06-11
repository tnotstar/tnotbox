use std:: fmt;

#[derive(Debug)]
enum Language {
    English,
    German,
}

#[derive(Debug)]
struct Greeter {
    language: Language,
}

impl Greeter {
    fn new() -> Greeter {
        Greeter {
            language: Language::English,
        }
    }

    fn with_language(mut self, language: Language) -> Greeter {
        self.language = language;
        return self
    }
}

impl fmt::Display for Greeter {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let greeting = match self.language {
            Language::English => "Hello",
            Language::German => "Hallo",
        };
        return write!(f, "{}, Rust!", greeting);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works_2() {
        let greeter = Greeter::new().with_language(Language::German);
        println!("{} => {:?}", greeter, greeter);
    }
}