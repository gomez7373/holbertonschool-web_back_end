// Display the initial message
console.log("Welcome to Holberton School, what is your name?");

// Capture user input
process.stdin.on('data', (data) => {
    const name = data.toString().trim();  // Remove any extra spaces or newlines
    console.log(`Your name is: ${name}`);
    process.exit();
});

// Display message when process exits
process.on('exit', () => {
    console.log('This important software is now closing');
});

