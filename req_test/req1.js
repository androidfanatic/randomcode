var request = require('request')

function queryString(arr) {
    var obj = new Array();
    if (arr) {
        for (var key in arr) {
            obj.push(key + '=' + encodeURIComponent(arr[key]));
        }
    }
    return obj.join('&');
}

function makeRequest(url, method, data, callback) {

    var req = request({
        uri: url,
        method: method,
        body: queryString(data),
        headers: { 'content-type': 'application/x-www-form-urlencoded' }
    }, function(err, data) {
        if (err) console.log(err)
        else callback(data)
    })
};

makeRequest(
    'https://jsonplaceholder.typicode.com/posts',
    'GET', null,
    function(data) {
        var posts = JSON.parse(data.body);
        console.log('Got ' + posts.length + ' posts');
    }
);

makeRequest(
    'https://jsonplaceholder.typicode.com/posts',
    'POST', {
        "userId": 1,
        "id": 1,
        "title": "Post title",
        "body": "This is just a post"
    },
    function(data) {
        console.log('Added: ' + data.body);
    }
);

makeRequest(
    'https://jsonplaceholder.typicode.com/posts/1',
    'PUT', {
        "userId": 1,
        "id": 1,
        "title": "Post title",
        "body": "This is just a NEW post"
    },
    function(data) {
        console.log('Updated: ' + data.body);
    }
);

makeRequest(
    'https://jsonplaceholder.typicode.com/posts/1',
    'DELETE', null,
    function(data) {
        console.log('Deleted: ');
    }
);