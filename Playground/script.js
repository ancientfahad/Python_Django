// Text to split PDF
try {
    // Define the coordinates and tolerance

    // 202, 592.846923828125
    // 229, 738.23193359375
    var targetX = 202;
    var targetY = 592.846923828125;
    var tolerance = 10; // Tolerance for matching coordinates
    var totalPages = 4; // Total number of pages in the document

    // Loop through each page and save it as a separate PDF
    for (var i = 0; i < totalPages; i++) {
        var wordCount = this.getPageNumWords(i); // Use 'i' for the current page number
        var foundText = null;

        // Loop through all words on the page to find text near the target coordinates
        for (var j = 0; j < wordCount; j++) { // Renamed inner loop variable
            var quad = this.getPageNthWordQuads(i, j); // Use 'i' for the current page number
            if (quad && quad.length > 0) {
                var x1 = quad[0][0];
                var y1 = quad[0][1];

                // Check if the word is within the target coordinates range
                if (Math.abs(x1 - targetX) <= tolerance && Math.abs(y1 - targetY) <= tolerance) {
                    foundText = this.getPageNthWord(i, j);
                    break; // Break out of the inner loop if found
                }
            }
        }

        // Print the found text or a message if no text is found
        if (foundText) {
            console.println("Page " + (i + 1) + ": Found text: " + foundText);
            
            // Create a valid filename using the found text
            var fileName = this.documentFileName.replace(".pdf", "_" + foundText + ".pdf");
            
            // Create a new PDF with only one page
            var newDoc = app.newDoc();
            this.extractPages({
                nStart: i,        // Starting page (0-based)
                nEnd: i,          // Ending page (0-based)
                cPath: fileName   // Path to save the new PDF
            });

            console.println("Page " + (i + 1) + " saved as: " + fileName);
        } else {
            console.println("Page " + (i + 1) + ": No text found at the coordinates.");
        }
    }
} catch (e) {
    console.println("Error: " + e.message);
}

// Code to look for text coordinates
try {
    // Specify the page number you want to analyze (0-based index)
    var pageNum = 1; // Change this to the desired page number (0 for the first page)
    
    // Get the number of words on the specified page
    var wordCount = this.getPageNumWords(pageNum);
    
    // Check if there are any words on the page
    if (wordCount === 0) {
        console.println("No words found on page " + (pageNum + 1) + ".");
    } else {
        console.println("Words and their coordinates on page " + (pageNum + 1) + ":");
        
        // Loop through all words on the page
        for (var i = 0; i < wordCount; i++) {
            var word = this.getPageNthWord(pageNum, i); // Get the text of the word
            var quads = this.getPageNthWordQuads(pageNum, i); // Get the coordinates (quads) of the word
            
            // Check if quads are available
            if (quads && quads.length > 0) {
                // Log the word and its coordinates
                var coordinates = "Coordinates: ";
                for (var j = 0; j < quads.length; j++) {
                    coordinates += "(" + quads[j][0] + ", " + quads[j][1] + ")";
                    if (j < quads.length - 1) {
                        coordinates += ", ";
                    }
                }
                console.println("Word: '" + word + "' - " + coordinates);
            } else {
                console.println("Word: '" + word + "' - No coordinates found.");
            }
        }
    }
} catch (e) {
    console.println("Error: " + e.message);
}

// Split PDF
try {
    var minX = 202; 
    var maxX = 300;
    var targetY = 592.846923828125;
    var tolerance = 10;
    var totalPages = 9;

    for (var i = 0; i < totalPages; i++) {
        try {
            var wordCount = this.getPageNumWords(i);
            var foundTexts = [];

            for (var j = 0; j < wordCount; j++) {
                var quad = this.getPageNthWordQuads(i, j);
                if (quad && quad.length > 0) {
                    var x1 = quad[0][0];
                    var y1 = quad[0][1];

                    if (x1 >= minX && x1 <= maxX && Math.abs(y1 - targetY) <= tolerance) {
                        var foundText = this.getPageNthWord(i, j, false).trim();
                        if (foundTexts.indexOf(foundText) === -1) {
                            foundTexts.push(foundText);
                        }
                    }
                }
            }

            if (foundTexts.length > 0) {
                var sanitizedText = foundTexts.map(text => text.trim()).join(" ").replace(/[^\w\s.]/g, "").trim();
                var fileName = this.documentFileName.replace(".pdf", " - " + sanitizedText + ".pdf");

                // Create a new PDF with only one page
                var newDoc = app.newDoc();
                this.extractPages({ nStart: i, nEnd: i, cPath: fileName });

                // Close the new document to prevent object locking
                // newDoc.closeDoc();

                console.println("Page " + (i + 1) + " saved as: " + fileName);
            } else {
                console.println("Page " + (i + 1) + ": No text found at the coordinates.");
            }
        } catch (e) {
            console.println("Error processing page " + (i + 1) + ": " + e.message);
        }
    }
} catch (e) {
    console.println("Critical Error: " + e.message);
}