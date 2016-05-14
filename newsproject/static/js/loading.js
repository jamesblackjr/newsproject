// Output a random loading message...
function randomLoadingMessage() {
    var lines = new Array(
        "Locating the required gigapixels to render...",
		"Please wait, we're testing your patience.",
        "Spinning up the hamster...",
        "Shovelling coal into the server...",
        "Programming the flux capacitor...",
		"Please wait, as if you had any other choice.",
		"640K ought to be enough for anybody...",
		"The architects are still drafting...",
		"Would you prefer chicken, steak, or tofu?",
		"Pay no attention to the man behind the curtain.",
		"Please wait, and enjoy the elevator music...",
		"A few bits tried to escape, but we caught them!",
		"Would you like fries with that?",
		"Checking the gravitational constant in your locale...",
		"Go ahead -- hold your breath.",
		"Please wait, while the satellite moves into position...",
		"At least you're not on hold...",
		"Hum something loud while others stare.",
		"The bits are breeding...",
		"Please wait, and dream of faster computers...",
		"You're not in Kansas any more.",
		"This server is powered by a lemon and two electrodes.",
		"Please wait, we love you just the way you are!",
		"Don't think of purple hippos!",
		"Dig on the 'X' for buried treasure... ARRR!",
		"Why don't you order a sandwich?",
		"Please wait, he bits are flowing slowly today.",
		"Follow the white rabbit..."
    );
    return lines[Math.round(Math.random()*(lines.length-1))];
}