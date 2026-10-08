let pages = 47;
let pagesPerSheet = 6;
let fullSheets = Math.floor(pages / pagesPerSheet);
let remainingPages = pages % pagesPerSheet;
console.log(fullSheets);
console.log(remainingPages);