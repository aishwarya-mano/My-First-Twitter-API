// Javascript functions written by Vidhi Agarwal

const tweet = document.getElementById('ctweet');
const id = document.getElementById('dtweet');
const statusc = document.getElementById('StatusC');
const statusd = document.getElementById('StatusD');

const createb = document.getElementById('sbutton');
if (createb) {
    createb.addEventListener('click', createTweet);
}

const deleteb = document.getElementById('dbutton');
if (deleteb) {
    deleteb.addEventListener('click', deleteTweet);
}

function createTweet() {
    fetch('http://127.0.0.1:5000/create', {
        method: 'POST',
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        },
        body: JSON.stringify({
            "text": tweet.value
        })
    }).then(response => {
          	if(response.status == 200) {
                statusc.innerHTML = "Successfully tweet created";
          	} else {
          		statusc.innerHTML = "Error in creating tweet" + ":" + response.status;
          	}
          });

}
const dtweet = document.getElementById("dtweet");
function deleteTweet() {
    fetch('http://127.0.0.1:5000/delete/' + id.value, {
        method: 'DELETE'
    }).then(response => {
          	if(response.status == 200) {
                statusd.innerHTML = "Successfully tweet deleted";
          	} else {
          		statusd.innerHTML = "Error in deleting tweet"+ ":" + response.status;
          	}
          });
}
