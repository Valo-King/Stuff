/// going to make a shift implementation as a way to learn me some RUST
/// it's gon be good !
use std::io;
use std::iter::FromIterator;
//use itertools::Itertools;
fn main() {
    let alphabet = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z'];
    println!("Shift Cypher");
    println!("What would you like to shift?");
    let mut message = String::new();
    io::stdin().read_line(&mut message)
            .expect("Failed to read line");
    let chars_msg: Vec<char> = message.trim().chars().collect();
    let mut shifted: Vec<char> = Vec::new();
    for (index , item) in alphabet.iter().enumerate(){
        for(index2 , item2) in chars_msg.iter().enumerate(){
            if item2 == item{
                shifted.push(alphabet[index+3])
            }
        }
    
    }
    let shift = String::from_iter(shifted);
    println!("{}" , shift);
}
