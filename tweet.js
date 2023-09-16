const tweet = document.getElementById('ctweet');
const id = document.getElementById('dtweet');
const createb = document.getElementById('sbutton');
const deleteb = document.getElementById('dbutton');
createb.addEventListener('click',createTweet);
deleteb.addEventListener('click',deleteTweet);
function createTweet() {
               fetch('http://127.0.0.1:5000/api/create' , {
               method: 'POST',
               body:JSON.stringify({
    	       "text": tweet.value
            })
})}
const dtweet = document.getElementById("dtweet");
function deleteTweet() {
    fetch('http://127.0.0.1:5000/api/delete/' + id.value , {
               method: 'POST'
               })
            }
