use std::time::Instant;

fn main() {
    let mut primes = Vec::new();

    let start_time = Instant::now();

    // Start at 2, because 1 is not a prime number
    for n in 2..100_000 {
        let mut is_prime = true;

        // Check if n is evenly divisible by any number between 2 and n-1
        for i in 2..n {
            if n % i == 0 {
                is_prime = false;
                break;
            }
        }

        if is_prime {
            primes.push(n);
        }
    }

    let elapsed_time = start_time.elapsed();
    let elapsed_ms = (elapsed_time.as_secs() * 1_000) + (elapsed_time.subsec_nanos() / 1_000_000) as u64;
    println!("{}", elapsed_ms);
}
