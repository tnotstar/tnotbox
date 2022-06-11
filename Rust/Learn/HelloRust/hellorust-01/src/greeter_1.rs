enum Language {
    English,
    German,
}

fn greet(language: Language) {
    let greeting = match language {
        Language::English => "Hello",
        Language::German => "Hallo",
    };
    println!("{}, Rust!", greeting);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works_1() {
        greet(Language::English);
        greet(Language::German);
    }
}