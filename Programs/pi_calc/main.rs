use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // Set the number of threads to use
    let num_threads = 8;

    // Set the number of iterations to use in the calculation
    let num_iterations = 100000000;

    // Set the initial values for the pi estimate and the step size
    let mut pi = 0.0;
    let step = 1.0 / num_iterations as f64;

    // Create a shared variable for the result and a mutex to protect it
    let result = Arc::new(Mutex::new(0.0));

    // Create a vector to hold the threads
    let mut threads = Vec::new();

    // Spawn the threads
    for i in 0..num_threads {
        // Create a local variable for the thread to use
        let local_result = result.clone();

        // Spawn the thread and store it in the vector
        threads.push(thread::spawn(move || {
            // Calculate the starting and ending points for this thread
            let start = i * (num_iterations / num_threads);
            let end = (i + 1) * (num_iterations / num_threads);

            // Calculate the partial result for this thread
            for j in start..end {
                let x = (j as f64 + 0.5) * step;
                let local_pi = 4.0 / (1.0 + x * x);
                *local_result.lock().unwrap() += local_pi;
            }
        }));
    }

    // Wait for all the threads to finish
    for thread in threads {
        thread.join().unwrap();
    }

    // Retrieve the result from the shared variable and print it
    pi += *result.lock().unwrap() * step;
}
