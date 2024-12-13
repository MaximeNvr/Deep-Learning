// Check if the 'resultat' variable is defined
if (typeof resultat !== "undefined") {
    // If 'resultat' is "Robot", set background image to robot image
    if (resultat === "Robot") {
        document.body.style.backgroundImage = "url('../static/images/robot.png')";
    } else {
        // If 'resultat' is "Human", set background image to human image
        document.body.style.backgroundImage = "url('../static/images/human.png')";
    }
} else {
    console.error("La variable 'resultat' n'est pas définie.");
}
