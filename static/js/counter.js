// Select the textarea element by its ID
const textarea = document.getElementById('texte');
const charCount = document.getElementById('charCount');
const maxChars = 5000; // Maximum allowed character count

// Add an input event listener to the textarea
textarea.addEventListener('input', function () {
    const currentLength = textarea.value.length; // Get the current length of the textarea value
    charCount.textContent = currentLength; // Update the character count display

    // If the current length exceeds the maximum allowed characters
    if (currentLength > maxChars) {
        // Limit the textarea value to the maximum allowed characters
        textarea.value = textarea.value.substring(0, maxChars);
        charCount.textContent = maxChars; 
    }
});
