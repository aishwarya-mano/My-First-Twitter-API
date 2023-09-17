// Javascript functions written by Vidhi Agarwal

const tweet = document.getElementById('ctweet');
const id = document.getElementById('dtweet');

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
    });

}
const dtweet = document.getElementById("dtweet");
function deleteTweet() {
    fetch('http://127.0.0.1:5000/delete/' + id.value, {
        method: 'DELETE'
    })
}