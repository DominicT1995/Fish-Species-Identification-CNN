const url = "/api/v1.0/fishjson";

var globalData = [];

var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};

function init(data) {

    globalData.push(data);

    var fish_info = globalData[0];

    const form = document.querySelector('form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok) {

            for (let i = 0; i < fish_info.length; i++) {

                if (result.predicted_class == fish_info[i]['Class']) {

                    var fish_index = i;
                }
            }

            console.log(typeof fish_info[fish_index]['Maximum Length']);

            if (fish_info[fish_index]['Maximum Length'] == 0) {

                fish_info[fish_index]['Maximum Length'] = 'N/A';
            }
            else if ( typeof fish_info[fish_index]['Maximum Length'] == "number") {

                fish_info[fish_index]['Maximum Length'] = fish_info[fish_index]['Maximum Length'] + ' inches';
            }

            resultDiv.innerHTML = `
                <img src="${fish_info[fish_index]['Image Link']}" class="figure-img img-fluid rounded">
                <p><strong>Predicted Fish:</strong> ${fish_info[fish_index]['Fish Name']}</p>
                <p><strong>Confidence:</strong> ${(result.confidence * 100).toFixed(2)}%</p>
                <p><strong>Daily Bag Limit:</strong> ${fish_info[fish_index]['Daily Bag Limit']}</p>
                <p><strong>Minimum Length:</strong> ${fish_info[fish_index]['Minimum Length']} inches</p>
                <p><strong>Maximum Length:</strong> ${fish_info[fish_index]['Maximum Length']}</p>
                <p><strong>Possession Limit:</strong> ${fish_info[fish_index]['Possession Limits']}</p>
                <p><a href="https://tpwd.texas.gov/regulations/outdoor-annual/fishing/freshwater-fishing/freshwater-fishing-laws-and-exceptions/" target="_blank">${fish_info[fish_index]['Exceptions']}</a></p>
            `;

        } else {
            resultDiv.innerHTML = `<p>Error: ${result.error}</p>`;
        }
    });

};

d3.json(url).then(data => init(data));


