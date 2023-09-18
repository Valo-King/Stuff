extern crate rand;

use std::io;
use std::cmp::Ordering;
use rand::Rng;
fn main() {
    let secret_number = rand::thread_rng().gen_range(1, 101);
    println!("guess the number.");
    loop{
        println!("please input your guess.");
        let mut guess = String::new();
        io::stdin().read_line(&mut guess)
            .expect("failed to read line");
        let guess: = match guess.trim().parse::<i32>(){
            Ok(num) => num,
            Err(_) =>{
                println!("numbers only.");
                continue;
            }
        };
        println!("You guess: {}", guess);
        match guess.cmp(&secret_number){
            Ordering::Less    => println!("Too small"),
            Ordering::Greater => println!("Too :large:"),
            Ordering::Equal   =>{ 
                println!("You're Winner");
                break;
            }
        }
    }
}
