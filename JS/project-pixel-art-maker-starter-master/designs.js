/**
* @description A colour selector for the cell in the grid
* @param {MouseEvent} event - activation via click
*/
function chooseColour(event) {
    const colour = document.getElementById('colourPicker').value;
    event.target.style.backgroundColor = colour;
}

/**
* @description Represents the grid for the future pixel art creation
* @param {Submitevent} event - activation via click
*/
function makeGrid(event) {
    const nCols = parseInt(document.getElementById('inputHeight').value);
    const nRows = parseInt(document.getElementById('inputWidth').value);
    const table = document.getElementById('pixelCanvas');
    while (table.firstChild) {
        table.removeChild(table.lastChild)
    }
    for (var n = 0; n < nRows; ++n) {
        let newRow = table.insertRow(n);
        for (var m = 0; m < nCols; ++m) {
            let newCol = newRow.insertCell(m);
            newCol.addEventListener('click', chooseColour)
       }
    }
    event.preventDefault();
}

document.getElementById('sizePicker').addEventListener('submit', makeGrid);
